# UNIT 4: DATA EXPLORATION AND ANALYSIS (CO4)
**Course:** DSA05 / DSA0501 – Query Processing for Data Science  
**Target:** 180-Question MCQ Exam Preparation & Comprehensive Concept Mastery  
**Assessment Framework:** Bloom's Revised Taxonomy (Levels L1 to L6)

---

## 📌 TABLE OF CONTENTS
1. [Core Concepts of Exploratory Data Analysis (EDA)](#1-core-concepts-of-exploratory-data-analysis-eda)
   - 1.1 Objectives & Scope of EDA
   - 1.2 The Split-Apply-Combine Strategy
2. [Data Ingestion & Structural Inspection](#2-data-ingestion--structural-inspection)
   - 2.1 Importing Diverse Formats (`read_csv`, `read_excel`, `read_sql`, `read_json`)
   - 2.2 Structural Inspection (`shape`, `info`, `describe`, `dtypes`, `nunique`)
3. [Table Operations, Indexing & Slicing](#3-table-operations-indexing--slicing)
   - 3.1 `.loc[]` (Label-Based) vs `.iloc[]` (Integer-Position-Based)
   - 3.2 Boolean Filtering & `.query()` Method
   - 3.3 Sorting, Column Transformations & `.apply()`
4. [Joining & Combining Numerous Datasets](#4-joining--combining-numerous-datasets)
   - 4.1 `pd.merge()` & Join Types (Inner, Left, Right, Outer, Cross)
   - 4.2 `pd.concat()` (Row-wise vs Column-wise)
   - 4.3 Semi-Joins and Anti-Joins
5. [Statistical Correlations & Association Detection](#5-statistical-correlations--association-detection)
   - 5.1 Pearson Correlation Coefficient ($r$) & Range
   - 5.2 Spearman Rank ($\rho$) & Kendall's Tau ($\tau$)
   - 5.3 Correlation Matrices, Heatmaps & "Correlation $\neq$ Causation"
6. [Groupings, Aggregations & Pivot Tables](#6-groupings-aggregations--pivot-tables)
   - 6.1 `groupby()` Operations with `.agg()`
   - 6.2 `.transform()` vs `.agg()`
   - 6.3 Pivot Tables (`pd.pivot_table`) & Cross-Tabulations (`pd.crosstab`)
7. [Visualizing & Presenting Analytical Insights](#7-visualizing--presenting-analytical-insights)
   - 7.1 Matching Visual Encodings to Data Types (Charts, Distributions, Trends)
   - 7.2 Time-Series, Geospatial Maps, Interactive Dashboards, Word Clouds
   - 7.3 Publishing Platforms & Open Data Ecosystems
8. [High-Yield Exam Tips & Common MCQ Traps](#8-high-yield-exam-tips--common-mcq-traps)
9. [Bloom's Taxonomy-Aligned MCQ Question Bank (40+ Questions)](#9-blooms-taxonomy-aligned-mcq-question-bank)
   - [9.1 Level 1: Remember (Knowledge & Recall)](#91-level-1-remember-knowledge--recall)
   - [9.2 Level 2: Understand (Comprehension & Explanation)](#92-level-2-understand-comprehension--explanation)
   - [9.3 Level 3: Apply (Application, Computation & Code Output)](#93-level-3-apply-application-computation--code-output)
   - [9.4 Level 4: Analyze (Analysis, Logic & Bug Detection)](#94-level-4-analyze-analysis-logic--bug-detection)
   - [9.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)](#95-level-5--6-evaluate--create-judgment-architecture--design)

---

## 1. CORE CONCEPTS OF EXPLORATORY DATA ANALYSIS (EDA)

### 1.1 Objectives of EDA
* Uncover data distributions, detect anomalies/outliers, verify hypotheses, and extract key features using summary statistics and visualization.

### 1.2 Split-Apply-Combine Strategy
```
Raw Dataset ──► [ SPLIT ] into Groups ──► [ APPLY ] Aggregation/Function ──► [ COMBINE ] into Summary Table
```

---

## 2. TABLE OPERATIONS & INDEXING

* **`.loc[]`:** Label-based indexing. End label is **INCLUSIVE** (`df.loc['A':'C']` includes `'C'`).
* **`.iloc[]`:** Integer-position indexing (0 to $N-1$). End position is **EXCLUSIVE** (`df.iloc[0:3]` includes rows 0, 1, 2).
* **Boolean Filtering:** Must use bitwise operators `&`, `|`, `~` with parentheses: `df[(df['age'] > 20) & (df['salary'] > 50000)]`.
* **`.query()`:** SQL-like string querying: `df.query("age > 20 and salary > 50000")`.

---

## 3. RELATIONAL JOINS IN PANDAS

* `pd.merge(df1, df2, on='id', how='inner')` (Default is `'inner'`).
* **Anti-Join:** `df1[~df1['key'].isin(df2['key'])]` (Rows in df1 with NO match in df2).
* **`pd.concat`:** `axis=0` stacks rows vertically; `axis=1` joins columns horizontally.

---

## 4. STATISTICAL CORRELATIONS

* **Pearson Correlation ($r$):** Linear association between continuous numeric variables. Range: **$-1.0 \le r \le +1.0$**.
* **Spearman Rank ($\rho$):** Monotonic association between ranked variables (robust to non-linear trends and outliers).
* **"Correlation Does Not Imply Causation"**: An unobserved lurking/confounding variable may drive both variables.

---

## 9. BLOOM'S TAXONOMY-ALIGNED MCQ QUESTION BANK

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    BLOOM'S REVISED TAXONOMY DISTRIBUTION                     ║
╠════════════════════════════════════╦══════════════════════╦══════════════════╣
║ Cognitive Level                    ║ Focus Area           ║ Questions        ║
╠════════════════════════════════════╬══════════════════════╬══════════════════╣
║ **L1: Remember (Knowledge)**       ║ Recall & Definitions ║ Q1 – Q8          ║
║ **L2: Understand (Comprehension)** ║ Explain & Distinguish║ Q9 – Q16         ║
║ **L3: Apply (Application)**        ║ Execute & Compute    ║ Q17 – Q26        ║
║ **L4: Analyze (Analysis)**         ║ Debug & Edge Cases   ║ Q27 – Q34        ║
║ **L5 & L6: Evaluate & Create**     ║ Judge, Design & Plan ║ Q35 – Q40        ║
╚════════════════════════════════════╩══════════════════════╩══════════════════╝
```

### 9.1 Level 1: Remember (Knowledge & Recall)

#### Question 1 [Bloom's Level: L1 - Remember]
**What is the primary purpose of Exploratory Data Analysis (EDA)?**  
A) To deploy applications on cloud servers  
B) To summarize main characteristics of data, uncover patterns, detect anomalies, and test hypotheses using visual and statistical tools  
C) To convert structured relational data into unformatted binary text  
D) To execute hardware clock cycles  
**Answer: B**  
*Explanation:* EDA is the foundational stage of data science where data is inspected through statistical metrics and visualizations to discover structures, outliers, and underlying distributions.

---

#### Question 2 [Bloom's Level: L1 - Remember]
**Which attribute of a Pandas DataFrame returns a tuple containing the number of rows and number of columns?**  
A) `df.size`  
B) `df.dimensions`  
C) `df.shape`  
D) `df.len`  
**Answer: C**  
*Explanation:* `df.shape` returns a tuple `(n_rows, n_cols)`.

---

#### Question 3 [Bloom's Level: L1 - Remember]
**What is the valid mathematical range of the Pearson Correlation Coefficient ($r$)?**  
A) $0 \le r \le 1$  
B) $-\infty < r < \infty$  
C) $-1.0 \le r \le +1.0$  
D) $-100 \le r \le +100$  
**Answer: C**  
*Explanation:* Pearson's $r$ is bounded strictly between $-1.0$ (perfect negative linear correlation) and $+1.0$ (perfect positive linear correlation).

---

#### Question 4 [Bloom's Level: L1 - Remember]
**What does `df.describe()` compute by default on a DataFrame?**  
A) Hardware CPU metrics  
B) Descriptive summary statistics (count, mean, std, min, 25%, 50%, 75%, max) for numeric columns  
C) Raw SQL table creation commands  
D) Memory addresses of columns  
**Answer: B**  
*Explanation:* `df.describe()` outputs standard summary statistics for all numerical columns.

---

#### Question 5 [Bloom's Level: L1 - Remember]
**What is the default join type in `pd.merge(df1, df2, on='key')`?**  
A) `how='outer'`  
B) `how='left'`  
C) `how='inner'`  
D) `how='cross'`  
**Answer: C**  
*Explanation:* `pd.merge()` defaults to `how='inner'`.

---

#### Question 6 [Bloom's Level: L1 - Remember]
**What type of map uses distinct color shading across predefined geographic boundaries (e.g. states or countries) to represent data values?**  
A) Scattergeo  
B) Choropleth Map  
C) Topographic Contour Map  
D) Heatmap  
**Answer: B**  
*Explanation:* A Choropleth map shades geographic polygon areas proportionally to the statistical variable being visualized.

---

#### Question 7 [Bloom's Level: L1 - Remember]
**Which open-source platform is widely used for hosting and publishing open government and organizational data catalogs?**  
A) CKAN  
B) Docker  
C) Nginx  
D) MongoDB  
**Answer: A**  
*Explanation:* CKAN (Comprehensive Knowledge Archive Network) is the leading open-source data portal platform used by data.gov and international agencies.

---

#### Question 8 [Bloom's Level: L1 - Remember]
**Which visual plot displays the five-number summary (Min, Q1, Median, Q3, Max) and shows outliers as individual dots?**  
A) Line Chart  
B) Box-and-Whisker Plot  
C) Pie Chart  
D) Step Chart  
**Answer: B**  
*Explanation:* Box plots summarize data distributions via quartiles and identify extreme points beyond the whiskers.

---

### 9.2 Level 2: Understand (Comprehension & Explanation)

#### Question 9 [Bloom's Level: L2 - Understand]
**What is the difference between `.loc[]` and `.iloc[]` in Pandas?**  
A) `.loc[]` is integer-based; `.iloc[]` is label-based  
B) `.loc[]` is label-based (with inclusive end label); `.iloc[]` is integer-position-based (with exclusive stop integer)  
C) `.loc[]` works only on rows; `.iloc[]` works only on columns  
D) There is no difference  
**Answer: B**  
*Explanation:* `.loc` looks up rows/columns by name/index label (inclusive of stop), whereas `.iloc` looks up by integer offsets from $0$ to $N-1$ (exclusive of stop).

---

#### Question 10 [Bloom's Level: L2 - Understand]
**Why does `df[df['age'] > 20 and df['salary'] < 50000]` raise an error in Pandas?**  
A) The column names are missing  
B) Standard Python keywords `and`, `or`, `not` cannot evaluate vector Series; bitwise operators `&`, `|`, `~` with parentheses are required  
C) Integers cannot be compared  
D) Salary must be positive  
**Answer: B**  
*Explanation:* Evaluating boolean logic on whole Pandas Series requires bitwise operators (`&`, `|`, `~`) enclosed in parentheses: `(df['age'] > 20) & (df['salary'] < 50000)`.

---

#### Question 11 [Bloom's Level: L2 - Understand]
**What does the Split-Apply-Combine paradigm refer to in Pandas?**  
A) Compressing files into chunks  
B) Splitting a DataFrame into groups with `groupby()`, applying an aggregation/transformation, and combining the results into a new summary structure  
C) Encrypting database tables  
D) Splitting text strings into words  
**Answer: B**  
*Explanation:* Split-Apply-Combine is the core operational philosophy of `df.groupby()`.

---

#### Question 12 [Bloom's Level: L2 - Understand]
**What is the difference between `.agg()` and `.transform()` in Pandas `groupby()`?**  
A) Both produce the same output shape  
B) `.agg()` reduces each group to a single summary row; `.transform()` computes group statistics and broadcasts them back to match the original DataFrame's row count  
C) `.transform()` works only on strings  
D) `.agg()` deletes the group index  
**Answer: B**  
*Explanation:* `.agg()` reduces data dimensions, while `.transform()` retains the original row shape and aligns group-level calculations with each individual row.

---

#### Question 13 [Bloom's Level: L2 - Understand]
**What is an Anti-Join between DataFrame A and DataFrame B?**  
A) Returns rows common to both A and B  
B) Returns all rows from A that have NO matching key in B  
C) Returns all columns except primary keys  
D) Swaps rows and columns  
**Answer: B**  
*Explanation:* An anti-join filters DataFrame A to return only records that do NOT exist in DataFrame B (`df1[~df1['key'].isin(df2['key'])]`).

---

#### Question 14 [Bloom's Level: L2 - Understand]
**What does a Pearson correlation coefficient of $r = 0.0$ indicate?**  
A) Perfect positive relationship  
B) Perfect negative relationship  
C) No linear relationship between the two variables  
D) Missing values  
**Answer: C**  
*Explanation:* $r = 0.0$ indicates zero linear association between two variables.

---

#### Question 15 [Bloom's Level: L2 - Understand]
**Why should Pie Charts be avoided when presenting data with more than 5–7 categories?**  
A) Computers cannot render colors  
B) The human visual system struggles to accurately compare subtle angles and 2D slice areas, leading to poor interpretability; bar charts are vastly superior  
C) Pie charts cannot display numeric percentages  
D) Pie charts require GPU cards  
**Answer: B**  
*Explanation:* Human perception is far more accurate at decoding 1D lengths (bars) than 2D angles and areas (pie slices).

---

#### Question 16 [Bloom's Level: L2 - Understand]
**What does `df['Department'].value_counts(normalize=True)` calculate?**  
A) Raw counts of employees per department  
B) Relative proportions / percentage frequencies (summing to 1.0) of each category  
C) Average salary per department  
D) Alphabetically sorted unique department names  
**Answer: B**  
*Explanation:* `normalize=True` divides the frequency count of each class by the total count, giving relative proportions.

---

### 9.3 Level 3: Apply (Application, Computation & Code Output)

#### Question 17 [Bloom's Level: L3 - Apply]
**Consider `df.iloc[0:4, 1:3]`. Which rows and columns are selected?**  
A) Rows 0 to 4 inclusive, Columns 1 to 3 inclusive  
B) Rows 0, 1, 2, 3 (offsets 0 to 3) and Columns 1, 2 (offsets 1 to 2)  
C) Rows 1 to 4 and Columns 1 to 3  
D) Raises an `IndexError`  
**Answer: B**  
*Explanation:* `.iloc` utilizes zero-based indexing where stop positions are exclusive (`0:4` selects rows 0, 1, 2, 3 and `1:3` selects columns 1, 2).

---

#### Question 18 [Bloom's Level: L3 - Apply]
**Consider `df.loc['A':'C']`. What is the slicing behavior on the end label `'C'`?**  
A) `'C'` is excluded  
B) `'C'` is included  
C) Raises a `KeyError`  
D) Slices randomly  
**Answer: B**  
*Explanation:* In `.loc[]`, both the start label and the stop label are **inclusive**.

---

#### Question 19 [Bloom's Level: L3 - Apply]
**How can you concatenate two DataFrames vertically (appending rows)?**  
A) `pd.concat([df1, df2], axis=0)`  
B) `pd.concat([df1, df2], axis=1)`  
C) `pd.merge([df1, df2], how='vertical')`  
D) `df1.stack(df2)`  
**Answer: A**  
*Explanation:* `pd.concat(..., axis=0)` stacks rows vertically.

---

#### Question 20 [Bloom's Level: L3 - Apply]
**How can you concatenate two DataFrames horizontally (placing columns side-by-side)?**  
A) `pd.concat([df1, df2], axis=0)`  
B) `pd.concat([df1, df2], axis=1)`  
C) `pd.append_cols(df1, df2)`  
D) `df1.join_horizontal(df2)`  
**Answer: B**  
*Explanation:* `pd.concat(..., axis=1)` aligns indices and places columns side-by-side.

---

#### Question 21 [Bloom's Level: L3 - Apply]
**What is the output of `df['score'].quantile(0.50)` for `score = [10, 20, 30, 40, 50]`?**  
A) 20  
B) 30  
C) 40  
D) 50  
**Answer: B**  
*Explanation:* The 0.50 quantile is the Median (50th percentile), which equals 30.

---

#### Question 22 [Bloom's Level: L3 - Apply]
**Which Pandas function is used to create spreadsheet-style pivot tables?**  
A) `pd.pivot_table()`  
B) `df.spread()`  
C) `pd.grid()`  
D) `df.cross_table()`  
**Answer: A**  
*Explanation:* `pd.pivot_table(df, values=..., index=..., columns=..., aggfunc=...)` generates multi-dimensional pivot summaries.

---

#### Question 23 [Bloom's Level: L3 - Apply]
**What is the role of `margins=True` in `pd.pivot_table()`?**  
A) Adds borders to the chart  
B) Adds `'All'` row and column grand totals and subtotals  
C) Removes missing values  
D) Limits memory usage  
**Answer: B**  
*Explanation:* `margins=True` adds marginal totals (`'All'`) across both axes.

---

#### Question 24 [Bloom's Level: L3 - Apply]
**Which Pandas function computes frequency contingency tables between two categorical columns?**  
A) `pd.crosstab()`  
B) `df.freq_table()`  
C) `pd.contingency()`  
D) `df.count_pairs()`  
**Answer: A**  
*Explanation:* `pd.crosstab(df['cat1'], df['cat2'])` computes frequency cross-tabulations.

---

#### Question 25 [Bloom's Level: L3 - Apply]
**Consider `df.sort_values(by=['Dept', 'Salary'], ascending=[True, False])`. How is the output ordered?**  
A) Dept Descending, Salary Ascending  
B) Dept Ascending (A-Z), Salary Descending (Highest to Lowest)  
C) Both Ascending  
D) Both Descending  
**Answer: B**  
*Explanation:* The `ascending` list `[True, False]` sorts `Dept` alphabetically A-Z and `Salary` from highest to lowest within each department.

---

#### Question 26 [Bloom's Level: L3 - Apply]
**What does `df.sample(frac=0.25, random_state=42)` do?**  
A) Takes the first 25 rows  
B) Randomly extracts a reproducible 25% sample of all rows in the DataFrame  
C) Deletes 25% of columns  
D) Fills 25% of NaNs  
**Answer: B**  
*Explanation:* `frac=0.25` selects 25% of rows randomly; `random_state=42` ensures reproducible output.

---

### 9.4 Level 4: Analyze (Analysis, Logic & Bug Detection)

#### Question 27 [Bloom's Level: L4 - Analyze]
**Analyze what a correlation coefficient of $r = -0.92$ between Product Price and Sales Volume signifies:**  
A) Weak positive relationship  
B) Strong inverse (negative) linear relationship (as Price increases, Sales Volume decreases strongly)  
C) Data entry error  
D) No relationship  
**Answer: B**  
*Explanation:* An $r$ of $-0.92$ indicates a powerful negative linear correlation.

---

#### Question 28 [Bloom's Level: L4 - Analyze]
**Compare Pearson's $r$ and Spearman's $\rho$ on a dataset with a monotonic, non-linear exponential relationship ($Y = e^X$) and severe outliers. Why is Spearman's $\rho$ close to 1.0 while Pearson's $r$ is significantly lower?**  
A) Pearson's formula is broken  
B) Pearson evaluates strictly linear relationships and is sensitive to outliers; Spearman evaluates rank order monotonicity, which is perfectly preserved in exponential growth  
C) Spearman only works on integers  
D) Pearson cannot handle positive numbers  
**Answer: B**  
*Explanation:* Monotonic transformations preserve rank orders perfectly ($\rho = 1.0$), while non-linear curvature degrades the Pearson linear correlation coefficient $r$.

---

#### Question 29 [Bloom's Level: L4 - Analyze]
**Analyze why `pd.merge(customers, orders, on='cust_id', how='inner')` produces MORE rows than `customers` when a customer has placed multiple orders:**  
A) It is a bug in Pandas  
B) An inner join duplicates matching left rows for every corresponding match in the right table (1-to-many relationship)  
C) It creates null rows  
D) It converts to an outer join  
**Answer: B**  
*Explanation:* In relational joins, a 1-to-many relationship multiplies the parent row for every matching child record in the right table.

---

#### Question 30 [Bloom's Level: L4 - Analyze]
**What happens if you execute `df.reset_index(drop=True)` after filtering rows?**  
A) The DataFrame is erased  
B) The row index is reset to clean 0-based consecutive integers, and the old non-consecutive index is discarded  
C) Column names are converted to numbers  
D) An exception is raised  
**Answer: B**  
*Explanation:* `reset_index(drop=True)` re-indexes rows sequentially from 0 and drops the old index.

---

#### Question 31 [Bloom's Level: L4 - Analyze]
**Why does `df.describe(include='all')` show `NaN` for `mean` and `std` on string columns?**  
A) String columns have missing values  
B) Arithmetic mean and standard deviation cannot be calculated on qualitative text data  
C) Pandas failed to load strings  
D) The strings must be encrypted  
**Answer: B**  
*Explanation:* Numerical metrics (`mean`, `std`) are mathematically undefined for categorical strings, so Pandas populates those summary cells with `NaN`.

---

#### Question 32 [Bloom's Level: L4 - Analyze]
**A researcher discovers a high positive correlation ($r = 0.85$) between ice cream sales and shark attacks. What explains this phenomenon?**  
A) Ice cream attracts sharks directly  
B) Confounding/Lurking variable effect: Warm summer weather causes both ice cream sales and beach swimming to rise simultaneously; correlation does not imply causation  
C) Measurement fraud  
D) Random coincidence  
**Answer: B**  
*Explanation:* This is a classic spurious correlation driven by a lurking variable (summer temperature).

---

#### Question 33 [Bloom's Level: L4 - Analyze]
**Which Pandas method provides the cleanest string expression interface for filtering without repeating `df['col']`?**  
A) `df.query()`  
B) `df.filter_rows()`  
C) `df.where_sql()`  
D) `df.extract()`  
**Answer: A**  
*Explanation:* `df.query("age >= 25 and department == 'AI'")` evaluates concise filter strings.

---

#### Question 34 [Bloom's Level: L4 - Analyze]
**Analyze the difference between `df.drop(columns=['id'])` and `df.drop(['id'], axis=0)`:**  
A) `columns=['id']` (or `axis=1`) drops the column named `'id'`; `axis=0` attempts to drop a row with index label `'id'`  
B) Both drop the column  
C) Both drop the row  
D) `axis=0` is invalid  
**Answer: A**  
*Explanation:* In Pandas, `axis=1` refers to columns and `axis=0` refers to rows/index labels.

---

### 9.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)

#### Question 35 [Bloom's Level: L5 - Evaluate]
**Evaluate the choice of visualization: An executive needs to analyze monthly patient admissions across 12 months to spot seasonal peaks and project future hospital bed requirements. Which visual encoding is optimal?**  
A) Pie Chart  
B) Line Chart / Graph  
C) Scatter Plot  
D) Treemap  
**Answer: B**  
*Explanation:* Line charts are optimal for continuous time-series trajectories, clearly highlighting trends, seasonal cycles, and inflection points over sequential months.

---

#### Question 36 [Bloom's Level: L5 - Evaluate]
**Evaluate which chart type is most appropriate for displaying the correlation heatmap of 15 numerical features in a machine learning dataset:**  
A) 15 separate Pie Charts  
B) A 2D Correlation Heatmap with a diverging colormap (`'coolwarm'`) and annotated correlation coefficients  
C) A 3D Bar Chart  
D) A Word Cloud  
**Answer: B**  
*Explanation:* A correlation heatmap provides a clean, comprehensive 2D matrix overview of all pairwise linear relationships simultaneously.

---

#### Question 37 [Bloom's Level: L6 - Create]
**Design a Pandas pipeline that groups an employee DataFrame by department and computes the employee count, mean salary, and maximum experience:**  
A)
```python
summary = df.groupby('department').agg(
    total_employees=('employee_id', 'count'),
    mean_salary=('salary', 'mean'),
    max_experience=('experience', 'max')
)
```
B)
```python
summary = df.groupby('department')['salary'].mean()
```
C)
```python
summary = df.pivot('department')
```
D)
```python
summary = df.describe()
```
**Answer: A**  
*Explanation:* Option A uses named aggregations in `.agg()` to compute distinct statistical metrics across multiple columns in a single, clean operation.

---

#### Question 38 [Bloom's Level: L6 - Create]
**Which Python expression creates an Anti-Join to identify all registered students who have NOT enrolled in any course?**  
A) `unregistered = students[~students['student_id'].isin(enrollments['student_id'])]`  
B) `unregistered = pd.merge(students, enrollments, on='student_id')`  
C) `unregistered = students.join(enrollments)`  
D) `unregistered = students.dropna()`  
**Answer: A**  
*Explanation:* Negating membership with `~...isin()` filters students whose ID is absent from the `enrollments` table (anti-join).

---

#### Question 39 [Bloom's Level: L5 - Evaluate]
**Evaluate which interactive framework is best suited for building web-based data dashboards in pure Python without writing HTML/JavaScript:**  
A) Postman  
B) Streamlit / Dash  
C) Matplotlib core  
D) SQLite  
**Answer: B**  
*Explanation:* Streamlit and Dash allow data scientists to build interactive, web-based analytical dashboards and data apps entirely in Python.

---

#### Question 40 [Bloom's Level: L6 - Create]
**Design a cross-tabulation query to compute row-wise percentage distribution of patient diagnosis categories across age brackets:**  
A) `pd.crosstab(df['age_bracket'], df['diagnosis'], normalize='index') * 100`  
B) `df.groupby('age_bracket').count()`  
C) `df.pivot('age_bracket', 'diagnosis')`  
D) `pd.merge(df['age_bracket'], df['diagnosis'])`  
**Answer: A**  
*Explanation:* `pd.crosstab` with `normalize='index'` computes conditional row proportions summing to 1.0 (multiplied by 100 for percentages).
