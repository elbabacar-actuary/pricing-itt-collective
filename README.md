# Actuarial Project Template

Reusable structure for actuarial analytics projects (pricing, reserving, profitability).

## How to use
1. Click **Use this template** (recommended) or clone the repo.
2. Put raw inputs in `data/raw/` (never commit client data).
3. Run cleaning to produce standardized outputs in `data/processed/`.
4. Implement project-specific models in `src/`.

## Folder structure
- `data/raw/` : raw inputs (client extracts, messy data)
- `data/processed/` : cleaned & standardized datasets
- `notebooks/` : exploration / QA / demos
- `src/` : reusable code (loader, cleaning, models, metrics)
- `config.yaml` : business parameters

## Data confidentiality
Client data must remain local. `.gitignore` prevents committing raw/processed data.
Use simulated or anonymized datasets for public demos.
