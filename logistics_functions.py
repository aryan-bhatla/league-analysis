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
# Team Rating function 
#----------------------------------------------------------------------------------------------------- # 
def calculate_team_ratings(teams: dict, model_results: pd.DataFrame, final_data: pd.DataFrame, model_method: str, normalization_factor: float = None) -> list:
    '''

    Parameters:
        teams (dict): Dictionary containing teams' data
        model_results (pd.DataFrame): Calculated rf_importance/co-efficient/xg_importance values 
        final_data (pd.DataFrame): Processed data
        model_method (str): One of "rf_importance", "coefficient", "xg_importance
        normalization_factor (float): Factor to normalize team ratings, defaults to None, alternatively a float can be used

    Returns:
        team_ratings (list): List of total team ratings

    '''
    team_ratings = []

    for team_name, team_data in teams.items():
        player_ratings = []

        for player in team_data.values():

            # Calculate player rating using a specific method ("rf_importance" or "coefficient" or "xg_importance")
            ratings = calc_player_rating(player, model_results, final_data, model_method)
            player_ratings.append(ratings)

        total_team_rating = sum(player_ratings)

        # Normalize total team rating if a normalization factor is provided
        if normalization_factor:
            total_team_rating /= normalization_factor

        team_ratings.append(total_team_rating)

    return team_ratings


#----------------------------------------------------------------------------------------------------- # 
# Rating to win one game function 
#----------------------------------------------------------------------------------------------------- # 
def rating_to_best_of_one(team_one: str, team_two: str, league_data_dict: dict) -> list[float]:
    '''
        
        Parameters: 
            team_one, team_two (str): Teams playing against each other
            league_data_dict (dict): One of lck_data_dict, lcs_data_dict, lec_data_dict

        Returns: 
            best_of_one_winrates (list): Predicted winrate for each team, should total 100% = 1

    '''
    # There is 1C1 = 1 cases in total, with 1 possible scenarios -> 1 game 

    # Sensitivity parameter affecting slope of curve
    beta = 0.011

    # Delta parameter affecting importance of ratings
    delta_coefficient = 1.2 

    # Retrieve ratings directly from the dictionary
    rating_one = league_data_dict.get(team_one)
    rating_two = league_data_dict.get(team_two)

    # Check if both teams are the same
    if team_one == team_two:
        return [0.5, 0.5] 

    # Difference between ratings
    rating_delta = rating_one - rating_two 

    # Scale delta to place emphasize/de-emphasize rating discrepancy 
    scaled_delta = rating_delta * delta_coefficient

    # Denominator for equation 
    denominator = 1 + math.exp(-beta*scaled_delta) 

    # Final winrates 
    winrate_one = 1 / denominator
    winrate_two = 1 - winrate_one
    best_of_one_winrates = [winrate_one, winrate_two]

    return best_of_one_winrates 


#----------------------------------------------------------------------------------------------------- # 
# Rating to win two games function 
#----------------------------------------------------------------------------------------------------- # 
def rating_to_best_of_three(best_of_one_winrates: list[float]) -> list[float]:
    '''
        
        Parameters: 
            best_of_one_winrates (list): Predicted best of one game winrates for each team, should total 100% = 1

        Returns: 
            best_of_three_winrates (list): Predicted best of three game winrates for each team, should total 100% = 1

    '''
    # There are 3C2 = 3 cases in total, with 2 possible scenarios -> 2 games and 3 games  

    # Case 1: W - W for team one 
    scenario_one_winrate = best_of_one_winrates[0] * best_of_one_winrates[0]
    scenario_one_total = 1 * scenario_one_winrate 

    # Case 2: W - L - W for team one
    # Case 3: L - W - W for team one 
    scenario_two_winrate = best_of_one_winrates[0] * best_of_one_winrates[1] * best_of_one_winrates[0]
    scenario_two_total = 2 * scenario_two_winrate

    # Final winrates 
    winrate_one = scenario_one_total + scenario_two_total
    winrate_two = 1 - winrate_one
    best_of_three_winrates = [winrate_one, winrate_two]

    return best_of_three_winrates


