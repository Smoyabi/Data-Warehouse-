# simple_data_warehouse.py
# Creating a simple data warehouse using Python, Pandas, and SQLite

import pandas as pd
import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(e)
    return conn

# Function to execute a query
def execute_query(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        print("Query executed successfully")
    except Error as e:
        print(e)

# Function to fetch data from a query
def fetch_data(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)
        return None

# Function to create a table from a DataFrame
def create_table_from_df(conn, df, table_name):
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Table '{table_name}' created successfully")

# Function to visualize data
def visualize_data(df, x, y, kind='bar'):
    plt.figure(figsize=(8, 5))
    if kind == 'bar':
        sns.barplot(x=x, y=y, data=df)
    elif kind == 'line':
        sns.lineplot(x=x, y=y, data=df)
    elif kind == 'scatter':
        sns.scatterplot(x=x, y=y, data=df)
    plt.title(f"{kind.capitalize()} chart of {y} vs {x}")
    plt.show()

# Function to perform basic data analysis
def basic_data_analysis(df):
    print("\n=== Dataframe Head ===")
    print(df.head())
    print("\n=== Dataframe Info ===")
    print(df.info())
    print("\n=== Dataframe Description ===")
    print(df.describe())
    print("\n=== Missing Values ===")
    print(df.isnull().sum())

# Main function
def main():
    database = "data_warehouse.db"
    conn = create_connection(database)

    if conn is not None:
        # Create a sample dataframe
        data = {
            'id': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
            'age': [24, 30, 22, 35, 28],
            'salary': [50000, 60000, 55000, 70000, 65000]
        }
        df = pd.DataFrame(data)

        # Create table from dataframe
        create_table_from_df(conn, df, 'employees')

        # Fetch data from table
        rows = fetch_data(conn, "SELECT * FROM employees")
        print("\n=== Fetched Data from Database ===")
        for row in rows:
            print(row)

        # Perform basic data analysis
        basic_data_analysis(df)

        # Visualize data
        visualize_data(df, x='name', y='salary', kind='bar')

        conn.close()
    else:
        print("Error! Cannot create the database connection.")

# Entry point
if __name__ == '__main__':
    main()
