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

"""Pydantic schemas and models defining the data contract for NestAI."""

from pydantic import BaseModel, Field


class LifeScore(BaseModel):
    """Breakdown of quality of life scores (0-100) for a neighborhood."""

    housing: float = Field(
        ..., description="Housing suitability and pricing rating (0-100)"
    )
    education: float = Field(
        ..., description="Educational options and school rating (0-100)"
    )
    healthcare: float = Field(
        ..., description="Medical facilities and accessibility rating (0-100)"
    )
    commute: float = Field(
        ..., description="Transit options and commute ease rating (0-100)"
    )
    affordability: float = Field(
        ..., description="Overall cost-of-living and affordability rating (0-100)"
    )
    family_friendliness: float = Field(
        ..., description="Family friendliness and safety rating (0-100)"
    )


class CandidateNeighborhood(BaseModel):
    """A neighborhood shortlisted by the Housing Agent for further evaluation."""

    name: str = Field(..., description="Name of the neighborhood.")

    estimated_rent_range: str = Field(..., description="Typical monthly rent range.")

    short_summary: str = Field(
        ..., description="Brief explanation of why this neighborhood was selected."
    )

    confidence_score: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Housing Agent's confidence in this recommendation.",
    )


class HousingReport(BaseModel):
    """Structured report returned by the Housing Agent."""

    neighborhoods: list[CandidateNeighborhood] = Field(
        ..., description="Candidate neighborhoods selected for further evaluation."
    )

    average_rent_range: str = Field(
        ..., description="Average rent range across the shortlisted neighborhoods."
    )

    average_purchase_price_range: str = Field(
        ...,
        description="Typical purchase price range across the shortlisted neighborhoods.",
    )

    housing_score: float = Field(
        ..., ge=0, le=100, description="Housing suitability score (0-100)."
    )

    listings_sample: list[dict[str, str]] = Field(
        default_factory=list,
        description="Optional sample property listings for demonstration purposes.",
    )


class SchoolReport(BaseModel):
    """Structured report returned by the School Agent."""

    recommended_schools: list[dict[str, str]] = Field(
        ..., description="List of recommended schools and grades, including ratings"
    )
    average_rating: float = Field(
        ..., description="Average rating score of nearby schools (0-10)"
    )
    education_score: float = Field(
        ..., description="Overall schooling and childcare index (0-100)"
    )
    explanation: str = Field(
        ...,
        description="Explanation of school selection and neighborhood childcare options",
    )


class HealthcareReport(BaseModel):
    """Structured report returned by the Healthcare Agent."""

    nearest_hospitals: list[dict[str, str]] = Field(
        ..., description="Main healthcare centers and hospitals in target area"
    )
    healthcare_score: float = Field(
        ..., description="Overall medical accessibility and quality index (0-100)"
    )
    explanation: str = Field(
        ..., description="Summary of healthcare facilities, rating, and distances"
    )


class CommuteReport(BaseModel):
    """Structured report returned by the Commute Agent."""

    commute_durations: dict[str, str] = Field(
        ...,
        description="Commute times for various transport modes to workplaces (e.g., {'car': '25 min', 'transit': '40 min'})",
    )
    commute_score: float = Field(
        ..., description="Overall transport and commute ease index (0-100)"
    )
    explanation: str = Field(
        ...,
        description="Detailed explanation of highway access, transit availability, and commuter paths",
    )


class BudgetReport(BaseModel):
    """Structured report returned by the Budget Agent."""

    monthly_cost_estimate: dict[str, float] = Field(
        ...,
        description="Estimated monthly expenses breakdown (utilities, transit, groceries, etc.)",
    )
    affordability_score: float = Field(
        ..., description="Overall cost-of-living compatibility index (0-100)"
    )
    explanation: str = Field(
        ...,
        description="Review of cost bounds, regional taxes, and pricing adjustments",
    )


class NeighborhoodAnalysis(BaseModel):
    """Consolidated neighborhood analysis including specialty reports and calculated LifeScore."""

    neighborhood_name: str = Field(..., description="Name of the neighborhood")
    lifescore: LifeScore = Field(..., description="LifeScore calculations")
    housing_analysis: HousingReport = Field(
        ..., description="Housing specialist's detailed analysis"
    )
    school_analysis: SchoolReport = Field(
        ..., description="Education specialist's detailed analysis"
    )
    healthcare_analysis: HealthcareReport = Field(
        ..., description="Healthcare specialist's detailed analysis"
    )
    commute_analysis: CommuteReport = Field(
        ..., description="Transit specialist's detailed analysis"
    )
    budget_analysis: BudgetReport = Field(
        ..., description="Affordability specialist's detailed analysis"
    )
    explanation: str = Field(
        ...,
        description="Detailed synthesis explaining exactly why these scores were assigned",
    )


class RelocationChecklist(BaseModel):
    """Action items checklist for the relocation process."""

    pre_move_tasks: list[str] = Field(
        ..., description="Tasks to complete before moving"
    )
    post_move_tasks: list[str] = Field(
        ..., description="Tasks to complete after arriving"
    )


class RelocationPlan(BaseModel):
    """Final consolidated plan generated by the Coordinator."""

    target_city: str = Field(..., description="The city of relocation")
    neighborhood_recommendations: list[NeighborhoodAnalysis] = Field(
        ..., description="Side-by-side analysis of target neighborhoods"
    )
    relocation_checklist: RelocationChecklist = Field(
        ..., description="Actionable checklist for the move"
    )
    overall_summary: str = Field(
        ..., description="Coordinator's synthesized final advice and guidance"
    )
