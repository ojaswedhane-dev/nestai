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
# See the License for the License.
# limitations under the License.

"""NestAI Coordinator Agent and App definitions."""

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools import ToolContext

from app.specialists import (
    budget_agent,
    commute_agent,
    healthcare_agent,
    housing_agent,
    school_agent,
)


def save_candidate_neighborhoods(
    neighborhoods: list[str], tool_context: ToolContext
) -> dict:
    """Stores candidate neighborhoods for downstream specialist evaluation."""

    tool_context.state["candidate_neighborhoods"] = neighborhoods

    return {
        "status": "success",
        "message": "Candidate neighborhoods successfully stored.",
    }


root_agent = Agent(
    name="coordinator_agent",
    model=Gemini(model="gemini-flash-latest"),
    description=(
        "Coordinates the complete NestAI relocation workflow by gathering "
        "preferences, delegating work to specialist agents, and presenting "
        "the final relocation plan."
    ),
    instruction="""
You are the NestAI Coordinator.

You are an orchestration agent.

You NEVER perform specialist reasoning yourself.

==================================================
WORKFLOW
==================================================

STEP 1 — Gather User Preferences

Collect:

• Destination city (required)

• Monthly housing budget (required)

• Family size (required)

• Children (yes/no) (required)

• Office location (optional)

• Commute preference (required)

If any required information is missing, ask follow-up questions.

Do not continue until all required information has been collected.

==================================================

STEP 2 — Validate

Verify that all required fields are reasonable and complete.

==================================================

STEP 3 — Housing Analysis

Delegate the request to the Housing Agent.

Receive the HousingReport.

Extract the candidate neighborhoods.

Store them using the save_candidate_neighborhoods tool.

==================================================

STEP 4 — Specialist Evaluation

Delegate the candidate neighborhoods to:

• School Agent

• Healthcare Agent

• Commute Agent

• Budget Agent

Collect every structured report.

==================================================

STEP 5 — Final Recommendation

Combine the outputs from every specialist.

Present:

• Candidate neighborhoods

• Housing summary

• Education summary

• Healthcare summary

• Commute summary

• Budget summary

Explain the strengths and trade-offs of each neighborhood.

If an overall LifeScore is available from the application, include it in the final explanation.

Do NOT invent missing specialist outputs.

Do NOT fabricate data.

Always explain uncertainty when information is unavailable.

==================================================

GENERAL RULES

• Never guess housing prices.

• Never invent hospitals.

• Never invent schools.

• Never invent commute times.

• Never fabricate listings.

• Delegate specialist work whenever possible.

• Produce a concise, organized, user-friendly final response.
""",
    tools=[
        save_candidate_neighborhoods,
    ],
    sub_agents=[
        housing_agent,
        school_agent,
        healthcare_agent,
        commute_agent,
        budget_agent,
    ],
)

# TODO:
# Integrate Browser / Puppeteer MCP for live housing and school searches.
#
# TODO:
# Integrate Google Maps MCP for commute analysis.
#
# TODO:
# Integrate custom Skills:
# - Neighborhood Comparison
# - Budget Breakdown
# - Relocation Checklist

app = App(
    root_agent=root_agent,
    name="app",
)
