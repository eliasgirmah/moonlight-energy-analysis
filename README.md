Week 0 Challenge: MoonLight Energy Solutions
Solar Radiation Data Analysis	
This repository contains the code and analysis for the Week 0 Challenge in MoonLight Energy Solutions. This challenge is part of the evaluation for a 12-week training program in Data Engineering (DE), Financial Analytics (FA), and Machine Learning Engineering (MLE). The main components of this repository include:
•	Exploratory Data Analysis (EDA): Analyzing data to uncover trends and patterns.
•	Statistical Analysis: Utilizing statistical techniques to guide data-driven decisions.
•	Streamlit Dashboard: Creating an interactive tool to present key insights.
Project Structure
MOONLIGHT-ENERGY-ANALYSIS/
│
├── .github/             # GitHub workflows
│   └── workflows/
│       └── unittests.yml
│
├── .gitignore           # Git ignore file
├── .vscode/             # VS Code settings
│   └── settings.json
│
├── data/                # Contains raw and processed data files
│
├── notebooks/           # Jupyter notebooks for analysis
│
├── scripts/             # Scripts for running the analysis
│   ├── __init__.py
│   └── README.md
│
├── src/                # Source code for data processing and analysis
│   ├── __init__.py
│   └── myapp.py
│
├── tests/               # Unit tests
│   └── __init__.py
│
├── venv/                # Virtual environment
│
└── requirements.txt     # Python package dependencies
How to Run
1.	Clone the Repository
git clone https://github.com/eliasgirmah/moonlight-energy-analysis.git
cd   moonlight-energy-analysis
2.	Set up a Python environment and install dependencies:
python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt
3.	Run the Jupyter notebooks for EDA:
jupyter notebook notebooks/
4.	Run the Application:
      streamlit run scripts/app.py

