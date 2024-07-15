from flask import Flask, request, redirect, render_template
import random
import string
import sqlite3

app = Flask(__name__)
#shortened_urls = {}
#instead of data dictionnary am going to use a data base 

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['POST', 'GET'])
def shorten_url():
    if request.method == "POST":
        long_url = request.form.get('long_url')
        if not long_url:
            return "Please provide a URL to shorten."

        short_url = generate_short_url()
        # while short_url in shortened_urls:
        #     short_url = generate_short_url()
        # we gonna search in the datatable
        conn = get_db_connection()
        while conn.execute('SELECT 1 FROM urls WHERE short_url = ?', (short_url,)).fetchone():
            short_url = generate_short_url()

        conn.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (long_url, short_url))
        conn.commit()
        conn.close()
        return f"Shortened URL: {request.url_root}{short_url}"

    return render_template("index.html")

@app.route('/<short_url>')
def redirect_to_original(short_url):
    conn = get_db_connection()
    row = conn.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,)).fetchone()
    conn.close()
    if row:
        return redirect(row['original_url'])
    else:
        return "URL not found."

@app.route('/data')
def show_data():
    conn = get_db_connection()
    rows = conn.execute('SELECT * FROM urls').fetchall()
    conn.close()
    return render_template('data.html', rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
