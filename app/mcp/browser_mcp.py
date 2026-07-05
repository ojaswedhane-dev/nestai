# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Browser MCP client configuration for web scraping and information gathering."""

import os

from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp import StdioServerParameters


def get_browser_mcp_toolset() -> McpToolset:
    """Returns the Browser/Puppeteer MCP toolset.

    This toolset allows specialist agents to scrape neighborhood details,
    housing directories, and local school statistics.
    """
    # Configure stdio connection parameters to run the Puppeteer MCP server via npx.
    # Design Decision: Using StdioConnectionParams for container scalability.
    return McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-puppeteer"],
                env=os.environ.copy(),
            ),
        ),
        # Expose only specific tools needed for safe web browsing
        tool_filter=[
            "puppeteer_navigate",
            "puppeteer_screenshot",
            "puppeteer_click",
            "puppeteer_fill",
            "puppeteer_evaluate",
        ],
    )
