import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
import pickle

def get_training_data():
    data_2022 = pd.read_csv("formatted_data_2022.csv")
    data_2023 = pd.read_csv("formatted_data_2023.csv")
    data_2024 = pd.read_csv("formatted_data_2024.csv")

    full_data = pd.concat([data_2022, data_2023, data_2024])
    y = full_data['score_diff']
    x = full_data.drop(columns=["score_diff", "Unnamed: 0"])
    return x, y


def train_model():
    x, y = get_training_data()
    feature_names = x.columns
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    rf = RandomForestRegressor()
    rf.fit(x_train, y_train)

    filename = "nfl_model.pkl"
    with open(filename, 'wb') as file:
        pickle.dump(rf, file)
    
    y_pred = rf.predict(x_test)

    accuracy = r2_score(y_test, y_pred)
    print(f"The model has a r2 score of {accuracy}")

    result = permutation_importance(
        rf, x_test, y_test, n_repeats=10, random_state=42, n_jobs=2
    )
    forest_importances = pd.Series(result.importances_mean, index=feature_names)
    fig, ax = plt.subplots()
    forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
    ax.set_title("Feature importances using permutation on full model")
    ax.set_ylabel("Mean accuracy decrease")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    train_model()