#----------------------------------------------------------------------------------------------------- # 
# Rating to win three games function 
#----------------------------------------------------------------------------------------------------- # 
def rating_to_best_of_five(best_of_one_winrates: list[float]) -> list[float]:
    '''
        
        Parameters: 
            best_of_one_winrates (list): Predicted best of one game winrates for each team, should total 100% = 1

        Returns: 
            best_of_five_winrates (list): Predicted best of five game winrates for each team, should total 100% = 1

    '''
    # There are 5C3 = 10 cases in total, with 3 possible scenarios -> 3 games, 4 games and 5 games 

    # Case 1: W - W - W for team one 
    scenario_one_winrate = best_of_one_winrates[0] * best_of_one_winrates[0] * best_of_one_winrates[0]
    scenario_one_total = 1 * scenario_one_winrate

    # Case 2: W - W - L - W for team one 
    # Case 3: W - L - W - W for team one
    # Case 4: L - W - W - W for team one 
    scenario_two_winrate = best_of_one_winrates[0] * best_of_one_winrates[0] * best_of_one_winrates[1] * best_of_one_winrates[0]
    scenario_two_total = 3 * scenario_two_winrate

    # Case 5: W - W - L - L - W for team one
    # Case 6: W - L - L - W - W for team one 
    # Case 7: L - L - W - W - W for team one
    # Case 8: L - W - W - L - W for team one 
    # Case 9: W - L - W - L - W for team one
    # Case 10: L - W - L - W - W for team one 
    scenario_three_winrate = best_of_one_winrates[0] * best_of_one_winrates[0] * best_of_one_winrates[0] * best_of_one_winrates[1] * best_of_one_winrates[1] 
    scenario_three_total = 6 * scenario_three_winrate

    # Final winrates 
    winrate_one = scenario_one_total + scenario_two_total + scenario_three_total
    winrate_two = 1 - winrate_one
    best_of_five_winrates = [winrate_one, winrate_two]

    return best_of_five_winrates


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
    odds_one = 1 / team_one_winrate 
    odds_two = 1 / team_two_winrate
    odds = [odds_one, odds_two]

    return odds 


#----------------------------------------------------------------------------------------------------- # 
# Ratings tabulation function 
#----------------------------------------------------------------------------------------------------- # 
def ratings_table(league_teams: dict, team_ratings: list) -> pd.DataFrame:
    '''

    Parameters:
        league_teams (dict): One of LCK_teams, LCS_teams or LEC_teams
        team_ratings (list): List of all team ratings for certain league

    Returns:
        ratings_df (pd.DataFrame): DataFrame with team names and their ratings.
    '''
    # List of team names from the chosen league
    team_names = list(league_teams.keys())

    # Create a DataFrame from the team names and ratings
    ratings_df = pd.DataFrame(team_ratings, index = team_names, columns = ['Rating'])

    return ratings_df


