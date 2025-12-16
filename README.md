# Scientific BD Lead Intelligence Web Agent

## Overview
This project is a lightweight, reviewable AI agent that identifies, enriches, and scores potential scientific business development (BD) leads in biotech/pharma.

It is built directly against the assignment brief and demonstrates:
- Lead identification from structured data
- Scientific enrichment via PubMed
- Simple, explainable scoring
- A Streamlit dashboard for review

---

## Architecture
scientific-bd-agent/
├── data/
│ ├── linkedin_profiles.csv
│ ├── pubmed_enrichment.csv
│
├── agent/
│ ├── identifier.py
│ ├── enricher.py
│ ├── scorer.py
│
├── app.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## How It Works
1. **Identifier Agent**
   - Filters LinkedIn-style profiles for senior scientific BD-relevant roles.

2. **Enrichment Agent**
   - Queries PubMed to detect recent publications (proxy for scientific activity).

3. **Scoring Agent**
   - Combines scientific signals and company funding stage into a probability score.

4. **Dashboard**
   - Displays ranked leads
   - Allows filtering and CSV export

---

## Running the Project

### Install dependencies
```bash
pip install -r requirements.txt
Run agents
bash
Copy code
python agent/identifier.py
python agent/enricher.py
python agent/scorer.py
Launch dashboard
bash
Copy code
python -m streamlit run app.py


Notes
This is a demo agent designed for clarity and reviewability

External APIs are intentionally lightweight or mocked

Scoring logic is transparent and easily extensible

## Agent Methodology (Patch C)...(optional)
This demo implements a web agent that mirrors how a Scientific Business Developer identifies and prioritizes high-value leads for 3D in-vitro models.

Website Categories Used by the Agent

The agent is architected to gather signals from five distinct categories of web sources. Each category contributes a different type of business or scientific intent signal, which is later combined into a probability score.

1. Professional Networks

Examples: LinkedIn, Xing (simulated via CSV or API providers)

Signals Extracted:

Job title and seniority (Director, Head, VP)

Functional area (Toxicology, Preclinical Safety, Safety Assessment)

Person location (remote vs on-site)

Company affiliation

Why This Matters:
Senior decision-makers in toxicology and safety functions are the primary buyers or influencers for in-vitro and NAMs solutions.

2. Scientific Databases

Examples: PubMed, Google Scholar, bioRxiv

Signals Extracted:

Recent publications (within last 24 months)

Keywords such as DILI, liver toxicity, hepatic models, 3D cell culture

Author position (first or corresponding author)

Why This Matters:
Recent scientific output in liver toxicity or related areas indicates active research interest and higher likelihood of adopting advanced in-vitro models.

3. Conference Websites

Examples: SOT, AACR, ISSX, ACT

Signals Extracted:

Speaker or poster presenter status

Session topics related to toxicology, safety, or liver models

Recency of participation

Why This Matters:
Conference presenters are typically engaged, budget-aware, and open to new technologies, making them strong BD targets.

4. Business & Funding Intelligence

Examples: Crunchbase, PitchBook, FierceBiotech

Signals Extracted:

Funding stage (Seed, Series A, Series B, etc.)

Recent fundraising activity

Company growth indicators

Why This Matters:
Funded companies are more likely to have budgets and immediate need for external CRO services and advanced testing models.

5. Grant Databases

Examples: NIH RePORTER, CORDIS (EU)

Signals Extracted:

Active or recent grants related to toxicology or liver research

Grant size and duration

Academic or translational research focus

Why This Matters:
Grant-funded labs often outsource experimental work and are strong prospects for collaborative or service-based engagements.

How These Signals Are Used

Each signal category contributes to a weighted probability score (0–100).
The final ranking reflects the likelihood that a lead would benefit from and be interested in 3D in-vitro model solutions.

This multi-source approach avoids generic lead lists and produces high-intent, BD-ready prospects aligned with real scientific and business demand.