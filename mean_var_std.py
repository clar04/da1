import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3, 3)
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  
            matrix.mean(axis=1).tolist(),  
            matrix.mean().item()          
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # variance of columns
            matrix.var(axis=1).tolist(),   # variance of rows
            matrix.var().item()            # variance of flattened matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # std dev of columns
            matrix.std(axis=1).tolist(),   # std dev of rows
            matrix.std().item()            # std dev of flattened matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # max of columns
            matrix.max(axis=1).tolist(),   # max of rows
            matrix.max().item()            # max of flattened matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # min of columns
            matrix.min(axis=1).tolist(),   # min of rows
            matrix.min().item()            # min of flattened matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # sum of columns
            matrix.sum(axis=1).tolist(),   # sum of rows
            matrix.sum().item()            # sum of flattened matrix
        ]
    }
    
    return calculations