#----------------------------------------------------------------------------------------------------- # 
# Winrate tabulation function 
#----------------------------------------------------------------------------------------------------- # 
def winrates_table(league_teams: dict, league_data_dict: dict, best_of_size: int) -> pd.DataFrame: 
    '''

        Parameters: 
            league_teams (dict): One of LCK_teams, LCS_teams or LEC_teams
            league_data_dict (dict): One of lck_data_dict, lcs_data_dict, lec_data_dict
            best_of_size (str): One of 1, 3, 5 
            
        Returns: 
            winrates (pd.DataFrame): Table containing pairwise winrates for each team in the league

    '''
    # List of team names from the chosen league
    team_names = list(league_teams.keys())

    # Initialize an empty DataFrame
    winrates_df = pd.DataFrame(index=[f"{team} (Winner)" for team in team_names],
                           columns=[f"{team} (Opponent)" for team in team_names])

    # Decide rating function dependent on game size
    rating_function = None
    if best_of_size == 1:
        rating_function = rating_to_best_of_one
    elif best_of_size == 3:
        rating_function = rating_to_best_of_three
    elif best_of_size == 5:
        rating_function = rating_to_best_of_five
    else:
        raise ValueError("Invalid best_of_size. Must be 1, 3, or 5.")

    for i in range(len(team_names)):
        for j in range(len(team_names)):
            i_team = team_names[i]
            j_team = team_names[j]

            # Calculate team winrates
            if rating_function == rating_to_best_of_one: 
                winrates = rating_function(i_team, j_team, league_data_dict)
            else: 
                winrates = rating_function(rating_to_best_of_one(i_team, j_team, league_data_dict))

            # Assign odds to DataFrame
            row_label = f"{i_team} (Winner)"
            col_label = f"{j_team} (Opponent)"
            winrates_df.at[row_label, col_label] = winrates[0]

    return winrates_df       


#----------------------------------------------------------------------------------------------------- # 
# Pairwise odds tabulation function 
#----------------------------------------------------------------------------------------------------- # 
def odds_table(league_teams: dict, league_data_dict: dict, best_of_size: int) -> pd.DataFrame: 
    '''

        Parameters: 
            league_teams (dict): One of LCK_teams, LCS_teams or LEC_teams
            league_data_dict (dict): One of lck_data_dict, lcs_data_dict, lec_data_dict
            best_of_size (str): One of 1, 3, 5
            
        Returns: 
            odds (pd.DataFrame): Table containing pairwise odds for each team in the league

    '''
    # List of team names from the chosen league
    team_names = list(league_teams.keys())

    # Initialize an empty DataFrame
    odds_df = pd.DataFrame(index=[f"{team} (Winner)" for team in team_names],
                           columns=[f"{team} (Opponent)" for team in team_names])

    # Decide rating function dependent on game size
    rating_function = None
    if best_of_size == 1:
        rating_function = rating_to_best_of_one
    elif best_of_size == 3:
        rating_function = rating_to_best_of_three
    elif best_of_size == 5:
        rating_function = rating_to_best_of_five
    else:
        raise ValueError("Invalid best_of_size. Must be 1, 3, or 5.")

    for i in range(len(team_names)):
        for j in range(len(team_names)):
            i_team = team_names[i]
            j_team = team_names[j]

            # Calculate team winrates
            if rating_function == rating_to_best_of_one: 
                winrates = rating_function(i_team, j_team, league_data_dict)
            else: 
                winrates = rating_function(rating_to_best_of_one(i_team, j_team, league_data_dict))

            # Calculate team odds
            odds = winrate_to_odds(winrates[0], winrates[1])

            # Assign odds to DataFrame
            row_label = f"{i_team} (Winner)"
            col_label = f"{j_team} (Opponent)"
            odds_df.at[row_label, col_label] = odds[0]

    return odds_df       


#----------------------------------------------------------------------------------------------------- # 
# Kelly bet function
#----------------------------------------------------------------------------------------------------- # 
def kelly_bet(calculated_win_prob: float, odds_your_team: float, odds_other_team: float) -> float: 
    '''
        
        Parameters: 
            calculated_win_prob (float): Winrate you have calculated for a team
            odds_your_team (float): Bookmaker odds for team you are betting on
            odds_other_team (float): Bookmaker odds for team you are not betting on
            
        Returns: 
            bet_size (float): Maximum bet size calculated via Kelly criterion 

    '''
    # Calculate win probability that bookmaker has determined 
    implied_win_prob = odds_your_team / (odds_your_team + odds_other_team) 

    # Set-up Kelly equation
    numerator = (odds_your_team * calculated_win_prob) - implied_win_prob 

    # Derive maximal bet size 
    bet_size = numerator / odds_your_team

    return bet_size 


