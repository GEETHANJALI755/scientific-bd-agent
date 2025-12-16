# Stage 3: Assign probability score (0–100)
import pandas as pd

HUB_LOCATIONS = [
    "Boston MA",
    "Cambridge MA",
    "San Francisco",
    "Bay Area",
    "Basel",
    "London",
    "Oxford",
    "Cambridge UK"
]

def score_lead(row: pd.Series) -> int:
    score = 0

    # Role Fit
    if any(k in row["title"] for k in ["Director", "Head", "VP"]):
        score += 30

    # Location Hub
    if row["company_hq"] in HUB_LOCATIONS:
        score += 10

    # Scientific Intent
    if row.get("recent_pub", False):
        score += 40

    # Company Funding (simulated flag)
    if row.get("funded", False):
        score += 20

    return min(score, 100)


def apply_scoring(df: pd.DataFrame) -> pd.DataFrame:
    df["probability_score"] = df.apply(score_lead, axis=1)
    return df

if __name__ == "__main__":
    from identifier import identify_targets
    from enricher import enrich_with_scientific_intent

    df = identify_targets("data/linkedin_profiles.csv")
    df = enrich_with_scientific_intent(df)
    df = apply_scoring(df)

    print(df[["name", "title", "company", "probability_score"]])
