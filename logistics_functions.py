#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import math 
import pandas as pd


#----------------------------------------------------------------------------------------------------- #
# Player Rating function 
#----------------------------------------------------------------------------------------------------- # 
def calc_player_rating(player: str, model_results: pd.DataFrame, final_data: pd.DataFrame, method: str = "coefficient") -> int: 
    '''
        
        Parameters: 
            player (str): Player to calculate rating for 
            model_results (pd.DataFrame): Calculated rf_importance/co-efficient/xg_importance values 
            final_data (pd.DataFrame): Processed data
            method (str): Method used to calculate rating, defaults to "coefficient", alternatively "rf_importance" or "xg_importance" can be used

        
        Returns: 
            rating (int): Final rating per player
    
    '''
    # Determine player role 
    try:
        player_role = final_data.loc[player, 'Pos']

    except KeyError:
        if method == "coefficient":
            return 3000
        elif method == "rf_importance" or method == "xg_importance":
            return 25

    # Linear model
    if method == "coefficient": 
        coefficient_column = f"{player_role}_Avg_Coefficient"
        coefficient = model_results[coefficient_column] 

        # Filter final_data for columns present in the 'coefficient' series
        filtered_final_data = final_data.loc[:, coefficient.index]

        # Multiply coefficients by stats 
        stat_ratings = filtered_final_data.loc[player].mul(coefficient)

    # Tree model 
    elif method == "rf_importance": 
        rf_importance_column = f"{player_role}_Avg_rf_Importance"
        rf_importance = model_results[rf_importance_column]

        # Filter final_data for columns present in the 'rf_importance' series
        filtered_final_data = final_data.loc[:, rf_importance.index]

        # Multiply importance values by stats 
        stat_ratings = filtered_final_data.loc[player].mul(rf_importance)

    # xgboost model 
    elif method == "xg_importance":  
        xg_importance_column = f"{player_role}_Avg_xg_Importance"
        xg_importance = model_results[xg_importance_column]

        # Filter final_data for columns present in the 'xg_importance' series
        filtered_final_data = final_data.loc[:, xg_importance.index]

        # Multiply importance values by stats 
        stat_ratings = filtered_final_data.loc[player].mul(xg_importance)

    # Add all individual stats to get final rating
    rating = stat_ratings.sum()

    return rating


#----------------------------------------------------------------------------------------------------- # 
# Rating to winrate function 
#----------------------------------------------------------------------------------------------------- # 
def rating_to_winrate(team_one: str, team_two: str, league_name: list[tuple[str, float]]) -> list[float]:
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


#----------------------------------------------------------------------------------------------------- # 
# Winrate to odds function 
#----------------------------------------------------------------------------------------------------- # 
def winrate_to_odds(team_one_winrate: float, team_two_winrate: float) -> list[float]:
    '''
        
        Parameters: 
            team_one_winrate, team_two_winrate (float): Team winrates against each other, should total 100% = 1

        Returns: 
            odds (list): Implied odds for each team based on their winrates

    '''
    # Final odds 
    odds_one = 100 / team_one_winrate 
    odds_two = 100 / team_two_winrate
    odds = [odds_one, odds_two]

    return odds 
