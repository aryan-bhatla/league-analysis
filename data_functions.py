#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import pandas as pd 


#----------------------------------------------------------------------------------------------------- # 
# Data cleanup function
#----------------------------------------------------------------------------------------------------- # 
def cleanup_data(joined_data: pd.DataFrame) -> pd.DataFrame:
    '''
        
        Parameters: 
            joined_data (pd.DataFrame): Combined statistics from Spring Regular Season 2022 - Summer Playoffs 2023
        
        Returns: 
            replaced_data (pd.DataFrame): Cleaned statistics
    
    '''
    # Remove all '%' from columns
    removed_data = joined_data.replace('%', '', regex = True)
    
    # Convert all numerical strings to floats (4th column onwards)
    removed_data.iloc[:, 3:] = removed_data.iloc[:, 3:].astype(float)
    replaced_data = removed_data

    return replaced_data


#----------------------------------------------------------------------------------------------------- # 
# Data appending function
#----------------------------------------------------------------------------------------------------- # 
def append_data(replaced_data: pd.DataFrame) -> pd.DataFrame:
    '''
        
        Parameters: 
            replaced_data (pd.DataFrame): Cleaned statistics 
        
        Returns: 
            replaced_data (pd.DataFrame): Appended statistics with 'totals'
    
    '''
    # Multiply games played by other stats to get 'total' stats per season 
    replaced_data['Total GP'] = replaced_data['GP']
    replaced_data['Total W%'] = replaced_data['GP'] * replaced_data['W%']
    replaced_data['Total CTR%'] = replaced_data['GP'] * replaced_data['CTR%']
    replaced_data['Total K'] =  replaced_data['K']
    replaced_data['Total D'] = replaced_data['D']
    replaced_data['Total A'] = replaced_data['A']
    replaced_data['Total KDA'] = replaced_data['KDA']
    replaced_data['Total KP'] = replaced_data['GP'] * replaced_data['KP']
    replaced_data['Total KS%'] = replaced_data['GP'] * replaced_data['KS%']
    replaced_data['Total DTH%'] = replaced_data['GP'] * replaced_data['DTH%']
    replaced_data['Total FB%'] = replaced_data['GP'] * replaced_data['FB%']
    replaced_data['Total GD10'] = replaced_data['GP'] * replaced_data['GD10']
    replaced_data['Total XPD10'] = replaced_data['GP'] * replaced_data['XPD10']
    replaced_data['Total CSD10'] = replaced_data['GP'] * replaced_data['CSD10']
    replaced_data['Total GD10'] = replaced_data['GP'] * replaced_data['GD10']
    replaced_data['Total XPD10'] = replaced_data['GP'] * replaced_data['XPD10']
    replaced_data['Total CSPM'] = replaced_data['GP'] * replaced_data['CSPM']
    replaced_data['Total CS%P15'] = replaced_data['GP'] * replaced_data['CS%P15']
    replaced_data['Total DPM'] = replaced_data['GP'] * replaced_data['DPM']
    replaced_data['Total DMG%'] = replaced_data['GP'] * replaced_data['DMG%']
    replaced_data['Total D%P15'] = replaced_data['GP'] * replaced_data['D%P15']
    replaced_data['Total EGPM'] = replaced_data['GP'] * replaced_data['EGPM']
    replaced_data['Total GOLD%'] = replaced_data['GP'] * replaced_data['GOLD%']
    replaced_data['Total STL'] = replaced_data['STL']
    replaced_data['Total WPM'] = replaced_data['GP'] * replaced_data['WPM']
    replaced_data['Total CWPM'] = replaced_data['GP'] * replaced_data['CWPM']
    replaced_data['Total WCPM'] = replaced_data['GP'] * replaced_data['WCPM']

    return replaced_data


