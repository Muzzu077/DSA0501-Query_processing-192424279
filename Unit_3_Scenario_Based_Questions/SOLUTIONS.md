# UNIT 3: DATA PREPROCESSING & CLEANUP SCENARIOS - SOLUTIONS

## Scenario 1: Why Clean Data?
**Problem:** A dataset contains missing values and inconsistent data formats. We need to clean it before analysis.

### Solution & Answers
1. **Why is data cleaning necessary prior to data analysis?**
   - Raw datasets often contain missing entries (`None`/`NaN`), invalid types (e.g. text `'Thirty'` in numeric `Age` column), and non-standard formats (e.g. `'Sixty-Five Thousand'`). Uncleaned data causes calculation errors, algorithm failures, skewed statistics, and misleading business insights ("Garbage In, Garbage Out").
2. **How does pandas handle missing strings vs invalid numerical values?**
   - `df['Name'].fillna('Unknown')` replaces missing string/`None` entries with a default placeholder.
   - `pd.to_numeric(df['Age'], errors='coerce')` attempts to parse values into numbers. Non-numeric text like `'Thirty'` cannot be automatically parsed and is converted to `NaN` (Not a Number) float.
   - `df['Salary'].replace('Sixty-Five Thousand', 65000).astype(int)` maps text-form numbers to actual numeric integers before casting.
3. **Modern Pandas Best Practice Note:**
   - In modern Pandas (v2.0+), `inplace=True` is deprecated for series methods. The recommended syntax is explicit assignment: `df['Name'] = df['Name'].fillna('Unknown')`.

---

## Scenario 2: Identifying Values for Data Cleanup
**Problem:** Identifying missing values and incorrect entries in a dataset.

### Solution & Answers
1. **How do `df.isnull().sum()` and `df.dtypes` aid in data cleanup?**
   - `df.isnull().sum()` calculates the exact total number of missing/`NaN` values present in each column. Here, it correctly highlights that `Age` has 2 missing values (from `'Thirty'` coercing to `NaN` and original `None`).
   - `df.dtypes` inspects the column data types. It verifies whether columns match their expected types (`Name`: `object`, `Age`: `float64`, `Salary`: `int64`).
2. **Why did the `Age` column become `float64` instead of `int64`?**
   - Standard integer arrays (`int64`) in Pandas cannot represent missing values (`NaN`). When a column contains `NaN` values, Pandas automatically upcasts numeric data types to `float64` to support `NaN`.

---

## Scenario 3: Formatting Data
**Problem:** The Date column is in multiple formats. We need to standardize it.

### Solution & Answers
1. **What issue does inconsistent date formatting create, and how does `pd.to_datetime()` solve it?**
   - Inconsistent dates (ISO `YYYY-MM-DD`, US `MM-DD-YYYY`, slashed `MM/DD/YYYY`, long text `April 7, 2025`) prevent sorting, time-series analysis, and date comparisons. `pd.to_datetime()` intelligently infers diverse date formats and converts string objects into unified `datetime64[ns]` objects.
2. **How can standardized date columns be further utilized?**
   - Once converted to `datetime64[ns]`, Pandas enables date extraction properties like `df['Date'].dt.year`, `df['Date'].dt.month_name()`, `df['Date'].dt.day_name()`, and date arithmetic (e.g., calculating elapsed days).

---

## Scenario 4: Finding Outliers and Bad Data
**Problem:** Detecting outliers in the Sales column using the Interquartile Range (IQR) method.

### Solution & Answers
1. **Explain the mathematics of the IQR Outlier Detection Method.**
   - $Q_1$ (25th Percentile) separates the lowest 25% of data.
   - $Q_3$ (75th Percentile) separates the lowest 75% of data.
   - Interquartile Range ($IQR$) = $Q_3 - Q_1$ (represents middle 50% spread).
   - $\text{Lower Bound} = Q_1 - 1.5 \times IQR$
   - $\text{Upper Bound} = Q_3 + 1.5 \times IQR$
   - Any value outside $[\text{Lower Bound}, \text{Upper Bound}]$ is flagged as an outlier.
2. **Why were 1500 and 10000 flagged as outliers in this dataset?**
   - For the Sales dataset: $Q_1 = 257.5$, $Q_3 = 600.0$, $IQR = 342.5$. Upper Bound = $600 + 1.5(342.5) = 1113.75$. Since `1500` and `10000` both exceed `1113.75`, they are correctly identified as severe high outliers.

---

## Scenario 5: Finding Duplicates
**Problem:** Identifying and removing duplicate records in a dataset.

