#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import pandas as pd 
import team_analysis


#----------------------------------------------------------------------------------------------------- #
# Fetch odds function
#----------------------------------------------------------------------------------------------------- # 
def fetch_odds(team_a: str, team_b: str, odds_df: pd.DataFrame) -> tuple:
    '''
        
        Parameters: 
            team a, team b (str): Teams read in from Excel file
            odds_df (pd.DataFrame): Odds dataframe containing all teams' odds
            
        Returns: 
            odds_a, odds_b (tuple): Winning odds for teams a and b  

    '''
    try:
        # Fetch odds for Team A as winner and Team B as opponent
        odds_a = odds_df.loc[f"{team_a} (Winner)", f"{team_b} (Opponent)"]
    except KeyError:
        odds_a = None

    try:
        # Fetch odds for Team B as winner and Team A as opponent
        odds_b = odds_df.loc[f"{team_b} (Winner)", f"{team_a} (Opponent)"]
    except KeyError:
        odds_b = None

    return odds_a, odds_b


#----------------------------------------------------------------------------------------------------- #
# Load odds into excel 
#----------------------------------------------------------------------------------------------------- # 
file_path = 'bookmaker_odds.xlsx'
excel_data = pd.read_excel(file_path)

for index, row in excel_data.iterrows():
    team_a = row['Team A '].strip() if pd.notna(row['Team A ']) else None
    team_b = row['Team B '].strip() if pd.notna(row['Team B ']) else None

    if team_a and team_b:
        odds_a, odds_b = fetch_odds(team_a, team_b, team_analysis.best_of_three_lck_odds)
        excel_data.at[index, 'Calculated A'] = odds_a
        excel_data.at[index, 'Calculated B'] = odds_b

updated_file_path = 'updated_bookmaker_odds.xlsx'
excel_data.to_excel(updated_file_path, index=False)