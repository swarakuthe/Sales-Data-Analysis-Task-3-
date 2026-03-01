# Project Overview

This project analyzes a sales dataset using Python and Pandas to calculate key business metrics such as total revenue, best-selling product, and top-performing products.

The goal is to demonstrate data cleaning, analysis, and reporting using real-world sales data.

# Objectives

Load and explore a sales dataset

Handle missing values and remove duplicates

Calculate revenue

Identify best-selling products

Generate a clean analysis report

# Tools & Technologies

Python

Pandas

# Project Structure
Sales-Data-Analysis/
│
├── sales_analysis.py
├── sales_data.csv
├── analysis_report.md
└── requirements.txt

# Steps Performed

# Data Loading

Loaded CSV file using pandas

# Data Cleaning

Checked for missing values

Filled missing Quantity values with 0

Filled missing Price values with average price

Removed duplicate records

# Feature Creation

Created a new column: Revenue = Quantity × Price

# Data Analysis

The following metrics were calculated:

Total Revenue

Total Quantity Sold

Best Product by Quantity

Best Product by Revenue

Top 3 Products by Revenue

Highest Single Sale

Lowest Single Sale

Total Unique Products

Average Revenue per Product

# Key Insights

Identified the highest revenue-generating product

Found the most sold product by quantity

Determined overall business performance through total revenue

# How to Run the Project

Install required libraries: pandas 

pip install -r requirements.txt

# Conclusion

This project demonstrates basic data cleaning and sales analysis using Python.
It provides meaningful insights that help understand product performance and overall revenue trends.
