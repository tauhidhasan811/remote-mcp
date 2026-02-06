import os
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()


mcp = FastMCP()
API_KEY=-os.environ.get('MCP_API_KEY')


@mcp.tool
def sum(a: float, b: float):
    return a + b


def main():
    print("Hello from remote-mcp!")


if __name__ == "__main__":
    #main()
    mcp.run(transport="http", host="0.0.0.0", port=8000,
            auth_token=API_KEY
            )
