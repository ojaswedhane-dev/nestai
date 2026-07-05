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

"""Google Maps MCP client configuration for transport, routing, and amenity searches."""

import os

from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp import StdioServerParameters


def get_maps_mcp_toolset() -> McpToolset:
    """Returns the Google Maps MCP toolset.

    This toolset allows commute estimation, hospital search, and travel distance
    lookups for the transit and healthcare specialists.
    """
    env = os.environ.copy()
    api_key = os.getenv("GOOGLE_MAPS_API_KEY", "")
    if api_key:
        env["GOOGLE_MAPS_API_KEY"] = api_key

    # Initialize standard Google Maps MCP server connection
    return McpToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-google-maps"],
                env=env,
            ),
        ),
    )
