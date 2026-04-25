#  ETL / QA Data Validation Project

## Overview
This project focuses on validating data across different layers:

- Source Files → Silver Layer  
- Silver Layer → Gold Layer  

The goal is to ensure data is correctly transformed, aggregated, and meets business requirements.

---

## 🗂️ Project Structure

### 📁 src (Source Files)
These are the raw input files:

- `Customer.xls` → Customer details  
- `Order.csv` → Order details  
- `Shipping.json` → Shipping details  

---

###  Data Models

We created data models to understand data flow:

- `data_model_src_files_to_silver_tables.png`  
  → Shows mapping from source files to silver tables  

- `data_model_silver_to_gold.png`  
  → Shows transformation from silver layer to gold layer  

---

###  Documentation Files

- `repo details.docx`  
  → Information about Git repo  

- `Signing up to databricks.docx`  
  → Steps followed to set up Databricks  

- `vs code.docx`  
  → Initial setup, Git initialization, and first commits  

---

###  Python Scripts

- `flatten_json.py`  
  → Used to flatten JSON file (`Shipping.json`)  
  → Output file: `shipping_flatten_output.csv`  

- `validate_data.py`  
  → Used to compare source and target data  
  → Helps identify mismatches between datasets  

---

##  Validation Reports (Main Work)

We created **two separate validation reports**:

---

### 1️⃣ Source → Silver Validation  
 File: `src_files_to_silver_validation.xlsx`

- Validates data from source files to silver tables  
- Covers:
  - Schema validation  
  - Data validation  
  - Record count checks  
  - Data quality checks  

---

### 2️⃣ Silver → Gold Validation  
 File: `silver_to_gold_validation.xlsx`

- Validates data from silver tables to gold tables  
- Covers:
  - Business logic validation  
  - Aggregations (sum, count, etc.)  
  - Requirement-based testing  
  - Final output validation  

---

##  Tools Used

- Databricks  
- PySpark  
- SQL  
- Excel  

---

##  Testing Approach

We performed:

### 🔹 Source → Silver Validation
- Checked data ingestion  
- Verified schema and data types  
- Validated data consistency  

### 🔹 Silver → Gold Validation
- Validated business requirements  
- Checked aggregations and transformations  
- Compared source query output vs target tables  

---

##  Key Highlights

- Separate validation reports for each layer  
- Data model diagrams for better understanding  
- End-to-end testing from raw data to final output  
- Detailed test cases, metrics, requirement gaps and bug reports included  

---

##  Outcome

- All test cases executed successfully(defects exists)  
- Data validated across all layers  
- 3 defects found while validating source files vs silver layer
- Requirement gaps documented separately  

---

##  Summary

This project demonstrates a complete ETL QA validation process, ensuring data accuracy from source files to final reporting tables in the gold layer.