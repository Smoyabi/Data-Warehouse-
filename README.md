

---

# 📊 Simple Data Warehouse with OLAP Operations

A Python class project demonstrating basic data warehouse concepts using SQLite, Pandas, and OLAP techniques (ROLAP, MOLAP, HOLAP), with data visualization using Seaborn and Matplotlib.

---

## 🚀 What This Project Does

This project showcases how to:
- Store and query data using a SQLite database
- Perform ROLAP (SQL-based aggregation), MOLAP (pivot-based cube), and HOLAP (hybrid slicing/dicing)
- Visualize aggregated data using bar charts and heatmaps
- Handle database connections and perform basic error handling

---

## 📦 Requirements

- Python 3.12 or higher  
- Required packages:
  ```bash
  pandas
  matplotlib
  seaborn
  numpy
  sqlite3 (built-in)
  ```

---

## 🧪 How to Run

1. **Install dependencies:**
   ```bash
   pip install pandas matplotlib seaborn numpy
   ```

2. **Run the script:**
   ```bash
   python warehouse.py
   ```

3. **What happens when you run it:**
   - Creates a SQLite database `olap_demo.db`
   - Inserts sample employee and department data
   - Executes ROLAP SQL queries for average salary by department
   - Builds a MOLAP cube (salary vs age vs department)
   - Performs HOLAP operations: slice, dice, drill-down, roll-up
   - Displays bar charts and heatmaps for visual analysis

---

## 📈 Sample Output

- ✅ Tables created: `employees` and `departments`
- ✅ ROLAP result: average salary by department (SQL)
- ✅ MOLAP cube: salary distribution across age and department
- ✅ HOLAP operations:
  - Slice: filter by department
  - Dice: filter by age and department
  - Drill-down: salary breakdown by employee
  - Roll-up: total salary by department
- ✅ Visualizations:
  - Bar chart for ROLAP
  - Heatmap for MOLAP
  - Roll-up salary chart

---

## 🗂️ Files Created

- `olap_demo.db` – SQLite database file
- Chart windows (bar plots and heatmaps) will open during execution

---

## 🧠 Key Functions

- `create_connection()` – Connects to SQLite database
- `to_sql()` – Loads Pandas DataFrames into SQL tables
- SQL query block – Performs ROLAP aggregation
- `pd.pivot_table()` – Builds MOLAP cube
- DataFrame slicing and grouping – Implements HOLAP logic
- `sns.barplot()` and `sns.heatmap()` – Visualize results

---

## 🎓 What You'll Learn

- OLAP concepts: ROLAP, MOLAP, HOLAP
- SQL joins and aggregations
- Pivot tables and cube generation
- Data slicing, dicing, drill-down, and roll-up
- Visual storytelling with Seaborn and Matplotlib
- Pythonic database interaction with Pandas and SQLite

---

## 📝 Assignment Notes

This project supports learning in:
- Data warehousing and OLAP fundamentals
- ETL workflows and schema design
- Analytical querying and cube modeling
- Visualization best practices for business intelligence

---

## 🛠️ Troubleshooting

- **Import errors?** Run:
  ```bash
  pip install pandas matplotlib seaborn numpy
  ```
- **Database locked?** Delete `olap_demo.db` and rerun the script
- **Charts not showing?** Ensure your system supports GUI windows (e.g., use Jupyter or a desktop Python environment)

---

## 📜 License

This is a class project — free to use, modify, and extend for educational purposes.

---

