#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
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