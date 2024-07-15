# URL Shortener Service

This is a simple URL shortener service built using Python and Flask. It shortens long URLs and redirects users to the original URL when accessed.
For exemple: 
long domain : https://mylongsubdomain.mylongdomain.com/somethinf/somthingelse
short domain : localhost/exemple8797917 whiche redirect to the long domain 
## Features

- **Shorten URLs**: Convert long URLs into short, manageable links.
- **Redirect**: Direct users to the original URL when they access the shortened link.
- **Database Storage**: Store mappings between short URLs and original URLs in SQLite.

## Setup

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd url-shortener 
   ```
2. Set up a virtual environment :
```bash
python app.py
```
3. Install dependencies:

```bash
pip install flask
```
## Configuration
Ensure config.py is configured appropriately for your environment .
## Running the Application
Initialize the database:
```bash
python app.py
```

## Usage
Shortening URLs
Endpoint: POST /shorten
Request:
```bash
{
  "original_url": "https://example.com/very/long/url"
}
```
Response:
```bash
{
  "short_url": "http://yourdomain.com/abcxyz"
}
```
Redirecting to Original URL
Access the short URL directly in your browser:
```bash
http://yourdomain.com/abcxyz
```
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.




