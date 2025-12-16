# Stage 2: Enrich profiles with PubMed and business signals
from Bio import Entrez
import pandas as pd
from datetime import datetime

# REQUIRED by NCBI
Entrez.email = "demo@example.com"

KEYWORDS = [
    "liver toxicity",
    "drug-induced liver injury",
    "3D cell",
    "organ-on-chip",
    "hepatic"
]

def has_recent_pubmed_paper(author_name: str, years: int = 2) -> bool:
    """
    Checks if the author has a recent PubMed publication
    related to liver toxicity or 3D in-vitro models.
    """
    query = f'{author_name}[Author] AND ({ " OR ".join(KEYWORDS) })'

    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=5,
        sort="pub date"
    )
    results = Entrez.read(handle)
    pmids = results.get("IdList", [])

    if not pmids:
        return False

    handle = Entrez.esummary(db="pubmed", id=",".join(pmids))
    summaries = Entrez.read(handle)

    current_year = datetime.now().year

    for record in summaries:
        pub_year = int(record.get("PubDate", "0")[:4] or 0)
        if current_year - pub_year <= years:
            return True

    return False


def enrich_with_scientific_intent(df: pd.DataFrame) -> pd.DataFrame:
    df["recent_pub"] = df["name"].apply(has_recent_pubmed_paper)

    # DEMO funding signal
    df["funded"] = df["company"].apply(
        lambda x: True if x in ["HelioBio", "NeoThera"] else False
    )

    return df


if __name__ == "__main__":
    from identifier import identify_targets

    df = identify_targets("data/linkedin_profiles.csv")
    enriched = enrich_with_scientific_intent(df)

    print(enriched[["name", "title", "recent_pub"]])
