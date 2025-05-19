import json
import urllib.parse
from firecrawl import FirecrawlApp
from bs4 import BeautifulSoup
from fastmcp import FastMCP

# Initialize FastMCP
mcp = FastMCP(
    name="PhoneLCDPartsScraper", 
    description="Scrapes product search results from phonelcdparts.com",
    dependencies=["firecrawl-py", "beautifulsoup4"] # Explicitly list tool dependencies
)

# --- Global Configuration ---
# IMPORTANT: Replace with your actual Firecrawl API key or load from environment for security
FIRECRAWL_API_KEY = "fc-bda2a324809b4cb2982a607a8c31ffac" 
BASE_SEARCH_URL = "https://www.phonelcdparts.com/catalogsearch/result/?q="

# --- Helper Function ---
def construct_search_url(query: str) -> str:
    """Constructs the full search URL for a given query."""
    encoded_query = urllib.parse.quote_plus(query)
    return f"{BASE_SEARCH_URL}{encoded_query}"

# --- MCP Tool Definition ---
@mcp.tool()
def scrape_phonelcdparts(search_query: str) -> list[dict]:
    """
    Scrapes product information (name, price, URL, image URL) 
    from phonelcdparts.com for a given search query.

    Args:
        search_query (str): The product search query (e.g., "iphone 15 pro max lcd").

    Returns:
        list[dict]: A list of dictionaries, where each dictionary contains
                    the name, price, URL, and image_url of a product. 
                    Returns an empty list if scraping fails or no products are found.
    """
    if not FIRECRAWL_API_KEY or FIRECRAWL_API_KEY == "fc-YOUR_FIRECRAWL_API_KEY":
        print("Error: Firecrawl API key is not set or is a placeholder.")
        # For a real MCP tool, you might want to raise a specific error type
        # that FastMCP can convert to an MCP error response.
        # from fastmcp.exceptions import ToolError
        # raise ToolError("Firecrawl API key is not configured.")
        return []

    app_firecrawl = FirecrawlApp(api_key=FIRECRAWL_API_KEY)
    target_url = construct_search_url(search_query)
    # Use mcp.log for logging within FastMCP tools if context is injected, 
    # or simple print for server console output.
    print(f"MCP Tool: Scraping URL: {target_url}") 

    try:
        scraped_data = app_firecrawl.scrape_url(target_url, formats=['html'])
        
        if not scraped_data:
            print(f"MCP Tool: Firecrawl returned no data for {target_url}.")
            return []

        if not hasattr(scraped_data, 'html') or not scraped_data.html:
            print(f"MCP Tool: Failed to retrieve HTML content from {target_url}.")
            print(f"MCP Tool: Firecrawl response was: {str(scraped_data)}")
            return []

        html_content = scraped_data.html
        
    except Exception as e:
        print(f"MCP Tool: An error occurred during scraping with Firecrawl: {e}")
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    products = []
    
    product_card_forms = soup.find_all('form', class_='product_addtocart_form')

    if not product_card_forms:
        print("MCP Tool: No product card forms found with selector 'form.product_addtocart_form'.")
        return []

    for card_form in product_card_forms:
        try:
            name = 'N/A'
            product_url = 'N/A'
            price = 'N/A'
            image_url = 'N/A'

            name_tag = card_form.find('a', class_='product-item-link')
            if name_tag:
                name = name_tag.text.strip()
                product_url = name_tag.get('href', 'N/A')
            
            price_tag = card_form.find('span', class_='price')
            if price_tag:
                price = price_tag.text.strip()

            img_tag = card_form.find('img', class_='product-image-photo')
            if img_tag:
                image_url = img_tag.get('src', 'N/A')

            products.append({
                'name': name,
                'price': price,
                'url': product_url,
                'image_url': image_url
            })
        except Exception as e:
            print(f"MCP Tool: Error parsing a product card: {e}")
            continue
            
    return products

# --- Main Execution (for running the MCP server) ---
def start_mcp_server(): # Renamed for clarity and to avoid conflict with any potential 'start_server' elsewhere
    print("Starting PhoneLCDPartsScraper MCP server via entry point...")
    # When running this file directly, it will start the FastMCP server.
    # For production, you'd typically use an ASGI server like uvicorn:
    # uvicorn phonelcdpart_mcp.app:mcp --reload (Note: underscore for module name)
    mcp.run()

if __name__ == "__main__":
    print("Starting PhoneLCDPartsScraper MCP server from app.py direct execution...")
    start_mcp_server() # Call the new function 