# league-analysis
League of Legends Player Analysis

Introduction
This project provides an in-depth analysis of professional League of Legends players, utilizing advanced statistical models to evaluate player performance and team dynamics. The methodology involves regression analysis using various models such as linear regression, random forest, and XGBoost to determine the significance of player statistics in relation to their win rate.

Key Features
Player Rating Calculation: The project calculates individual player ratings using coefficients/importance values derived from players' statistics.
Team Ratings: These player ratings are aggregated to form overall team ratings.
Win Rate Estimation: A logistic function is employed to estimate implied win rates based on the differences between team ratings.
Odds Comparison: The project calculates implied odds for each team across different leagues and offers a comparative analysis against bookmakers' odds.
Project Data
Player data is sourced from Oracle's Elixir, collected from Match History pages, lolesports.com, lpl.QQ.com, Leaguepedia, the Riot Games solo queue APIs, and more.

Installation & Running the Project
Option 1: Python Based
Prerequisites: Python 3.9.7
Setup:
Clone the repository: git clone [repository URL]
Navigate to the project directory
Install dependencies: pip install -r requirements.txt
Running the App: Execute python app.py in the project directory. Some environment/variable setups may vary between users.
Option 2: Docker Based
Pulling the Project Image:
docker pull aryanbhatla/league-analysis-image
Running as a Container:
docker run -p 8501:8501 aryanbhatla/league-analysis-image
Usage
Upon running the application, users can navigate through the interface to view and interact with the statistical analyses and comparisons. The tool provides insights into player performances, team strengths, and potential outcomes based on statistical models.

Troubleshooting
For issues, please check Python and Docker versions for compatibility. For more specific problems, open an issue in the repository.

Contact
For support or inquiries, contact aryan.bhatla184@gmail.com
