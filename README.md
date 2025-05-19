# PhoneLCDParts MCP Server

This project provides a Model Context Protocol (MCP) server with a tool to scrape product search results from `phonelcdparts.com`.

## Purpose

The primary tool, `scrape_phonelcdparts`, allows an MCP-compatible client (like an LLM agent) to query the `phonelcdparts.com` website for products based on a search term. It returns structured JSON data containing the product name, price, direct URL, and image URL.

This enables automated product information retrieval for various applications, such as price tracking, data analysis, or integration into larger AI-driven workflows.

## Prerequisites

*   Python 3.12 or higher.
*   [`uv`](https://github.com/astral-sh/uv) (for environment and package management).
*   A valid Firecrawl API key (from [firecrawl.dev](https://firecrawl.dev)).

## Setup

1.  **Clone the repository (if applicable) or navigate to the project directory:**
    ```bash
    cd path/to/phonelcdpart-mcp
    ```

2.  **Create and activate a virtual environment using `uv`:**
    ```bash
    uv venv
    source .venv/bin/activate
    ```

3.  **Configure Firecrawl API Key:**
    Create a file named `.env` in the `phonelcdpart-mcp` project root directory (i.e., `phonelcdpart-mcp/.env`).
    Add your Firecrawl API key to this file:
    ```env
    FIRECRAWL_API_KEY="YOUR_ACTUAL_FIRECRAWL_API_KEY_HERE"
    ```
    The application uses the `python-dotenv` library to load this key at runtime.

4.  **Install dependencies using `uv`:**
    ```bash
    uv pip install .
    ```
    This will install all dependencies listed in `pyproject.toml`, including `python-dotenv`.

## Running the MCP Server

You have a few options to run the server:

1.  **Directly using Python (for simple development):**
    ```bash
    python app.py
    ```

2.  **Using Uvicorn (recommended for development, provides auto-reload):**
    Ensure `uvicorn` is installed (it's in `pyproject.toml`).
    ```bash
    uvicorn app:mcp --reload --host 0.0.0.0 --port 8000
    ```
    (The `app:mcp` refers to the `mcp` instance of `FastMCP` in your `app.py` file.)

3.  **Using the installed script (if `uv pip install .` was successful):**
    After a successful `uv pip install .`, a script defined in `pyproject.toml` should be available:
    ```bash
    start-mcp
    ```
    This will typically use the `mcp.run()` method.

The server will usually start on `http://127.0.0.1:8000` or `http://0.0.0.0:8000`.

## Using the Tool

Once the server is running, you can interact with it using any MCP-compatible client.

*   **Tool Name:** `scrape_phonelcdparts`
*   **Description (from docstring):** Scrapes product information (name, price, URL, image URL) from `phonelcdparts.com` for a given search query.
*   **Argument:**
    *   `search_query` (string): The product search term (e.g., "iphone 15 pro max lcd").
*   **Returns:** A list of dictionaries, where each dictionary contains:
    *   `name` (string)
    *   `price` (string)
    *   `url` (string)
    *   `image_url` (string)

**Example Call (conceptual, using a Python client):**

```python
# (This is a conceptual example of how a client might call the tool)
# import asyncio
# from fastmcp import Client
#
# async def main():
#     # Ensure the server_url matches where your MCP server is running
#     server_url = "http://127.0.0.1:8000/sse" 
#     async with Client(server_url) as client:
#         try:
#             result = await client.call_tool(
#                 "scrape_phonelcdparts", 
#                 {"search_query": "iphone 14 screen"}
#             )
#             if result and result.data:
#                 print("Tool Result:")
#                 for item in result.data:
#                     print(item)
#             else:
#                 print("No data returned or tool call failed.")
#         except Exception as e:
#             print(f"Error calling tool: {e}")
#
# if __name__ == "__main__":
#     asyncio.run(main())
```

This client code would connect to your running MCP server and invoke the `scrape_phonelcdparts` tool with the specified search query, then print the structured JSON results.
