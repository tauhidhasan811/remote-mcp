FastMCP custom authentication
=============================

This project runs a small FastAPI proxy in front of your FastMCP tools so you can implement custom authentication.

How it works
- The proxy exposes authenticated HTTP endpoints (e.g. `/sum`) that call the local MCP tool implementations.
- Set `MCP_API_KEY` to a secret value and send `Authorization: Bearer <MCP_API_KEY>` with requests.

Disable FastMCP built-in identity provider
- By default this project runs the custom FastAPI proxy (the built-in FastMCP Identity Provider is not started).
- To run FastMCP's native HTTP transport (which may enable its built-in IDP), set environment variable `FASTMCP_IDP=on`.

Run locally
```bash
pip install fastmcp fastapi "uvicorn[standard]"
export MCP_API_KEY=mysupersecret
python main.py
```

Example request
```bash
curl -X POST http://localhost:8000/sum \
	-H "Authorization: Bearer mysupersecret" \
	-H "Content-Type: application/json" \
	-d '{"a": 1.5, "b": 2.5}'
```

If you want full OAuth2/OpenID Connect flows, you'll need to integrate an OAuth provider or implement the flows yourself; FastMCP's built-in IDP is currently the simplest option but can be turned off to allow custom auth.

Disable all authentication
--------------------------

If you do not want any authentication at all (anonymous access), set the `NO_AUTH` environment variable to a truthy value and ensure the FastMCP identity provider is not started.

Windows (CMD):
```bat
set NO_AUTH=1
set FASTMCP_IDP=off
python main.py
```

PowerShell:
```powershell
$env:NO_AUTH = '1'
$env:FASTMCP_IDP = 'off'
python main.py
```

When `NO_AUTH` is enabled the server will accept requests without an `Authorization` header. When `FASTMCP_IDP` is `off` (the default in this project) FastMCP's built-in identity provider will not be started.

