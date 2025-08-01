import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
import pickle

def get_training_data():
    """
    Returns the training data as a pandas dataframe
    :return: A dataframe containing the training data
    """
    data_2022 = pd.read_csv("formatted_data_2022.csv")
    data_2023 = pd.read_csv("formatted_data_2023.csv")
    data_2024 = pd.read_csv("formatted_data_2024.csv")
    data_2017 = pd.read_csv("formatted_data_2017.csv")
    data_2018 = pd.read_csv("formatted_data_2018.csv")
    data_2019 = pd.read_csv("formatted_data_2019.csv")

    full_data = pd.concat([data_2022, data_2023, data_2024, data_2019, data_2018, data_2017])
    y = full_data['score_diff']
    x = full_data.drop(columns=["score_diff", "Unnamed: 0"])
    return x, y


def train_model():
    """
    Handles the actual creation and training of the model; stores the model as a .pkl file
    :return: None
    """
    x, y = get_training_data()

    y_avg = y.mean()

    # dependent_descrip = x.describe()
    # dependent_descrip.to_csv("dependent_variables.csv")

    y_arr = np.array(y)
    x_arr = np.array(x)

    x_train, x_test, y_train, y_test = train_test_split(x_arr, y_arr, test_size=0.2, random_state=42)
    rf = RandomForestRegressor(n_estimators=1000, random_state=42)
    rf.fit(x_train, y_train)

    filename = "nfl_model.pkl"
    with open(filename, 'wb') as file:
        pickle.dump(rf, file)

    y_pred = rf.predict(x_test)

    # Calculate R^2 value
    r2 = r2_score(y_test, y_pred)
    print(f"The model has a r2 score of {r2}")

    # Calculate mean error
    errors = abs(y_pred - y_test)
    avg_error = np.mean(errors)
    print(f"The average error was {avg_error}")

    # Print baseline
    base_error = np.mean(abs(y_avg - y))
    print(f"This compares to a base error of {base_error}")

    feature_importance = list(rf.feature_importances_)
    features = list(x.columns)
    for i in range(0, len(feature_importance)):
        print(f"{features[i]}: {feature_importance[i]}")


if __name__ == "__main__":
    train_model()