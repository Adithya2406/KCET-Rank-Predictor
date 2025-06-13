## KCET Rank Predictor
A data-driven web application that predicts college admissions for KCET aspirants with over 85% accuracy, based on historical cut-off trends. This tool helps students identify the top colleges they are eligible for, guiding them towards informed decisions in the Karnataka Common Entrance Test (KCET) counseling process.

---
**Table of Contents**
- Overview
- Features
- How It Works
- Application & Usage
- Installation & Setup
- Project Structure
- Contributing
- License

---
## Overview
KCET Rank Predictor leverages historical KCET cut-off data (2019–2021) to help students predict which engineering colleges and branches they can secure admission to, given their rank, category, and preferred branch. The application processes user inputs and cross-references them with past admission trends to generate a ranked list of eligible colleges.

---
## Features
- Predicts eligible colleges based on user’s KCET rank, category, and branch preference.
- Utilizes historical cut-off data for three years (2019, 2020, 2021).
- Provides the top 10 best-fit colleges for the user’s profile.
- Displays previous years’ cut-off ranks for transparency and informed decision-making.
- Simple command-line interface for easy use.

---
## How It Works
1. **Input Collection**: The user is prompted to enter their category (e.g., GM, 2AG, SCG), KCET rank, and preferred engineering branch.
2. **Data Processing**: The application loads cut-off datasets for 2019, 2020, and 2021, and sorts the data based on the selected category.
3. **Eligibility Filtering**: It filters colleges where the user’s rank is within the cut-off for their category and branch.
4. **Result Compilation**: The top 10 eligible colleges are displayed, along with their codes and cut-off ranks for the past three years, helping users compare trends and make informed choices.
5. **Output**: Results are presented in a tabular format in the command line.

---
## Application & Usage
KCET Rank Predictor is designed for students appearing for the Karnataka CET, aiming to:
- Identify colleges and branches they are eligible for based on their rank and category.
- Compare historical cut-off trends to assess their chances in different institutes.
- Plan their counseling and college selection strategy more effectively.

**Example Use Case:**
- A student with a KCET rank of 5000 in the GM category for Computer Science can input these details to instantly get a list of top colleges where admission is likely, along with cut-off ranks for 2019, 2020, and 2021.

---
## Installation & Setup

**Prerequisites:**
- Python 3.x
- pandas library

**Steps:**
1. Clone this repository:
   ```bash
   git clone https://github.com/Adithya2406/KCET-Rank-Predictor.git
   cd KCET-Rank-Predictor
   ```
2. Install required libraries:
   ```bash
   pip install pandas
   ```
3. Run the application:
   ```bash
   python "kcet final.py"
   ```
4. Follow the prompts to enter your category, rank, and branch.

---
## Project Structure
- `kcet final.py` — Main Python script for prediction logic.
- `CET_Database_Final2019.csv`, `CET_Database_Final2020.csv`, `CET_Database_Final2021.csv` — Historical cut-off data files.
- `index.html`, `style.css` — (Under development) Web interface files (currently, the main interface is command-line).
- `KCET Rank Predictor.png` — Project logo or screenshot.
- `K - CET draft.pptx` — Project presentation or documentation.

---
## Contributing
Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your improvements or bug fixes.

---
## License
This project is open-source and available under the MIT License.

---
**Disclaimer:** This tool is intended to assist with decision-making and does not guarantee admission. Please refer to official KEA notifications and counseling guidelines for the most accurate and updated information.
---

For any queries or feedback, please open an issue on the repository.
