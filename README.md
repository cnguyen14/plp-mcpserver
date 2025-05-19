# PhoneLCDParts MCP Server

A Model Context Protocol (MCP) server for scraping product search results from [phonelcdparts.com](https://www.phonelcdparts.com) using Firecrawl and BeautifulSoup. This server exposes a tool for programmatically retrieving product information (name, price, URL, image) for any search query.

## Features
- **MCP Tool:** `scrape_phonelcdparts` — Scrape product listings for any search term.
- **Open Source:** MIT License.
- **Ready for MCP.so Hosting:** Includes `chatmcp.yaml` and environment variable support.

## Requirements
- Python 3.12+
- [Firecrawl API Key](https://firecrawl.dev/)

## Installation
Clone the repository and install dependencies (recommended: use a virtual environment):

```bash
uv venv .venv
source .venv/bin/activate
uv pip install .
```

## Usage (Local)
Set your Firecrawl API key and run the server:

```bash
export FIRECRAWL_API_KEY=your_firecrawl_api_key
python app.py
```

Or use the provided script (if installed):
```bash
start-mcp
```

## MCP Tool
### scrape_phonelcdparts
**Arguments:**
- `search_query` (str): The product search query (e.g., "iphone 15 pro max lcd")

**Returns:**
- List of products, each with:
  - `name`: Product name
  - `price`: Price string
  - `url`: Product page URL
  - `image_url`: Product image URL

## Environment Variables
- `FIRECRAWL_API_KEY` (required): Your Firecrawl API key for web scraping.

## MCP.so Hosting
This project is ready for [MCP.so](https://docs.mcp.so/server-hosting) hosting:
- Includes `chatmcp.yaml` for parameter and run command specification.
- Reads API key from environment variable.
- MIT License included.

### To Host:
1. Push your code to a public GitHub repository.
2. Submit your repo to MCP.so for review and hosting.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
