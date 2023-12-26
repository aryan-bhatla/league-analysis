#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import pandas as pd 


#----------------------------------------------------------------------------------------------------- #
# Load results 
#----------------------------------------------------------------------------------------------------- # 
model_results = pd.read_csv('results.csv', index_col = 0)


#----------------------------------------------------------------------------------------------------- #
# Rating function 
#----------------------------------------------------------------------------------------------------- # 
def calc_player_rating(player: str, model_results: pd.DataFrame, final_data: pd.DataFrame, method = "coefficient") -> int: 
    '''
        
        Parameters: 
            player (str): Player to calculate rating for 
            model_results (pd.DataFrame): Calculated importance/co-efficient values 
            final_data (pd.DataFrame): Processed data
            method (str): Method used to calculate rating, defaults to "coefficient", alternatively "importance" can be used

        
        Returns: 
            rating (int): Final rating per player
    
    '''
    # Determine player role 
    try:
        player_role = final_data.loc[player, 'Pos']

    except KeyError:
        if method == "coefficient":
            return 3000
        elif method == "importance":
            return 25

    # Linear model
    if method == "coefficient": 
        coefficient_column = f"{player_role}_Avg_Coefficient"
        coefficient = model_results[coefficient_column] 

        # Filter final_data for columns present in the 'coefficient' Series
        filtered_final_data = final_data.loc[:, coefficient.index]

        # Multiply coefficients by stats 
        stat_ratings = filtered_final_data.loc[player].mul(coefficient)

    # Tree model 
    elif method == "importance": 
        importance_column = f"{player_role}_Avg_Importance"
        importance = model_results[importance_column]

        # Filter final_data for columns present in the 'importance' Series
        filtered_final_data = final_data.loc[:, importance.index]

        # Multiply importance values by stats 
        stat_ratings = filtered_final_data.loc[player].mul(importance)

    # Add all individual stats to get final rating
    rating = stat_ratings.sum()

    return rating