import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Lasso

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import pickle
import matplotlib.pyplot as plt


def get_training_data():
    """
    Returns the training data as a pandas dataframe
    :return: A dataframe containing the training data
    """
    data_2022 = pd.read_csv("training_data_2022.csv")
    data_2023 = pd.read_csv("training_data_2023.csv")
    data_2024 = pd.read_csv("training_data_2024.csv")
    full_data = pd.concat([data_2022, data_2023, data_2024])

    columns_to_drop = ["avg_receptions", "avg_targets", "avg_receiving_yards", "avg_receiving_tds",
                       "avg_receiving_first_downs", "pst_fg_missed_0_19", "avg_completions", "avg_attempts",
                       "avg_passing_first_downs", "avg_sack_yards_lost", "avg_rushing_first_downs", "avg_carries",
                       "pst_receptions", "pst_targets", "pst_receiving_yards", "pst_receiving_tds",
                       "pst_receiving_first_downs", "pst_fg_missed_0_19", "pst_completions", "pst_attempts",
                       "pst_passing_first_downs", "pst_sack_yards_lost", "pst_rushing_first_downs",
                       "pst_carries", "avg_fumble_recovery_yards_opp", "pst_fumble_recovery_yards_opp",
                       "avg_fumble_recovery_yards_own", "pst_fumble_recovery_yards_own", "avg_penalty_yards",
                       "pst_penalty_yards", "avg_def_sack_yards", "pst_def_sack_yards",
                       "avg_def_tackles_for_loss_yards", "pst_def_tackles_for_loss_yards", "avg_receiving_epa",
                       "pst_receiving_epa", "avg_receiving_2pt_conversions", "pst_receiving_2pt_conversions",
                       "avg_passing_yards_after_catch", "pst_passing_yards_after_catch", "avg_receiving_yards_after_catch",
                       "pst_receiving_yards_after_catch", "avg_receiving_air_yards", "pst_receiving_air_yards",
                       "avg_kickoff_return_yards", "pst_kickoff_return_yards", "pst_fg_made_distance", "avg_fg_made_distance",
                       "avg_fg_att", "pst_fg_att", "avg_fg_missed_distance", "pst_fg_missed_distance", "avg_fg_blocked_distance",
                       "pst_fg_blocked_distance", "pst_pat_att", "avg_pat_att", "pst_gwfg_att", "avg_fg_long", "avg_fg_pct",
                       "avg_pat_pct"]
    full_data = full_data.drop(columns=columns_to_drop)
    # full_data.to_csv("full_data.csv", index=False)
    print(len(full_data))
    y = full_data['score_diff']
    x = full_data.drop(columns=["score_diff"])
    return x, y


def train_model():
    """
    Handles the actual creation and training of the model; stores the model as a .pkl file
    :return: None
    """
    x, y = get_training_data()

    # x.corr(method="pearson").to_csv("correlations.csv")

    y_avg = y.mean()

    # dependent_descrip = x.describe()
    # dependent_descrip.to_csv("dependent_variables.csv")

    y_arr = np.array(y)
    x_arr = np.array(x)

    indexes = np.array(range(len(y_arr)))
    plt.scatter(x=indexes, y=y_arr)

    x_train, x_test, y_train, y_test = train_test_split(x_arr, y_arr, test_size=0.2, random_state=42)
    rf = RandomForestRegressor(random_state=42)
    lr = LinearRegression()
    lasso = Lasso(alpha=0.2)
    rf.fit(x_train, y_train)
    lr.fit(x_train, y_train)
    lasso.fit(x_train, y_train)

    filename = "nfl_model.pkl"
    with open(filename, 'wb') as file:
        pickle.dump(rf, file)

    y_pred = rf.predict(x_test)
    lr_pred = lr.predict(x_test)
    lasso_pred = lasso.predict(x_test)

    # Calculate R^2 training values?
    yt_pred = rf.predict(x_train)
    r2t_rf = r2_score(y_train, yt_pred)

    lrt_pred = lr.predict(x_train)
    r2t_lr = r2_score(y_train, lrt_pred)

    lassot_pred = lasso.predict(x_train)
    r2t_lasso = r2_score(y_train, lassot_pred)

    print(f"The model has a training r2 score of {r2t_rf}")
    print(f"The LR model has a training r2 score of {r2t_lr}")
    print(f"The lasso model has a training r2 score of {r2t_lasso}")

    # Calculate R^2 value
    r2 = r2_score(y_test, y_pred)
    r2_lr = r2_score(y_test, lr_pred)
    r2_lasso = r2_score(y_test, lasso_pred)
    print(f"The model has a r2 score of {r2}")
    print(f"The LR model has a r2 score of {r2_lr}")
    print(f"The lasso model has a r2 score of {r2_lasso}")

    # Calculate mean error
    errors = abs(y_pred - y_test)
    lr_errors = np.mean(abs(lr_pred - y_test))
    lasso_errors = np.mean(abs(lasso_pred- y_test))
    avg_error = np.mean(errors)
    print(f"The average error was {avg_error}")
    print(f"The LR average error was {lr_errors}")
    print(f"The lasso average error was {lasso_errors}")

    # Print baseline
    base_error = np.mean(abs(y_avg - y))
    print(f"This compares to a base error of {base_error}")

    feature_importance = list(rf.feature_importances_)
    features = list(x.columns)
    imp_sorted = {}
    for i in range(0, len(feature_importance)):
        imp_sorted[feature_importance[i]] = features[i]

    results = list(imp_sorted.keys())
    results.sort()
    for r in results:
        print(f"{imp_sorted[r]} - {r}")

    mse = mean_squared_error(y_test, y_pred)
    print(f"The mean squared error equals {mse} for the model")

    lr_mse = mean_squared_error(y_test, lr_pred)
    print(f"This compares to a MSE for the LR model of {lr_mse}")

    lasso_mse = mean_squared_error(y_test, lasso_pred)
    print(f"And the lasso's MSE of {lasso_mse}")


if __name__ == "__main__":
    train_model()
