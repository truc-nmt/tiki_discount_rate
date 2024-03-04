Predicting Discount Rates of Tiki Products EDA and Visualiaztion
==============================

<p>
    <small><b>Data Analysis and Visualization Project</b><br>
    Faculty of Information Science and Engineering, University of Information Technology <br>
    Vietnam National University, Ho Chi Minh City, Vietnam<br>
</p>

## Contributing Members

|Name     |  Email   | Edu Mail|
|---------|-----------------|----------------------|
|Truc Mai-Thanh Nguyen| truc.ngmaithanh@gmail.com | 21522721@gm.uit.edu.vn|
|Dat Minh Nguyen |     nguyenminhdatyasuo@gmail.com    | 21521937@gm.uit.edu.vn|


-------------------------------
Project Description: 
------------------------------
In this project, we aim to develop a predictive model to forecast the discount rates of products available on the popular e-commerce platform Tiki. With the abundance of online shopping options, consumers are often on the lookout for the best deals, and businesses need to strategically manage their pricing and promotional strategies. By predicting the discount rates of products, we can provide valuable insights to both consumers and businesses, enabling informed decision-making and optimization of various aspects of the retail process.
![Image Alt text](images/tiki_book.png)

Dataset 
-------------------------------
| Attribute         | Description                                                                                      |
|-------------------|--------------------------------------------------------------------------------------------------|
| Product ID        | The unique identifier for each product.                                                          |
| Name              | The name of the product.                                                                         |
| Link Product      | The hyperlink leading to the product.                                                            |
| Store             | The name of the store selling the product.                                                       |
| Price             | The discounted price of the product.                                                             |
| Original Price    | The original price of the product.                                                               |
| Discount          | The amount of discount applied to the product.                                                   |
| Discount Rate     | The percentage decrease in price from the original to the discounted price.                       |
| Rating            | The customer satisfaction rating on a scale from 1 to 5.                                          |
| Review Count      | The number of customer reviews for the product.                                                   |
| Type              | The type of product, simple or configurable.                                                      |
| Quantity Sold     | The quantity of the product sold.                                                                 |
| Author Name       | The name of the author for books.                                                                 |
| Short Description| A brief description of the product.                                                               |
| Publisher         | The name of the publisher for books.                                                              |
| Publication Date  | The publication date of books.                                                                    |
| Translators       | The name of the translator for books.                                                             |
| Number of Pages   | The number of pages in a book.                                                                    |
| Categories        | The categories or genres of books.                                                                                                                                     |
| is_authentic      | Indicates whether the product is authenticated.                                                   |
| has_buynow        | Indicates whether the product is available for purchase.                                          |
| Has Book          | Indicates whether the product is a book.                                                          |
| Gift Item Title   | Title of any accompanying gift item.                                                              |
| Stock Item        | Initial stock quantity of books.                                                                  |


Methods Used
------------
* Statistics
* Machine Learning
* Data Collection
* Exploratory Data Analysis
* Data Visualiaztion
* Predictive Modeling 


Project Organization
------------
    └── LICENSE
    └── Makefile
    └── README.md
    └── .gitignore
    └── requirements.txt        <- packages requirements
    └── setup.py
    └── test_environment.py     <- test python version environment (python/python3)
    └── data                    <- Include raw data, processed data
        └── processed
            └── .gitkeep
            └── Data_Tiki_Cleaned.csv
        └── raw
            └── .gitkeep
            └── Data_Tiki_Raw.xlsx
    └── docs
        └── commands.rst
        └── conf.py
        └── getting-started.rst
        └── index.rst
        └── make.bat
        └── Makefile
    └── images
        └── tiki_book.png
    └── models                  <- Model trained
        └── .gitkeep
    └── notebooks               <- (.ipynb) notebook of project
        └── .gitkeep
    └── references
        └── .gitkeep
    └── reports 
        └── .gitkeep
        └── figures
            └── .gitkeep
    └── src
        └── components
            └── data_ingestion.py
            └── data_transformation.py
            └── model_trainer.py
            └── __init__.py
        └── data
            └── .gitkeep
            └── make_dataset.py
            └── __init__.py
        └── features
            └── .gitkeep
            └── build_features.py
            └── __init__.py
        └── models
            └── .gitkeep
            └── predict_model.py
            └── train_model.py
            └── __init__.py
        └── visualization
            └── .gitkeep
            └── visualize.py
            └── __init__.py
        └── logger.py
        └── exception.py
        └── utils.py
        └── __init__.py
    └── src.egg-info
        └── dependency_links.txt
        └── PKG-INFO
        └── SOURCES.txt
        └── top_level.txt




Task Assignments Responsibility
-----------------------------------
|No.|Task|Resposibility Member|
|----|--------------|----------------------|
|1|Crawling Data|Dat Minh Nguyen|
|2|Cleaning Data|Truc Mai-Thanh Nguyen|
|3|Project Organization|Truc Mai-Thanh Nguyen|
|4|Exploratory Data Analysis|Truc Mai-Thanh Nguyen  <br> Dat Minh Nguyen|
|5|Predictive Modeling|Dat Minh Nguyen|
|6|Data Visualization|Truc Mai-Thanh Nguyen|
|7|Notebook (.ipynb)<br>Source (.py)|Dat Minh Nguyen <br> Truc Mai-Thanh Nguyen|
|8|Demo App|Dat Minh Nguyen|
|10|Report|Truc Mai-Thanh Nguyen|

-------------------







