import os
import sys

from src.exception import CustomException
from src.logger import logging

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder



class DataVisualization:

    def __init__(self):
        pass


    
    def visualize_data(self, data_path):

        logging.info("Entered the data visualization components")
        
        try:
            df = pd.read_csv(data_path)
            df1 = df.copy()
            categorical_var = ['Store', 'Type', 'Author_Name','Publisher', 'Translators', 'Categories', 'Range_Price']

            self.convert_categorical_var(df1,categorical_var)    


            # 1. Overview

            self.correlation_matrix(df1)
            
            self.boxplot(df1)

            self.distribution(df1)
            

            # 2. Deep Insight
            df2 = df.copy()
            # 2.1 - Top 20 products has highest discount rate
            self.plot_top_products(df2, 20)

            # 2.1 - Top 20 stores has highest discount rate
            self.plot_top_discount_stores(df2, 200)

            # 2.2 - Large stores and the average product discount rate of those stores
            self.plot_top_stores(df2, 10)

            # 2.3 - How does product category affect discount rates?
            self.plot_category_discount_rate(df2, 10)

            # 2.4 - Products at what price range usually have a high discount rate?
            self.plot_price_range_discount_rate(df2)

            # 2.5 - Does the level of discounts affect sales?
            self.plot_top_products_sold_discount_rate(df2)

            # 2.6 - Is there any relationship between the discount rate and product rating?
            self.plot_rating_discount_rate(df2)

            # 2.7 - Change in discount rate over time!
            self.plot_discount_rate_over_years(df2)
            logging.info("Data Visualization Completed!")

            

        except Exception as e:
            raise CustomException(e, sys)
        
    def plot_discount_rate_over_years(self, df):
        plt.figure(figsize=(16, 10))

        data_from_2000 = df[df['Publication_Year'] >= 2000]
        ADR_year=data_from_2000.groupby('Publication_Year')['Discount_Rate'].mean().reset_index()
        ADR_year.columns=['Publication_Year','Average_Discount_Rate']
        sns.lineplot(x='Publication_Year',y='Average_Discount_Rate',data=ADR_year)
        plt.title('Average of Discount Rate Over Year', fontweight='bold')
        plt.xlabel('Publication Year', fontweight='bold')
        plt.ylabel('Average Discount Rate', fontweight='bold')
        plt.grid(True)

        self.store_image('discount_rate_over_years')
        # plt.show()
        
    def plot_rating_discount_rate(self, df):
        # Calculate the average discount rate for each product rating
        top_rating = df.groupby('Rating')['Discount_Rate'].mean().sort_values(ascending=False)

        plt.figure(figsize=(18, 12))
        splot = sns.barplot(x=top_rating.values, y=top_rating.index, palette='viridis', orient='h')

        # Decorating the plot
        plt.title('Average Discount Rate by Rating', fontsize=20, weight='bold')
        plt.yticks(fontsize=14)
        plt.xticks(fontsize=14)
        plt.xlabel('Average Discount Rate', fontsize=16, weight='bold')
        plt.ylabel('Rating', fontsize=16, weight='bold')

        # Add annotation to each bar
        for p in splot.patches:
            width = p.get_width()
            plt.text(0.25 + p.get_width(), p.get_y() + 0.55 * p.get_height(),
                    int(width),
                    ha='center', va='center', fontsize=14)

        plt.tight_layout()
        self.store_image('rating_discount_rate')
        # plt.show()

    def plot_top_products_sold_discount_rate(self, df):
        # Sort the DataFrame by quantity sold and select the top 20 products
        top_product_sold = df.sort_values(by='Quantity_Sold', ascending=False).head(20)

        plt.figure(figsize=(16, 4))
        plt.plot(top_product_sold['Quantity_Sold'], top_product_sold['Discount_Rate'], marker='o', linestyle='-', color='darkblue')
        plt.xlabel('Quantity Sold', fontweight='bold')
        plt.ylabel('Discount Rate', fontweight='bold')
        plt.title('Top 20 Products by Quantity Sold and Their Discount Rate', fontweight='bold')
        plt.grid(True)
        self.store_image('top_products_sold_discount_rate')
        # plt.show()


    def plot_price_range_discount_rate(self, df):
        # Calculate the average discount rate for each price range
        top_range = df.groupby('Range_Price')['Discount_Rate'].mean().sort_values(ascending=False)

        plt.figure(figsize=(16, 10))
        barplot = sns.barplot(x=top_range.index, y=top_range.values, palette='viridis')
        
        plt.title('Average Discount Rate by Price Range', fontweight='bold', fontsize=20)
        plt.xlabel('Price Range', fontweight='bold', fontsize=16)
        plt.ylabel('Average Discount Rate', fontweight='bold', fontsize=16)

        # Add text annotations to the bars
        for i, val in enumerate(top_range.values):
            barplot.text(i, val, f' {val:.2f}', ha='center', va='bottom', color='black', fontsize=14)

        plt.xticks(fontsize=16)
        plt.yticks(fontsize=16)

        plt.tight_layout()
        self.store_image('price_range_discount_rate')
        # plt.show()

    def plot_category_discount_rate(self, df, top_n=10):
        # Calculate the average discount rate and number of products for each category
        top_cate = df.groupby('Categories')['Discount_Rate'].mean()
        top_cate_quan = df.groupby('Categories')['Name'].count()

        # Merge the two Series into a DataFrame
        result = pd.concat([top_cate, top_cate_quan], axis=1).reset_index()
        result.columns = ['Categories', 'Average_Discount_Rate', 'Number_of_Products']

        # Sort the DataFrame by the number of products and select the top n categories
        result = result.sort_values(by='Number_of_Products', ascending=False).head(top_n)

        # Add a row for the remaining categories
        result.loc[len(result)] = ['Remaining', 0, len(df) - result['Number_of_Products'].sum()]

        # Plotting
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))

        # Bar plot for average discount rate by category
        sns.barplot(x='Average_Discount_Rate', y='Categories', data=result, palette='Set2', ax=axes[0])
        axes[0].set_title('Average Discount Rate by Category', fontweight='bold')
        axes[0].set_xlabel('Average Discount Rate')
        axes[0].set_ylabel('Categories')

        # Pie chart for the distribution of products by category
        axes[1].pie(result['Number_of_Products'], labels=result['Categories'], autopct='%1.1f%%', colors=sns.color_palette('Pastel1'))
        axes[1].set_title('Product Distribution by Category', fontweight='bold')

        plt.tight_layout()
        self.store_image('category_discount_rate_relationship')
        # plt.show()



    
    def plot_top_stores(self, df, top_n=10):
        # Group by store and calculate the number of products and average discount rate
        store_pro = df.groupby("Store")['Name'].count()
        store_dis = df.groupby("Store")['Discount_Rate'].mean()

        # Merge the two Series into a DataFrame
        result = pd.concat([store_pro, store_dis], axis=1).reset_index()
        result.columns = ['Store', 'Number_of_Products', 'Average_Discount_Rate']

        # Sort the DataFrame by the number of products and select the top n stores
        result = result.sort_values(by='Number_of_Products', ascending=False).head(top_n)

        bar_width = 0.4
        index = np.arange(len(result))

        # Create figure and subplot
        fig, ax1 = plt.subplots(figsize=(20, 8))

        # Plot bars for number of products
        bars1 = ax1.barh(index, result['Number_of_Products'], bar_width, label='Number of Products', color='blue')

        # Create twinned axes for average discount rate
        ax2 = ax1.twiny()
        bars2 = ax2.barh(index + bar_width, result['Average_Discount_Rate'], bar_width, label='Average Discount Rate', color='green')

        # Set y-axis ticks and labels
        ax1.set_yticks(index + bar_width / 2)
        ax1.set_yticklabels(result['Store'])
        ax1.set_ylabel('Store')

        # Set x-axis labels
        ax1.set_xlabel('Number of Products', color='blue')
        ax2.set_xlabel('Average Discount Rate', color='green')

        # Add text annotations
        for i, v in enumerate(result['Number_of_Products']):
            ax1.text(v + 2, i, str(v), color='blue', va='center', fontsize=8, fontweight='normal')

        for i, v in enumerate(result['Average_Discount_Rate']):
            ax2.text(v + 0.02, i + bar_width, f'{v:.2f}', color='green', va='center', fontsize=8, fontweight='normal')

        plt.title('Top 10 Stores with the Most Products')

        # Save image
        self.store_image('top_10_big_store')

        # plt.show()




    def plot_top_products(self, df, top_n=10):
        top_products = df.sort_values(by='Discount_Rate', ascending=False).reset_index()
        top_n_sp = top_products[['Name', 'Store', 'Discount_Rate']].head(top_n)

        plt.figure(figsize=(10, 6))
        sns.barplot(x='Discount_Rate', y='Name', data=top_n_sp)
        plt.xlabel('Discount Rate')
        plt.ylabel('Product Name')
        plt.title(f'Top {top_n} Products with Highest Discount Rate')
        plt.tight_layout()
        self.store_image('top_10_highest_discount_rate_products')
        # plt.show()

    def plot_top_discount_stores(self, df, top_n=10):
        top_products = df.sort_values(by='Discount_Rate', ascending=False).reset_index()
        top_n_sp = top_products[['Name', 'Store', 'Discount_Rate']].head(top_n)
        top_10_store = top_n_sp["Store"].value_counts().head(10)

        custom_color = sns.cubehelix_palette(10, rot=-.25, light=.7)

        plt.figure(figsize=(18, 12))
        splot = sns.barplot(x=top_10_store.values, y=top_10_store.index, palette=custom_color)
        # Decorating the plot
        plt.title('Top 10 Stores with the Most Products with Highest Discount Rate', fontsize=15, weight='bold')
        plt.yticks(fontsize=14)
        plt.xticks(fontsize=14)
        plt.xlabel('Number of Products', fontsize=14)
        plt.ylabel('Store', fontsize=14)

        # Add annotation to each bar
        for p in splot.patches:
            width = p.get_width()
            plt.text(1.25 + p.get_width(), p.get_y() + 0.55 * p.get_height(),
                    int(width),
                    ha='center', va='center', fontsize=14)

        plt.tight_layout()
        self.store_image('top_10_highest_discount_stores.png')
        # plt.show()

    def correlation_matrix(self, df):
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df_numeric = df[numeric_cols]

        correlation_matrix = df_numeric.corr(method='spearman')
        mask = np.zeros_like(correlation_matrix)
        mask[np.triu_indices_from(mask)] = True
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix,mask=mask, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Matrix', fontsize=20, weight= 'bold')
        self.store_image('correlation_matrix')
        # plt.show()


    def boxplot(self, df):
        numerical_columns = df.select_dtypes(include=np.number)

        num_plots = len(numerical_columns.columns)
        fig, axes = plt.subplots(nrows=4, ncols=5, figsize=(16, 8))
        axes = axes.flatten()

        for i, col in enumerate(numerical_columns.columns):
            sns.boxplot(x=numerical_columns[col], ax=axes[i], palette='Set2', showfliers=False)
            axes[i].set_title(f'Boxplot of {col}')
            axes[i].set_xlabel(None)

        for i in range(num_plots, len(axes)):
            axes[i].remove()

        plt.tight_layout()
        self.store_image('boxplot')
        # plt.show()

    def distribution(self, df):
        columns_to_plot = ['Price', 'Original_Price', 'Discount', 'Discount_Rate']
        plt.figure(figsize=(16, 10))
        for i, column in enumerate(columns_to_plot, 1):
            plt.subplot(2, 2, i)
            sns.histplot(df[column], kde=True)
            plt.title(f'Distribution of {column}',fontweight='bold',fontsize=16)
            plt.xlabel(column,fontweight='bold',fontsize=12)
            plt.ylabel('Frequency',fontweight='bold',fontsize=12)

        plt.tight_layout(pad=2)
        self.store_image('distribution')
        # plt.show()

        
        
    def convert_categorical_var(self, data, columns):
        label_encoder = LabelEncoder()
        for col in columns:
            data[col] = label_encoder.fit_transform(data[col])

    def store_image(self, file_name):

        if not file_name.endswith('.png'):
            file_name += '.png'
        output_dir = 'Data Visualization'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, file_name)
        plt.savefig(output_path)



