from gplearn.genetic import SymbolicRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.utils.random import check_random_state
import matplotlib.pyplot as plt
import numpy as np
import graphviz
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
    
input_file = "mc-training2.txt"
input_file2 = "mc-validation.txt"

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

# Define the hyperparameter grid for grid search
param_grid = {
    'population_size': [100, 500, 1000],
    'generations': [5000, 9000, 12000],
    'stopping_criteria': [0.01, 0.001],
    'p_crossover': [0.75, 0.9],
    'p_subtree_mutation': [0.1, 0.2],
    'p_hoist_mutation': [0.05, 0.1],
    'p_point_mutation': [0.1, 0.2],
    'max_samples': [0.9, 0.95],
    'parsimony_coefficient': [0.01, 0.001]
}

# Create the SymbolicRegressor instance
est_gp = SymbolicRegressor(metric='pearson', random_state=0)

# Create the GridSearchCV instance
grid_search = GridSearchCV(estimator=est_gp, param_grid=param_grid, cv=5, verbose=2, n_jobs=-1)

# Fit the grid search on the training data
grid_search.fit(X_train, y_train)

# Get the best estimator after grid search
best_estimator = grid_search.best_estimator_

# Print the best hyperparameters
print("Best Hyperparameters:")
print(grid_search.best_params_)

# Train the best estimator on the entire training data
best_estimator.fit(X_train, y_train)

# Predict on the test data using the best estimator
y_pred = best_estimator.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print(df_preds)
print("Pearson Correlation:", my_pearson(y_test, y_pred))
#print("Spearman Correlation:", my_spearman(y_test, y_pred))