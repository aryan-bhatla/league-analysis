#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import streamlit as st

from team_construction import calculate_team_ratings, LCK_teams, LCS_teams, LEC_teams


#----------------------------------------------------------------------------------------------------- # 
# App main
#----------------------------------------------------------------------------------------------------- # 
# Streamlit title
st.title('Team Ratings')

# Decide normalisation
LCS_normalisation = 1.25
LEC_normalisation = 1.15
LCK_normalisation = 1.0

# Calculate team ratings
lck_team_ratings = calculate_team_ratings(LCK_teams, LCK_normalisation)
lcs_team_ratings = calculate_team_ratings(LCS_teams, LCS_normalisation)
lec_team_ratings = calculate_team_ratings(LEC_teams, LEC_normalisation)

# Function to display data
def display_data(teams, ratings, league_name):
    st.subheader(f'{league_name} Teams and Ratings')
    for team, rating in zip(teams, ratings):
        st.write(f"{team}: {rating}")

# Display data for each league
display_data(LCK_teams, lck_team_ratings, 'LCK')
display_data(LCS_teams, lcs_team_ratings, 'LCS')
display_data(LEC_teams, lec_team_ratings, 'LEC')