#----------------------------------------------------------------------------------------------------- # 
# Data summing function
#----------------------------------------------------------------------------------------------------- # 
def sum_data(replaced_data: pd.DataFrame) -> pd.DataFrame:
    '''
        
        Parameters: 
            replaced_data (pd.DataFrame): Appended statistics with 'totals'
        
        Returns: 
            indexed_data (pd.DataFrame): Summed and indexed statistics
    
    '''
    # Sum stats for duplicate players 
    aggregated_data = replaced_data.groupby('Player').agg({col: 'sum' for col in replaced_data.columns[28:]})
    non_aggregated_data = replaced_data.drop_duplicates(subset=['Player']).iloc[:, :28]
    merged_data = pd.merge(non_aggregated_data, aggregated_data, on = 'Player', how = 'left')

    # Sort players alphabetically
    sorted_data = merged_data.sort_values(by = 'Player', ascending = True)

    # Re-index with player names 
    indexed_data = sorted_data.set_index('Player')

    return indexed_data


#----------------------------------------------------------------------------------------------------- # 
# Data averaging function
#----------------------------------------------------------------------------------------------------- # 
def average_data(indexed_data: pd.DataFrame) -> pd.DataFrame:
    '''
        
        Parameters: 
            indexed_data (pd.DataFrame): Summed and indexed statistics
        
        Returns: 
            final_data (pd.DataFrame): Final averaged statistics 
    
    '''
    # Average out sums using total games played
    indexed_data['GP'] = indexed_data['Total GP']
    indexed_data['W%'] = indexed_data['Total W%'] / indexed_data['Total GP']
    indexed_data['CTR%'] = indexed_data['Total CTR%'] / indexed_data['Total GP']
    indexed_data['K'] =  indexed_data['Total K'] / indexed_data['Total GP']                # changed from total kills to kills per game 
    indexed_data['D'] = indexed_data['Total D'] / indexed_data['Total GP']                 # changed from total deaths to deaths per game 
    indexed_data['A'] = indexed_data['Total A'] / indexed_data['Total GP']                 # changed from total assists to assits per game 
    indexed_data['KDA'] = indexed_data['Total KDA'] / indexed_data['Total GP']             # changed from total KDA to KDA per game
    indexed_data['KP'] = indexed_data['Total KP'] / indexed_data['Total GP']
    indexed_data['KS%'] = indexed_data['Total KS%'] / indexed_data['Total GP']
    indexed_data['DTH%'] = indexed_data['Total DTH%'] / indexed_data['Total GP']
    indexed_data['FB%'] = indexed_data['Total FB%'] / indexed_data['Total GP']
    indexed_data['GD10'] = indexed_data['Total GD10'] / indexed_data['Total GP']
    indexed_data['XPD10'] = indexed_data['Total XPD10'] / indexed_data['Total GP']
    indexed_data['CSD10'] = indexed_data['Total CSD10'] / indexed_data['Total GP']
    indexed_data['GD10'] = indexed_data['Total GD10'] / indexed_data['Total GP']
    indexed_data['XPD10'] = indexed_data['Total XPD10'] / indexed_data['Total GP']
    indexed_data['CSPM'] = indexed_data['Total CSPM'] / indexed_data['Total GP']
    indexed_data['CS%P15'] = indexed_data['Total CS%P15'] / indexed_data['Total GP']
    indexed_data['DPM'] = indexed_data['Total DPM'] / indexed_data['Total GP']
    indexed_data['DMG%'] = indexed_data['Total DMG%'] / indexed_data['Total GP']
    indexed_data['D%P15'] = indexed_data['Total D%P15'] / indexed_data['Total GP']
    indexed_data['EGPM'] = indexed_data['Total EGPM'] / indexed_data['Total GP']
    indexed_data['GOLD%'] = indexed_data['Total GOLD%'] / indexed_data['Total GP']
    indexed_data['STL'] = indexed_data['Total STL'] / indexed_data['Total GP']             # changed from total steals to steals per game 
    indexed_data['WPM'] = indexed_data['Total WPM'] / indexed_data['Total GP']
    indexed_data['CWPM'] = indexed_data['Total CWPM'] / indexed_data['Total GP']
    indexed_data['WCPM'] = indexed_data['Total WCPM'] / indexed_data['Total GP']

    averaged_data = indexed_data 
    
    # Drop initially appended 'total' columns 
    columns_to_drop = averaged_data.columns[27:52]
    dropped_data = averaged_data.drop(columns = columns_to_drop)

    final_data = dropped_data

    return final_data