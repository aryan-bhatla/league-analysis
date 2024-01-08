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
def display_winrates(league_winrates: pd.DataFrame, league_name: str):
    '''
        
        Parameters: 
            league_odds (pd.DataFrame): One of lck_winrates, lcs_winrates, lec_winrates
            league_name (str): One of LCK, LCS, LEC 

    '''
    st.subheader(f'{league_name} Teams and Winrates using Calculated Ratings')
    st.write(league_winrates)


#----------------------------------------------------------------------------------------------------- # 
# Odds display function
#----------------------------------------------------------------------------------------------------- # 
def display_odds(league_odds: pd.DataFrame, league_name: str):
    '''
        
        Parameters: 
            league_odds (pd.DataFrame): One of lck_odds, lcs_odds, lec_odds
            league_name (str): One of LCK, LCS, LEC 

    '''
    st.subheader(f'{league_name} Teams and Odds using Calculated Winrates')
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
display_winrates(team_analysis.lck_winrates, 'LCK')
display_winrates(team_analysis.lcs_winrates, 'LCS')
display_winrates(team_analysis.lec_winrates, 'LEC')

# Odds for each league
display_odds(team_analysis.lck_odds, 'LCK')
display_odds(team_analysis.lcs_odds, 'LCS')
display_odds(team_analysis.lec_odds, 'LEC')