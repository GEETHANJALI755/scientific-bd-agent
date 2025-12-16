import streamlit as st
import pandas as pd

from agent.identifier import identify_targets
from agent.enricher import enrich_with_scientific_intent
from agent.scorer import apply_scoring

st.set_page_config(page_title="Scientific BD Lead Intelligence", layout="wide")

st.title("🧪 Scientific BD Lead Intelligence Dashboard")
st.write(
    "Ranked list of toxicology and preclinical safety leaders "
    "by probability of working with 3D in-vitro models."
)

# Load & process data
df = identify_targets("data/linkedin_profiles.csv")
df = enrich_with_scientific_intent(df)
df = apply_scoring(df)

# Rank leads
df = df.sort_values(by="probability_score", ascending=False).reset_index(drop=True)
df.insert(0, "Rank", df.index + 1)

# Search / filter
search = st.text_input("🔍 Search by keyword (Boston, Liver, Toxicology, Company)")

if search:
    df = df[df.apply(lambda x: search.lower() in str(x).lower(), axis=1)]

# Display table
st.dataframe(
    df[
        [
            "Rank",
            "probability_score",
            "name",
            "title",
            "company",
            "person_location",
            "company_hq",
            "recent_pub",
            "linkedin_url",
        ]
    ],
    use_container_width=True,
)

# Export
st.download_button(
    label="⬇️ Export Leads to CSV",
    data=df.to_csv(index=False),
    file_name="ranked_bd_leads.csv",
    mime="text/csv",
)
