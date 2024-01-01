#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import math 

#----------------------------------------------------------------------------------------------------- # 
# Logistics function 
#----------------------------------------------------------------------------------------------------- # 
def rating_to_winrate(team_one: str, team_two: str, league_name: list[tuple[str, float]]) -> list:
    '''
        
        Parameters: 
            team_one, team_two (str): Teams playing against each other
            league_name (list): Pass in either lck_data, lcs_data or lec_data depending on which teams are being assessed

        Returns: 
            winrates (list): Predicted winrate for each team, should total 100% = 1

    '''
    # Sensitivity parameter affecting slope of curve
    beta = 0.011

    # Finding ratings for both teams
    for team, rating in league_name:
        if team == team_one:
            rating_one = rating
        elif team == team_two:
            rating_two = rating

    # Difference between ratings
    rating_delta = rating_one - rating_two 

    # Denominator for equation 
    denominator = 1 + math.exp(-beta*rating_delta) 

    # Final winrates 
    winrate_one = 1 / denominator
    winrate_two = 1 - winrate_one
    winrates = [winrate_one, winrate_two]

    return winrates 