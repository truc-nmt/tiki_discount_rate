import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.utils import save_object
from src.exception import CustomException
from src.logger import logging

@dataclass 
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("models", "preprocessor.pkl")

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
                                'Product ID',
                                'Price',
                                'Original Price',
                                'Discount',
                                'Discount Rate',
                                'Rating',
                                'Review Count',
                                'Quantity Sold',
                                'Number of page',
                                'Publication Year'
                                ]
            # categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
            categorical_columns = [
                                    # 'Name',  # not use 
                                    # 'Link Product', # not use
                                    'Store',
                                    'Type',
                                    'Author Name',
                                    # 'Short Description', # not use
                                    'Publisher',
                                    'Translators',
                                    'Categories',
                                    'Range Price',
                                    # 'Publication Date' # not use
                                    ]
            
            # Pipeline

            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            cate_pipeline = Pipeline(

                steps = [
                    ("Imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
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
                    ("cate_pipeline", cate_pipeline, categorical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
