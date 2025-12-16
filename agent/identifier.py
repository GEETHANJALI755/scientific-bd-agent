# Stage 1: Identify target profiles from LinkedIn-style input
import pandas as pd

TARGET_KEYWORDS = [
    "Director",
    "Head",
    "VP",
    "Safety",
    "Toxicology",
    "Preclinical"
]

def identify_targets(csv_path: str) -> pd.DataFrame:
    """
    Stage 1: Identify relevant BD targets based on role/title.
    """
    df = pd.read_csv(csv_path)

    def is_relevant(title: str) -> bool:
        title = str(title)
        return any(keyword.lower() in title.lower() for keyword in TARGET_KEYWORDS)

    df["is_target"] = df["title"].apply(is_relevant)

    return df[df["is_target"]].reset_index(drop=True)

if __name__ == "__main__":
    targets = identify_targets("data/linkedin_profiles.csv")
    print(targets[["name", "title", "company"]])
