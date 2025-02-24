# Yallakora-ETL-Pipeline

## Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline that extracts football data from Yallakora, transforms it, and loads it into a MySQL database for further analysis and visualization using Jupyter Notebook.


![ETL Pipeline](https://github.com/user-attachments/assets/69fdd512-3558-4a14-89a1-f1cddef40fd2)


## Data Pipeline Workflow

1. **Extract**: Scrape data from [Yallakora](https://www.yallakora.com/) using **BeautifulSoup** and **Requests**, and store it in a CSV file with Arabic text.
   - **Scraped Information**: Championship Title, Team 1, Team 2, Score, Timing.
   - **Script**: `ScrapData.py`
2. **Translate**: Convert the Arabic data into English using **GoogleTranslator** and store it in an Excel file using **Pandas**.
   - **Script**: `translatedata.py`
3. **Transform**: Clean and preprocess the data using **Pandas** and store it in an Excel file.
   - **Script**: `CleanDatatoExcel.py`
4. **Load**: Store the transformed data in **MySQL** using **SQLAlchemy**.
   - **Script**: `LoadtoMysqlDatabase.py`
5. **Visualize**: Analyze and visualize data using **Jupyter Notebook** and **Matplotlib**.
   - **Notebook**: `visualization.ipynb`

## Tech Stack

- **Python**
- **BeautifulSoup** (for web scraping)
- **Requests** (for making HTTP requests)
- **CSV** (for initial data storage)
- **GoogleTranslator** (for data translation)
- **Pandas** (for data manipulation and cleaning)
- **Excel** (for structured storage)
- **SQLAlchemy** (for database connection)
- **MySQL** (for data storage)
- **Jupyter Notebook** (for data analysis and visualization)
- **Matplotlib** (for data visualization)

## Installation

To run this project, install the required dependencies:

```bash
pip install beautifulsoup4 requests csv pandas sqlalchemy mysql-connector-python jupyter deep-translator matplotlib
```

## How to Run

1. Clone the repository:

```bash
pip clone https://github.com/SALMASAID1/Yallakora-ETL-Pipeline.git
```

2. Scrape data from Yallakora and store it in a CSV file:

```bash
python ScrapData.py
```

3. Translate the Arabic data to English and store it in an Excel file:

```bash
python translatedata.py
```

4. Clean and preprocess the data:

```bash
python CleanDatatoExcel.py
```

5. Load the cleaned data into MySQL:

```bash
python LoadtoMysqlDatabase.py
```

6. Open Jupyter Notebook for visualization:

```bash
jupyter notebook
```

## Database Schema

The MySQL database consists of structured tables containing football match details, including Championship Title, Team 1, Team 2, Score, and Timing.

## Author

**SALMA SAID**

##

