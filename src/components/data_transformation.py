import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder

from src.utils import save_object
from src.exception import CustomException
from src.logger import logging
class MultiColumnLabelEncoder:

    def __init__(self, columns=None):
        self.columns = columns if columns else []

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_ = X.copy()
        for col in self.columns:
            le = LabelEncoder()
            X_[col] = le.fit_transform(X_[col])
        return X_

    def fit_transform(self, X, y=None):
        return self.fit(X).transform(X)
@dataclass 
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("data", "preprocessor.pkl")

class DataTransformation:

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        '''

        This function is responsible for data transformation

        '''

        '''
            Information of columns data types after cleaned and filled null values!
            RangeIndex: 1916 entries, 0 to 1915
            Data columns (total 24 columns):
            #   Column             Non-Null Count  Dtype  
            ---  ------             --------------  -----  
            0   Name               1916 non-null   object 
            1   Link Product       1916 non-null   object 
            2   Store              1916 non-null   object 
            3   Type               1916 non-null   object 
            4   Author Name        1916 non-null   object 
            5   Short Description  1916 non-null   object 
            6   Publisher          1916 non-null   object 
            7   Translators        1916 non-null   object 
            8   Categories         1916 non-null   object 
            9   Width              1916 non-null   float64
            10  Length             1916 non-null   float64
            11  Height             1916 non-null   float64
            12  Product ID         1916 non-null   int64  
            13  Price              1916 non-null   int64  
            14  Original Price     1916 non-null   int64  
            15  Discount           1916 non-null   int64  
            16  Discount Rate      1916 non-null   int64  
            17  Rating             1916 non-null   float64
            18  Review Count       1916 non-null   int64  
            19  Quantity Sold      1916 non-null   float64
            20  Number of page     1916 non-null   float64
            21  Range Price        1916 non-null   object 
            22  Publication Date   1916 non-null   object 
            23  Publication Year   1916 non-null   float64
            dtypes: float64(7), int64(6), object(11)
        '''
        try:

            # numerical_columns = df.select_dtypes(include=['number']).columns.tolist()

            numerical_columns = [
                                'Width',
                                'Length',
                                'Height',
                                'Product_ID',
                                'Price',
                                'Original_Price',
                                'Discount',
                                # 'Discount_Rate', # target
                                'Rating',
                                'Review_Count',
                                'Quantity_Sold',
                                'Number_of_page',
                                'Publication_Year'
                                ]
            # categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
            categorical_columns = [
                                'Store',
                                'Type',
                                'Author_Name',
                                'Publisher',
                                'Translators',
                                'Categories',
                                'Range_Price',
                            ]
            
            # Pipeline

            num_pipeline = Pipeline(
                steps = [
                    # ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            cate_pipeline = Pipeline(
                steps=[
                    ("label_encoder", MultiColumnLabelEncoder(columns=categorical_columns)),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )

            # Log info

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # Preprocessor

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cate_pipeline", cate_pipeline, categorical_columns),
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            print(train_df.columns)
            print(test_df.columns)

            logging.info("read train and test data completed!")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformation_object()

            target_column_name = "Discount_Rate"
            numerical_columns = train_df.select_dtypes(include=['number']).columns.tolist()
            print(numerical_columns)

            
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis = 1)
            print(input_feature_train_df.info)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path= self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path)

        except Exception as e:
            raise CustomException(e, sys)
        

        

    
        
