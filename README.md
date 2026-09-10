# KCET Rank Predictor

A command-line tool that compares a student's Karnataka Common Entrance Test rank with historical engineering-college cutoffs and returns up to ten matching college and branch options.

## Features

- Rank, reservation-category, and branch filtering
- Historical cutoff data for 2019, 2020, and 2021
- Top-ten result display
- Previous-year cutoff comparison
- Included static front-end concept

## Repository contents

| Path | Purpose |
|---|---|
| `kcet final.py` | Command-line prediction workflow |
| `CET_Database_Final2019.csv` | 2019 cutoff data |
| `CET_Database_Final2020.csv` | 2020 cutoff data |
| `CET_Database_Final2021.csv` | 2021 cutoff data |
| `index.html`, `style.css` | Non-functional front-end concept |
| `KCET Rank Predictor.png` | Project image |
| `K - CET draft.pptx` | Project presentation |

## Setup

```bash
git clone <repository-url>
cd KCET-Rank-Predictor

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python "kcet final.py"
```

Enter:

1. A category code such as `GM`, `2AG`, `SCG`, or `STG`
2. Your numeric rank
3. The dataset's exact branch label, such as `CS-Computers`

The program prints up to ten rows whose 2021 cutoff is compatible with the supplied rank, along with the available 2020 and 2019 values.

## How it works

The script loads the three included CSV files, sorts the 2021 records by the selected category, filters by rank and branch, and joins matching college codes to earlier-year cutoff values.

## Front-end status

The included HTML and CSS are a visual prototype only. The submit button is not connected to the Python predictor; use the command-line script for working results.

## Data and limitations

- The repository contains historical data, not current admission cutoffs.
- A result is an estimate and does not guarantee admission.
- Category and branch inputs must match CSV column values exactly.
- Verify decisions against current official counseling publications.
- Public college-site addresses have been removed from the bundled dataset.
