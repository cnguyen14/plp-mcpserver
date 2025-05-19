## PhoneLCDPartsScraper MCP Server

This MCP server provides a tool to scrape product search results from [phonelcdparts.com](https://www.phonelcdparts.com). It allows users to programmatically retrieve details about products based on a search query.

**Functionality:**
-   Searches `phonelcdparts.com` for a given query.
-   Extracts key information for each product found on the search results page.

**Tool Provided:**
-   `scrape_phonelcdparts`
    -   **Description:** Scrapes product information (name, price, URL, image URL) from `phonelcdparts.com` based on a search query.
    -   **Input Parameter:** `search_query` (string) - The term to search for (e.g., "iphone 15 pro max lcd").
    -   **Output:** A list of dictionaries, where each dictionary contains:
        -   `name` (string)
        -   `product_url` (string)
        -   `price` (string)
        -   `image_url` (string)

**Server Environment Requirements:**
-   `FIRECRAWL_API_KEY`: An API key for the Firecrawl service is required to fetch website content. This needs to be configured when deploying or running the server.

**Technologies Used:**
-   [FastMCP](https://docs.mcp.so/): For creating the MCP server and tool.
-   [Firecrawl](https://firecrawl.dev/): For crawling and scraping the initial web page content.
-   [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): For parsing the HTML content and extracting product details.

This server is ideal for applications that need to monitor product listings, gather pricing information, or integrate `phonelcdparts.com` product data into other systems. 