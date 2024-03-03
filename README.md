Predicting Discount Rates of Tiki Products EDA and Visualiaztion
==============================
![Image Alt text](images/tiki_book.png)
-------------------------------
Project Description: 
------------------------------
In this project, we aim to develop a predictive model to forecast the discount rates of products available on the popular e-commerce platform Tiki. With the abundance of online shopping options, consumers are often on the lookout for the best deals, and businesses need to strategically manage their pricing and promotional strategies. By predicting the discount rates of products, we can provide valuable insights to both consumers and businesses, enabling informed decision-making and optimization of various aspects of the retail process.

Dataset Attributes
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
* Exploratory Data Analysis
* Data Visualiaztion
* Predictive Modeling 


Project Organization
------------


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

## Contributing Members



|Name     |  Email   | Edu Mail|
|---------|-----------------|----------------------|
|Truc Mai-Thanh Nguyen| truc.ngmaithanh@gmail.com | 21522721@gm.uit.edu.vn|
|Dat Minh Nguyen |     dat.minhnguyen@gmail.com    | 21521937@gm.uit.edu.vn|

Task Assignments Responsibility
-----------------------------------
|No.|Task|Resposibility Member|
|----|--------------|----------------------|
|1|Crawling Data|Dat Minh Nguyen|
|2|Cleaning Data|Truc Mai-Thanh Nguyen|
|3|Design Project|Truc Mai-Thanh Nguyen|
|4|Exploratory Data Analysis|Truc Mai-Thanh Nguyen  <br> Dat Minh Nguyen|
|5|Predictive Modeling|Dat Minh Nguyen|
|6|Data Visualization|Truc Mai-Thanh Nguyen|
|7|Notebook (.ipynb)<br>Source (.py)|Dat Minh Nguyen <br> Truc Mai-Thanh Nguyen|
|8|Demo App|Dat Minh Nguyen|
|10|Report|Truc Mai-Thanh Nguyen|






--------
<!-- 
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p> -->
