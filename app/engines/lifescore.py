"""
LifeScore Engine

This module contains deterministic business logic.
It combines the outputs from all specialist agents into
a transparent overall LifeScore.

No LLM reasoning happens here.
"""

from typing import ClassVar

from app.models import (
    BudgetReport,
    CommuteReport,
    HealthcareReport,
    HousingReport,
    LifeScore,
    SchoolReport,
)


class LifeScoreEngine:
    """Computes the final LifeScore for a neighborhood."""

    WEIGHTS: ClassVar[dict[str, float]] = {
        "housing": 0.25,
        "education": 0.20,
        "healthcare": 0.20,
        "commute": 0.15,
        "affordability": 0.20,
    }

    @classmethod
    def calculate_lifescore(
        cls,
        housing: HousingReport,
        school: SchoolReport,
        healthcare: HealthcareReport,
        commute: CommuteReport,
        budget: BudgetReport,
    ) -> dict:

        overall_score = (
            housing.housing_score * cls.WEIGHTS["housing"]
            + school.schooling_score * cls.WEIGHTS["education"]
            + healthcare.healthcare_score * cls.WEIGHTS["healthcare"]
            + commute.commute_score * cls.WEIGHTS["commute"]
            + budget.affordability_score * cls.WEIGHTS["affordability"]
        )

        family_friendliness = (
            school.schooling_score * 0.45
            + healthcare.healthcare_score * 0.25
            + housing.housing_score * 0.20
            + commute.commute_score * 0.10
        )

        return {
            "lifescore": LifeScore(
                housing=round(housing.housing_score, 2),
                education=round(school.schooling_score, 2),
                healthcare=round(healthcare.healthcare_score, 2),
                commute=round(commute.commute_score, 2),
                affordability=round(budget.affordability_score, 2),
                family_friendliness=round(family_friendliness, 2),
            ),
            "overall_score": round(overall_score, 2),
        }
