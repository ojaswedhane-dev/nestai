"""
Budget Breakdown Skill.

Creates an easy-to-read monthly budget summary.
"""

from app.models import BudgetReport


def generate_budget_breakdown(
    report: BudgetReport,
) -> str:

    expenses = report.monthly_cost_estimate

    lines = ["Monthly Budget Breakdown", "-" * 35]

    total = 0

    for category, value in expenses.items():
        total += value
        lines.append(f"{category}: ${value:.2f}")

    lines.append("")
    lines.append(f"Estimated Total: ${total:.2f}")
    lines.append("")
    lines.append(report.explanation)

    return "\n".join(lines)
