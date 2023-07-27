from gplearn.genetic import SymbolicRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.utils.random import check_random_state
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats

def my_pearson(x, y):
    a = x.flatten()
    b = y.flatten()
    return -1*np.corrcoef(a, b)[0, 1]
    
def my_spearman(x, y):
    a = x.flatten()
    b = y.flatten()
    rho, p = scipy.stats.spearmanr(x, y)
    return -1*rho
    
input_file = "mc2.txt"
input_file2 = "mc.txt"

categories = ['b', 'c', 'd', 'e', 'f']
categories2 = ['bert-cos', 'bert-inn', 'bert-man', 'bert-euc', 'bert-ang']

raw_dataset = pd.read_csv(input_file, error_bad_lines=False) 
df = pd.read_csv(input_file, skipinitialspace=True, usecols=categories)
y = pd.DataFrame(raw_dataset, columns=['a']) 

X_train = df.to_numpy()
y_train = y.to_numpy()

raw_dataset = pd.read_csv(input_file2, error_bad_lines=False) 
df = pd.read_csv(input_file2, skipinitialspace=True, usecols=categories2)
y = pd.DataFrame(raw_dataset, columns=['truth']) 

X_test = df.to_numpy()
y_test = y.to_numpy()

# Define the parameter grid to search over
param_grid = {
    'population_size': [5000, 8000, 10000],
    'metric': ['pearson', 'spearman'],
    'generations': [5000, 9000, 10000],
    'stopping_criteria': [0.01, 0.05, 0.1],
    'p_crossover': [0.5, 0.75, 0.9],
    'p_subtree_mutation': [0.05, 0.1, 0.2],
    'p_hoist_mutation': [0.01, 0.05, 0.1],
    'p_point_mutation': [0.05, 0.1, 0.2],
    'max_samples': [0.5, 0.9, 1.0],
    'parsimony_coefficient': [0.001, 0.01, 0.1],
    'random_state': [0, 42, 123]
}

# Create a SymbolicRegressor object
est_gp = SymbolicRegressor()

# Create a GridSearchCV object
grid_search = GridSearchCV(est_gp, param_grid=param_grid, cv=5, n_jobs=-1)

# Fit the GridSearchCV object to the data
grid_search.fit(X_train, y_train)

# Print the best parameters and score
print("Best parameters: ", grid_search.best_params_)
print("Best score: ", grid_search.best_score_)

# Create a new SymbolicRegressor object with the best parameters
best_gp = SymbolicRegressor(**grid_search.best_params_)

# Fit the new SymbolicRegressor object to the data
best_gp.fit(X_train, y_train)

# Predict the target values for the test data
y_pred = best_gp.predict(X_test)

# Print the predicted and actual target values
df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)

# Print the Pearson correlation coefficient between the predicted and actual target values
print("Pearson correlation coefficient: ", my_pearson(y_test, y_pred))

# Print the Spearman correlation coefficient between the predicted and actual target values
print("Spearman correlation coefficient: ", my_spearman(y_test, y_pred))