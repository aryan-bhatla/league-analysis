#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import pandas as pd
import streamlit as st
import team_analysis


#----------------------------------------------------------------------------------------------------- # 
# Ratings display function
#----------------------------------------------------------------------------------------------------- # 
def display_ratings(league_ratings: pd.DataFrame, league_name: str):
    '''
        
        Parameters: 
            league_ratings (pd.DataFrame): One of lck_ratings, lcs_ratings, lec_ratings
            league_name (str): One of LCK, LCS, LEC

    '''
    if team_analysis.model_method == "rf_importance": 
        st.subheader(f'{league_name} Teams and Ratings using Random Forest Modelling')
    
    elif team_analysis.model_method == "xg_importance": 
        st.subheader(f'{league_name} Teams and Ratings using XGBoost Modelling')

    elif team_analysis.model_method == "coefficient": 
        st.subheader(f'{league_name} Teams and Ratings using Linear Regression Modelling')

    st.write(league_ratings)


#----------------------------------------------------------------------------------------------------- # 
# Winrates display function
#----------------------------------------------------------------------------------------------------- # 
def display_winrates(league_winrates: pd.DataFrame, league_name: str, best_of_size: int):
    '''
        
        Parameters: 
            league_odds (pd.DataFrame): One of lck_winrates, lcs_winrates, lec_winrates
            league_name (str): One of LCK, LCS, LEC 
            best_of_size (int): One of 1, 3, 5

    '''
    st.subheader(f'{league_name} Best of {best_of_size} Winrates using Calculated Ratings')
    st.write(league_winrates)


#----------------------------------------------------------------------------------------------------- # 
# Odds display function
#----------------------------------------------------------------------------------------------------- # 
def display_odds(league_odds: pd.DataFrame, league_name: str, best_of_size: int):
    '''
        
        Parameters: 
            league_odds (pd.DataFrame): One of lck_odds, lcs_odds, lec_odds
            league_name (str): One of LCK, LCS, LEC 
            best_of_size (int): One of 1, 3, 5

    '''
    st.subheader(f'{league_name} Best of {best_of_size} Odds using Calculated Winrates')
    st.write(league_odds)


#----------------------------------------------------------------------------------------------------- # 
# App main
#----------------------------------------------------------------------------------------------------- # 
# Title
st.title('Team Analysis')

# Ratings for each league
display_ratings(team_analysis.lck_ratings, 'LCK')
display_ratings(team_analysis.lcs_ratings, 'LCS')
display_ratings(team_analysis.lec_ratings, 'LEC')

# Winrates for each league
display_winrates(team_analysis.best_of_one_lck_winrates, 'LCK', 1)
display_winrates(team_analysis.best_of_one_lcs_winrates, 'LCS', 1)
display_winrates(team_analysis.best_of_one_lec_winrates, 'LEC', 1)

display_winrates(team_analysis.best_of_three_lck_winrates, 'LCK', 3)
display_winrates(team_analysis.best_of_three_lcs_winrates, 'LCS', 3)
display_winrates(team_analysis.best_of_three_lec_winrates, 'LEC', 3)

display_winrates(team_analysis.best_of_five_lck_winrates, 'LCK', 5)
display_winrates(team_analysis.best_of_five_lcs_winrates, 'LCS', 5)
display_winrates(team_analysis.best_of_five_lec_winrates, 'LEC', 5)

# Odds for each league
display_odds(team_analysis.best_of_one_lck_odds, 'LCK', 1)
display_odds(team_analysis.best_of_one_lcs_odds, 'LCS', 1)
display_odds(team_analysis.best_of_one_lec_odds, 'LEC', 1)

display_odds(team_analysis.best_of_three_lck_odds, 'LCK', 3)
display_odds(team_analysis.best_of_three_lcs_odds, 'LCS', 3)
display_odds(team_analysis.best_of_three_lec_odds, 'LEC', 3)

display_odds(team_analysis.best_of_five_lck_odds, 'LCK', 5)
display_odds(team_analysis.best_of_five_lcs_odds, 'LCS', 5)
display_odds(team_analysis.best_of_five_lec_odds, 'LEC', 5)