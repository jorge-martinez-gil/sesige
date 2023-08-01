from sklearn.model_selection import train_test_split
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import scipy.stats
import pandas as pd
import numpy as np

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

raw_dataset = pd.read_csv(input_file2, skipinitialspace=True, delimiter=',', error_bad_lines=False) 
df = pd.read_csv(input_file2, skipinitialspace=True, usecols=categories2)
y = pd.DataFrame(raw_dataset, columns=['truth'])

X_test = df.to_numpy()
y_test = y.to_numpy()

reg = LinearRegression().fit(X_train, y_train)
y_pred = reg.predict(X_test)

df_preds = pd.DataFrame({'Actual': y_test.squeeze(), 'Predicted': y_pred.squeeze()})
print (df_preds)
print (my_pearson(y_test, y_pred))
print (my_spearman(y_test, y_pred))