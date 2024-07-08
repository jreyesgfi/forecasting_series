import numpy as np

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(
        np.absolute(
            np.subtract(y_true, y_pred)
        )
    ) *100

if __name__ == '__main__':
    y_true = [0,1,2]
    y_pred = [2,3,2]
    print(mean_absolute_percentage_error(y_true, y_pred))