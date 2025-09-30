# Simple Data Warehouse

A Python class project demonstrating basic data warehouse concepts using SQLite, Pandas, and data visualization.

## What This Project Does

This is a simple data warehouse implementation that shows how to:
- Store data in a SQLite database
- Perform basic data analysis
- Create visualizations from stored data
- Handle database connections and errors

## Requirements

- Python 3.12 or higher
- Required packages:
  ```
  pandas
  matplotlib
  seaborn
  numpy
  ```

## How to Run

1. **Install the required packages:**
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```

2. **Run the program:**
   ```bash
   python simple_data_warehouse.py
   ```

3. **What happens when you run it:**
   - Creates a SQLite database called `data_warehouse.db`
   - Inserts sample employee data (names, ages, salaries)
   - Shows basic statistics about the data
   - Creates a bar chart showing employee salaries
   - Displays the data in your terminal

## Sample Output

When you run the program, you'll see:
- Database connection confirmation
- Employee data displayed in a table format
- Basic statistics (mean, median, etc.)
- Information about missing values
- A bar chart showing salary comparisons

## Files Created

- `data_warehouse.db` - SQLite database file (created automatically)
- Various chart windows will pop up when running

## Key Functions

- `create_connection()` - Connects to SQLite database
- `create_table_from_df()` - Converts pandas DataFrame to database table
- `basic_data_analysis()` - Shows data statistics and info
- `visualize_data()` - Creates charts from the data
- `fetch_data()` - Retrieves data from database

## What You'll Learn

This project demonstrates:
- Database connections and operations
- Data analysis with pandas
- Data visualization with matplotlib/seaborn
- Error handling in Python
- Working with CSV-like data structures

## Assignment Notes

This project covers the following concepts typically taught in data management classes:
- ETL (Extract, Transform, Load) basics
- Database design principles
- Data analysis workflows
- Visualization best practices

## Troubleshooting

**Common Issues:**
- If you get import errors, make sure all packages are installed: `pip install pandas matplotlib seaborn numpy`
- If the database file is locked, close the program and delete `data_warehouse.db`, then run again
- Charts should open in new windows - if they don't appear, check if your system supports GUI applications

## License

This is a class project - free to use and modify for educational purposes.
