#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import numpy as np 
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from xgboost import XGBRegressor


#----------------------------------------------------------------------------------------------------- # 
# Random forest 
#----------------------------------------------------------------------------------------------------- # 
def perform_random_forest(data: pd.DataFrame, seed: int) -> tuple[float, float, float]:
    '''
        
        Parameters: 
            data (pd.DataFrame): Statistics for different roles (Support, ADC, Middle, Jungle, Top)
        
        Returns: 
            np.mean(r2_scores) (float): Mean R^2 over K folds 
            np.mean(mse_scores) (float): Mean MSE over K folds 
            feature_importances (float): Importance of each independent variable relative to each other 
    
    '''
    # Split data into dependent and independent variables
    X = data.drop(['Team', 'Pos', 'GP', 'W%', 'KDA', 'STL'], axis = 1)                   # indepdendent variables = other statistics
    y = data['W%']                                                                       # dependent variable = winrate 
    weights = data['GP']                                                                 # weigh each row depending on number of games played   

    # K-fold validation setup
    k = 10
    kf = KFold(n_splits = k, shuffle = True, random_state = 42)

    # Model initialization
    rf_model = RandomForestRegressor(n_estimators = 100, random_state = seed)

    # Metrics initialization
    r2_scores = []
    mse_scores = []

    # K-Fold validation loop
    for train_index, test_index in tqdm(kf.split(X), total = k, desc = "RF KFold Progress"):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        weights_train = weights.iloc[train_index]

        # Fit the model
        rf_model.fit(X_train, y_train, sample_weight = weights_train)

        # Predict and evaluate
        y_pred = rf_model.predict(X_test)
        r2_scores.append(r2_score(y_test, y_pred))
        mse_scores.append(mean_squared_error(y_test, y_pred))

    # Feature importance
    feature_importances = pd.DataFrame(rf_model.feature_importances_, index = X_train.columns, columns = ['rf_Importance']).sort_values('rf_Importance', ascending = False)
    print(np.mean(r2_scores))
    return np.mean(r2_scores), np.mean(mse_scores), feature_importances


#----------------------------------------------------------------------------------------------------- # 
# Linear regression
#----------------------------------------------------------------------------------------------------- # 
# Split data into dependent and independent variables 
def perform_linear_regression(data: pd.DataFrame, seed: int) -> tuple[float, float, float]:
    '''
        
        Parameters: 
            data (pd.DataFrame): Statistics for different roles (Support, ADC, Middle, Jungle, Top)
        
        Returns: 
            np.mean(r2_scores) (float): Mean R^2 over K folds 
            np.mean(mse_scores) (float): Mean MSE over K folds 
            coefficients (float): Importance of each independent variable relative to each other 
    
    '''
    # Split data into dependent and independent variables
    X = data.drop(['Team', 'Pos', 'GP', 'W%', 'KDA', 'STL'], axis = 1)                   # indepdendent variables = other statistics
    y = data['W%']                                                                       # dependent variable = winrate 
    weights = data['GP']                                                                 # weigh each row depending on number of games played

    # K-fold validation setup
    k = 10
    kf = KFold(n_splits = k, shuffle = True, random_state = seed)

    # Model and scaler initialization
    lr_model = LinearRegression()
    scaler = StandardScaler()

    # Metrics initialization
    r2_scores = []
    mse_scores = []

    # K-Fold validation loop
    for train_index, test_index in tqdm(kf.split(X), total = k, desc = "LR KFold Progress"):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        weights_train = weights.iloc[train_index]

        # Apply scaling
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Fit the model
        lr_model.fit(X_train_scaled, y_train, sample_weight = weights_train)

        # Predict and evaluate
        y_pred = lr_model.predict(X_test_scaled)
        r2_scores.append(r2_score(y_test, y_pred))
        mse_scores.append(mean_squared_error(y_test, y_pred))

    # Coefficients
    coefficients = pd.DataFrame(lr_model.coef_, X_train.columns, columns = ['Coefficient'])
    return np.mean(r2_scores), np.mean(mse_scores), coefficients


#----------------------------------------------------------------------------------------------------- # 
# xgboost 
#----------------------------------------------------------------------------------------------------- # 
def perform_xgboost(data: pd.DataFrame, seed: int) -> tuple[float, float, float]:
    '''
        
        Parameters: 
            data (pd.DataFrame): Statistics for different roles (Support, ADC, Middle, Jungle, Top)
        
        Returns: 
            np.mean(r2_scores) (float): Mean R^2 over K folds 
            np.mean(mse_scores) (float): Mean MSE over K folds 
            xg_feature_importances (float): Importance of each independent variable relative to each other 
    
    '''
    # Split data into dependent and independent variables
    X = data.drop(['Team', 'Pos', 'GP', 'W%', 'KDA', 'STL'], axis = 1)                   # indepdendent variables = other statistics
    y = data['W%']                                                                # dependent variable = winrate 
    weights = data['GP']                                                          # weigh each row depending on number of games played   

    # K-fold validation setup
    k = 10
    kf = KFold(n_splits = k, shuffle = True, random_state = 42)

    # Model initialization
    xg_model = XGBRegressor(n_estimators = 100, random_state = seed)

    # Metrics initialization
    r2_scores = []
    mse_scores = []

    # K-Fold validation loop
    for train_index, test_index in tqdm(kf.split(X), total = k, desc = "xgboost KFold Progress"):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        weights_train = weights.iloc[train_index]

        # Fit the model
        xg_model.fit(X_train, y_train, sample_weight = weights_train)

        # Predict and evaluate
        y_pred = xg_model.predict(X_test)
        r2_scores.append(r2_score(y_test, y_pred))
        mse_scores.append(mean_squared_error(y_test, y_pred))

    # Feature importance
    xg_feature_importances = pd.DataFrame(xg_model.feature_importances_, index = X_train.columns, columns = ['xg_Importance']).sort_values('xg_Importance', ascending = False)
    return np.mean(r2_scores), np.mean(mse_scores), xg_feature_importances