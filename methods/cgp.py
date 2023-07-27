import pandas as pd
from sklearn.model_selection import train_test_split
import scipy.stats
import numpy as np
import tengp
from sklearn.model_selection import ParameterGrid

# Load data
input_file = "geresid-training.txt"
input_file2 = "geresid-validation.txt"

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

# Set up CGP system
def protected_division(x, y):
    return np.divide(x, y, out=np.copy(x), where=y!=0)
   
def my_pearson(x, y):
    a = x.flatten()
    b = y.flatten()
    return -1*np.corrcoef(a, b)[0, 1]
    
def my_spearman(x, y):
    a = x.flatten()
    b = y.flatten()
    rho, p = scipy.stats.spearmanr(x, y)
    return -1*rho

funset = tengp.FunctionSet()
funset.add(np.add, 2)
funset.add(np.subtract, 2)
funset.add(np.multiply, 2)
funset.add(protected_division, 2)
funset.add(np.sin, 1)
funset.add(np.cos, 1)

# Define hyperparameters to search over
hyperparameters = {
    'n_columns': [50, 100, 150, 200, 250],
    'n_rows': [1, 2, 3, 4]
}

# Create ParameterGrid object
param_grid = ParameterGrid(hyperparameters)

# Initialize variables to store best hyperparameters and fitness
best_params = None
best_fitness = float('-inf')

# Loop over each set of hyperparameters
for params_dict in param_grid:
    # Create new params object with current hyperparameters
    params = tengp.Parameters(n_inputs=X_train.shape[1],
                              n_outputs=1,
                              function_set=funset,
                              n_columns=params_dict['n_columns'],
                              n_rows=params_dict['n_rows'])
    # Run evolution using new params object
    res = tengp.simple_es(X_train,
                          y_train,
                          my_pearson,
                          params,
                          mutation='probabilistic',
                          verbose=100)
    # Record fitness of best individual
    fitness = res[0].fitness
    if fitness > best_fitness:
        best_fitness = fitness
        best_params = params_dict

# Print best hyperparameters and fitness
print('Best hyperparameters:', best_params)
print('Best fitness:', best_fitness)

# Run evolution with best hyperparameters
params = tengp.Parameters(n_inputs=X_train.shape[1],
                          n_outputs=1,
                          function_set=funset,
                          **best_params)
res = tengp.simple_es(X_train,
                      y_train,
                      my_pearson,
                      params,
                      mutation='probabilistic',
                      verbose=100)

# Print fitness and phenotype of best individual
print(res[0].fitness)
print(res[0].get_expression())

y_pred = res[0].transform(X_test)
print(my_pearson(y_test, y_pred))
#print(my_spearman(y_test, y_pred))