from mcp.server.fastmcp import FastMCP
import os
from pathlib import Path
import json

# Initialize MCP server
mcp = FastMCP("FileSystem Server")

# Tool 1: List files in directory
@mcp.tool()
def list_files(directory: str) -> list:
    """List all files in the given directory"""
    try:
        path = Path(directory)
        if not path.exists():
            return {"error": f"Directory {directory} does not exist"}
        
        files = [str(f) for f in path.iterdir()]
        return {"files": files, "count": len(files)}
    except Exception as e:
        return {"error": str(e)}

# Tool 2: Read file contents
@mcp.tool()
def read_file(file_path: str) -> str:
    """Read contents of a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {"content": content, "size": len(content)}
    except Exception as e:
        return {"error": str(e)}

# Tool 3: Search files by extension
@mcp.tool()
def search_files(directory: str, extension: str) -> list:
    """Search for files with specific extension"""
    try:
        path = Path(directory)
        matches = list(path.glob(f"**/*.{extension}"))
        return {"matches": [str(m) for m in matches], "count": len(matches)}
    except Exception as e:
        return {"error": str(e)}

# Tool 4: Get file info
@mcp.tool()
def get_file_info(file_path: str) -> dict:
    """Get detailed information about a file"""
    try:
        stat = os.stat(file_path)
        return {
            "name": os.path.basename(file_path),
            "size": stat.st_size,
            "modified": stat.st_mtime,
            "is_file": os.path.isfile(file_path)
        }
    except Exception as e:
        return {"error": str(e)}

# Resource: Project structure
@mcp.resource("project://structure")
def get_project_structure() -> str:
    """Get current project directory structure"""
    cwd = os.getcwd()
    return f"Current working directory: {cwd}"

# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
