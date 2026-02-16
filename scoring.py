import pandas as pd

df = pd.read_csv("parent_master_final.csv")

# --- Manual Overrides for Known Large Sponsors ---
OVERRIDES = {
    "amazon": "amazon com services",
    "aws": "amazon web services",
    "microsoft": "microsoft",
    "google": "google",
    "meta": "meta",
    "infosys": "infosys"
}

def normalize_input(name: str) -> str:
    return name.lower().strip()

def compute_company_profile(company_name: str):
    name = normalize_input(company_name)

    # Apply override if exists
    if name in OVERRIDES:
        name = OVERRIDES[name]

    # Exact match
    result = df[df["PARENT_KEY"] == name]

    if not result.empty:
        row = result.iloc[0]
        return {
            "company": row["PARENT_KEY"],
            "h1b_score": round(row["H1B_SCORE"], 2),
            "h1b_tier": row["H1B_TIER"],
            "opt_score": round(row["OPT_SCORE"], 2),
            "opt_tier": row["OPT_TIER"],
            "total_workers_5yr": int(row["TOTAL_WORKERS_5YR"]),
            "total_workers_3yr": int(row["TOTAL_WORKERS_3YR"])
        }

   # Partial search fallback
partial = df[df["PARENT_KEY"].str.contains(name, na=False)]

if partial.empty:
    return None

# Return only the top match instead of list
row = partial.sort_values("H1B_SCORE", ascending=False).iloc[0]

return {
    "company": row["PARENT_KEY"],
    "h1b_score": round(row["H1B_SCORE"], 2),
    "h1b_tier": row["H1B_TIER"],
    "opt_score": round(row["OPT_SCORE"], 2),
    "opt_tier": row["OPT_TIER"],
    "total_workers_5yr": int(row["TOTAL_WORKERS_5YR"]),
    "total_workers_3yr": int(row["TOTAL_WORKERS_3YR"])
}
