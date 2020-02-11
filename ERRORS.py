import numpy as np
"""
    The implementation of the following is included:
    
    1. Root mean square
    2. Mean absolute procentage error
    3. Correlation coefficient
    4. Mean absolute error
    
    The equation for these can be found in:
    A systematic review of fundamental and technical analysis of stock market predictions
"""

"""
    Root mean squared error (RMSE): This performance index will show an estimation of
    the residual between the actual (t_i) value and predicted value (y_i) 
"""
def RMS(t,y):
    arr_len = len(t)
    # Now we want to subtract each element in t and y and list them
    forecast_errors = [t[i]-y[i] for i in range(arr_len)]
    RMS = np.sqrt(1/(arr_len)) * forecast_errors
    return RMS

"""
    The next performance metric is the mean absolute percentage error (MAPE):
    this metric is an indicator of an average absolute percentage error;
    lower MAPE is better than higher MAPE.
"""
def MAPE(t,y):
    arr_len = len(t)
    forecast_errors = [abs((t[i]-y[i])/t[i]) for i in range(arr_len)]
    MAPE = 1/arr_len * forecast_errors
    return MAPE

"""
    This index measures the average magnitude of the errors in a set of predictions,
    without considering their direction
"""
def MAE(t,y):
    arr_len = len(t)
    forecast_errors = [t[i]-y[i] for i in range(arr_len)]
    MAE = np.multiply(1/arr_len,forecast_errors)
    return MAE

"""
    The correlation coefficient (R): performance index unveils the degree of associations
    between predicted values and actual values, it ranges from 0 to 1, and the bigger the
    Correlation coefficient, the better model performance.
"""
def R(t,y):
    mean_t,mean_y,len_arr = np.mean(t), np.mean(y), len(t)
    nume,deno = [],[]
    for i in range(len_arr):
        nume.append((t[i]-mean_t) * (y[i]-mean_y))
        deno.append(pow((t[i]-mean_t),2) * pow(y[i-mean_y],2))
    nume,deno = np.sum(nume),np.sum(np.sqrt(deno))
    return nume/deno




















