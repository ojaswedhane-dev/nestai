"""
Neighborhood Comparison Skill

Provides an easy-to-understand comparison between
multiple candidate neighborhoods.
"""

from app.models import NeighborhoodAnalysis


def compare_neighborhoods(
    neighborhoods: list[NeighborhoodAnalysis],
) -> str:
    """
    Generates a readable comparison between candidate neighborhoods.
    """

    if not neighborhoods:
        return "No neighborhood analysis is available."

    lines = ["Neighborhood Comparison", "-" * 40]

    for n in neighborhoods:
        lines.append(
            f"""
📍 {n.neighborhood_name}

Housing: {n.lifescore.housing:.1f}/100
Education: {n.lifescore.education:.1f}/100
Healthcare: {n.lifescore.healthcare:.1f}/100
Commute: {n.lifescore.commute:.1f}/100
Affordability: {n.lifescore.affordability:.1f}/100
Family Friendliness: {n.lifescore.family_friendliness:.1f}/100

Summary:
{n.explanation}
"""
        )

    return "\n".join(lines)