### Solution & Answers
1. **How does `df.duplicated()` identify duplicates, and what parameters can modify its behavior?**
   - `df.duplicated()` returns a boolean mask indicating duplicate rows across specified columns (or all columns by default). By default, `keep='first'` marks the first occurrence as `False` (unique) and subsequent identical occurrences as `True` (duplicate).
   - `keep='last'` keeps the final occurrence.
   - `keep=False` marks ALL identical duplicates as `True`.
2. **Why is removing duplicates important?**
   - Duplicate rows artificially inflate sample sizes, distort mean/variance calculations, over-weight identical instances in Machine Learning training models, and cause erroneous metrics reporting.

---

## Scenario 6: Fuzzy Matching
**Problem:** Matching similar but slightly misspelled names in a dataset.

### Solution & Answers
1. **What mechanism powers fuzzy matching in Python?**
   - Fuzzy matching computes string similarity using the **Levenshtein Distance** algorithm, which measures the minimum number of single-character edits (insertions, deletions, substitutions) required to change one word into another.
2. **Interpret the similarity scores in the output:**
   - `'John Doe'` (100): Exact match.
   - `'Jon Doe'` (95): High match score (1 deletion of letter `'h'`).
   - `'J0hn Doe'` (80): Good match score (1 character substitution: digit `'0'` instead of letter `'O'`).

---

## Scenario 7: RegEx Matching
**Problem:** Finding invalid email formats using Regular Expressions (RegEx).

### Solution & Answers
1. **Break down the components of the regular expression pattern used.**
   - `^` : Asserts start of the string.
   - `[a-zA-Z0-9_.+-]+` : Matches 1 or more alphanumeric chars, dots, underscores, pluses, or hyphens (username).
   - `@` : Matches mandatory literal `@` symbol.
   - `[a-zA-Z0-9-]+` : Matches 1 or more domain name characters.
   - `\.` : Matches mandatory literal dot `.`.
   - `[a-zA-Z0-9-.]+` : Matches top-level domain extension.
   - `$` : Asserts end of the string.
2. **Why were `'invalid-email@'` and `'hello@world'` flagged as invalid?**
   - `'invalid-email@'` lacks a domain name and dot extension after `@`.
   - `'hello@world'` lacks a top-level domain extension (missing a dot and suffix like `.com` or `.org`).

---

## Scenario 8: Normalizing and Standardizing Data
**Problem:** Standardizing a numerical column using Min-Max scaling.

### Solution & Answers
1. **State the formula for Min-Max Normalization and calculate values for this dataset.**
   - Formula: $X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$
   - Here, $X_{\min} = 100, X_{\max} = 500, \text{Range} = 400$.
   - For 100: $(100 - 100) / 400 = 0.00$
   - For 200: $(200 - 100) / 400 = 0.25$
   - For 300: $(300 - 100) / 400 = 0.50$
   - For 400: $(400 - 100) / 400 = 0.75$
   - For 500: $(500 - 100) / 400 = 1.00$
2. **What is the difference between Normalization and Standardization?**
   - **Normalization (Min-Max Scaling)** rescales values into a bounded range of $[0, 1]$. Best used when data does not assume a normal distribution.
   - **Standardization (Z-score Scaling)** rescales data to have $\mu = 0$ and $\sigma = 1$ ($X_{\text{std}} = \frac{X - \mu}{\sigma}$). Best used when algorithms assume Gaussian-distributed features (e.g. SVM, Logistic Regression).

---

## Scenario 9: Saving the Data
**Problem:** Saving the cleaned dataset to a CSV file.

### Solution & Answers
1. **Why is `index=False` recommended when saving DataFrames to CSV?**
   - By default, pandas writes the integer index (`0, 1, 2, ...`) as an un-named first column. Setting `index=False` prevents creating a redundant `'Unnamed: 0'` index column every time the CSV is read and written.
2. **What alternative file export formats exist in pandas?**
   - `df.to_parquet('data.parquet')`: Fast binary columnar storage format with compression.
   - `df.to_excel('data.xlsx')`: For spreadsheet reporting.
   - `df.to_json('data.json')`: For web API integration.

---

## Scenario 10: Automating Data Cleanup with a Script
**Problem:** Creating a reusable Python function/script to automate dataset cleanup and transformation pipelines.

### Solution & Answers
1. **Why is automating data cleanup through functions critical in production pipelines?**
   - Modular data cleaning functions encapsulate data transformation rules into repeatable, testable units. This ensures consistency across training and testing data splits in Machine Learning and facilitates batch processing in automated ETL pipelines.
2. **Syntax Fix Note in Original Code:**
   - The original code snippet contained a concatenated line error (`df = clean_data(df)print(df)`). The fixed code separates assignment and print statements into valid Python syntax.
