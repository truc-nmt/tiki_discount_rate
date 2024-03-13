import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score, f1_score, recall_score, precision_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor


from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass 
class ModelTrainerConfig:
    train_model_file_path = os.path.join("models", "model.pkl")


class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()


    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=True),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            # Fine-tune Hyper Parameter
            params = {
                "Decision Tree": {
                    'criterion': ['poisson', 'absolute_error', 'friedman_mse', 'squared_error'],
                    'splitter': ['best', 'random'],
                    'max_features': ['sqrt', 'log2'],
                },
                "Random Forest": {
                    'criterion': ['squared_error', 'friedman_mse', 'poisson', 'absolute_error'],
                    'max_features': ['sqrt', 'log2', None],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "Gradient Boosting": {
                    'loss': ['squared_error', 'absolute_error', 'quantile', 'huber'],
                    'learning_rate': [0.1, 0.01, 0.05, 0.001],
                    'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    'max_features': ['sqrt', 'log2'],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "Linear Regression": {},
                "XGBRegressor": {
                    'learning_rate': [0.1, 0.01, 0.05, 0.001],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "CatBoosting Regressor": {
                    'depth': [6, 8, 10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor": {
                    'learning_rate': [0.1, 0.01, 0.5, 0.001],
                    'loss': ['linear', 'square', 'exponential'],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                }
            }

            model_report = evaluate_models(X_train, y_train, X_test, y_test, models, params)

            # Print all model results
            logging.info("Model results:")
            for model_name, scores in model_report.items():
                logging.info(f"{model_name}: Train R2 Score - {scores[0]}, Test R2 Score - {scores[1]}, MSE - {scores[2]}, MAE - {scores[3]}") # Save in log file
                print((f"{model_name}: Train R2 Score - {scores[0]}, Test R2 Score - {scores[1]}, MSE - {scores[2]}, MAE - {scores[3]}"))

            # Find the best model based on test R2 score
            best_model_name = max(model_report, key=lambda k: model_report[k][1])  # Choose based on test R2 score
            best_model_scores = model_report[best_model_name]

            # Check if the test R2 score of the best model meets the threshold
            if best_model_scores[1] < 0.6:
                raise CustomException("No best model found")

            # Retrieve the best model
            best_model = models[best_model_name]

            # Save the best model
            save_object(file_path=self.model_trainer_config.train_model_file_path, obj=best_model)

            # Return the test R2 score, MSE, and MAE of the best model
            print("Final Best Model after Fine-tune with Hyper Paramaters")
            return best_model_scores[1], best_model_scores[2], best_model_scores[3]

        except Exception as e:
            raise CustomException(e, sys)

   