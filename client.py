import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Configure server connection
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            # Initialize session
            await session.initialize()
            
            # Test 1: List files
            print("=== Testing list_files ===")
            result = await session.call_tool("list_files", arguments={"directory": "."})
            print(f"Result: {result}\n")
            
            # Test 2: Search for Python files
            print("=== Testing search_files ===")
            result = await session.call_tool("search_files", 
                                            arguments={"directory": ".", "extension": "py"})
            print(f"Result: {result}\n")
            
            # Test 3: Get file info
            print("=== Testing get_file_info ===")
            result = await session.call_tool("get_file_info", 
                                            arguments={"file_path": "server.py"})
            print(f"Result: {result}\n")

if __name__ == "__main__":
    asyncio.run(main())
