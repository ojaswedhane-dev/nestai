"""
Relocation Checklist Skill.

Produces a personalized moving checklist.
"""

from app.models import RelocationChecklist


def generate_checklist() -> RelocationChecklist:

    return RelocationChecklist(
        pre_move_tasks=[
            "Finalize housing.",
            "Notify employer.",
            "Transfer utilities.",
            "Arrange movers.",
            "Prepare important documents.",
            "Update address.",
        ],
        post_move_tasks=[
            "Inspect new home.",
            "Register with local services.",
            "Locate nearby hospitals.",
            "Visit schools if applicable.",
            "Explore neighborhood amenities.",
            "Update banking and subscriptions.",
        ],
    )
