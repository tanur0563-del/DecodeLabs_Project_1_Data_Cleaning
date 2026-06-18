# DecodeLabs Project 1: Data Cleaning & Preparation

## Project Overview
This project focuses on cleaning and preparing a raw e-commerce dataset using Python and Pandas. The objective was to transform a messy dataset into a clean, accurate, and analysis-ready dataset.

## Tools & Technologies Used
- Python
- Pandas
- Visual Studio Code
- Git SCM
- GitHub

## Dataset
The dataset contains e-commerce order records with details such as:
- Order ID
- Order Date
- Customer ID
- Product Information
- Quantity and Pricing
- Payment Method
- Order Status
- Tracking Details
- Coupon Codes
- Referral Sources

## Data Cleaning Steps Performed

### 1. Dataset Exploration
- Loaded the CSV dataset using Pandas.
- Checked dataset shape, columns, and data types.
- Examined the first few records of the dataset.

### 2. Handling Missing Values
- Identified null and missing values.
- Removed critical missing records.
- Filled missing text values with "Unknown".
- Filled missing numerical values using median values.

### 3. Removing Duplicates
- Identified duplicate rows.
- Removed duplicate records.
- Verified that there are zero duplicate Order IDs.

### 4. Data Format Correction
- Converted the Date column into a proper date format.
- Removed invalid date entries.
- Standardized text formatting by removing extra spaces and maintaining consistency.

### 5. Final Validation
- Checked the final dataset for:
  - Missing values
  - Duplicate rows
  - Duplicate Order IDs
  - Correct data formats

## Project Files

- `Dataset for Data Analytics - Sheet1.csv` : Original raw dataset
- `data_cleaning.py` : Python script containing the complete data cleaning process
- `cleaned_dataset.csv` : Final cleaned dataset
- `README.md` : Project documentation

## Project Outcome
The raw dataset was successfully cleaned and transformed into a reliable dataset ready for further data analysis, visualization, and machine learning applications.


