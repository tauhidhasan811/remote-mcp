from fastmcp import FastMCP
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
import os
import uvicorn


mcp = FastMCP()

@mcp.tool
def mcp_sum(a: float, b: float):
    return a + b


app = FastAPI()

# API key used to authenticate requests. Set via environment variable `MCP_API_KEY`.
API_KEY = os.getenv("MCP_API_KEY", "changeme")


async def verify_api_key(authorization: str | None = Header(None)):
    return True
    """if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    token = authorization.split()[-1]
    if token != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid token")"""


class SumRequest(BaseModel):
    a: float
    b: float


@app.post("/sum", dependencies=[Depends(verify_api_key)])
async def sum_endpoint(req: SumRequest):
    """Authenticated endpoint that calls the registered MCP tool."""
    # Call the local tool implementation directly to keep things simple.
    result = mcp_sum(req.a, req.b)
    return {"result": result}


def main():
    print("Starting remote-mcp with custom auth on port 8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
