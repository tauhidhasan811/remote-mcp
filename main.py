from fastmcp import FastMCP



mcp = FastMCP()

@mcp.tool
def sum(a: float, b: float):
    return a + b


def main():
    print("Hello from remote-mcp!")


if __name__ == "__main__":
    #main()
    mcp.run(transport="http", host="0.0.0.0", port=8000)
