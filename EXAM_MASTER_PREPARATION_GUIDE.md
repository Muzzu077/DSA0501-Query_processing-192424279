# 🎯 MASTER EXAM PREPARATION GUIDE & QUICK REVISION CHEAT SHEET
**Course Code & Title:** DSA05 / DSA0501 – Query Processing for Data Science  
**Exam Format:** 180 Multiple-Choice Questions (MCQ Pattern)  
**Assessment Framework:** Bloom's Revised Taxonomy (Levels L1 to L6)  
**Target Score:** 100% Mastery across All 5 Units / Course Outcomes (CO1 – CO5)  

---

## 🧠 BLOOM'S TAXONOMY FRAMEWORK FOR THE EXAM
Your 180-question exam will test various cognitive levels across all 5 units:

| Bloom's Cognitive Level | Question Characteristics & Verbs | Typical Exam Question Format |
| :---: | :--- | :--- |
| **L1: Remember** (Knowledge) | Define, List, Identify, Recall, Name, State | Syntax rules, default ports, formulas, return types, library names |
| **L2: Understand** (Comprehension) | Explain, Distinguish, Compare, Interpret, Summarize | Why a function works, difference between methods, statistical interpretations |
| **L3: Apply** (Application) | Compute, Calculate, Execute, Implement, Predict Output | Tracing Python/SQL code snippets, calculating IQR bounds, writing regex |
| **L4: Analyze** (Analysis) | Differentiate, Debug, Diagnose, Find Errors, Deconstruct | Identifying why a query/transaction failed, diagnosing edge cases, join duplicates |
| **L5: Evaluate** (Evaluation) | Judge, Justify, Assess, Select Optimal Strategy | Choosing best imputation/visualization/database for complex real-world scenarios |
| **L6: Create** (Synthesis) | Design, Construct, Formulate, Develop | Designing end-to-end cleaning pipelines, multi-metric queries, dashboard layouts |

---

## 📚 UNIT-WISE STUDY GUIDES DIRECTORY (BLOOM'S ALIGNED)

| Unit / CO | Topic Title | Focus Areas | Dedicated Study Guide Link |
| :---: | :--- | :--- | :--- |
| **Unit 1 (CO1)** | **Data Wrangling & Machine-Readable Data** | Ingestion, 6-Step Lifecycle, CSV (`DictReader`/`writer`), JSON (`load`/`loads`/`dump`/`dumps`), XML (`ElementTree`), Database Schemas | [📖 `UNIT_1_DATA_WRANGLING.md`](./UNIT_1_DATA_WRANGLING.md) |
| **Unit 2 (CO2)** | **Python SQL Libraries & Database Operations** | SQLite (`sqlite3`), MySQL (`mysql.connector`), PostgreSQL (`psycopg2`), CRUD Operations, Cursors, Transactions, Placeholders (`?` vs `%s`), Joins | [📖 `UNIT_2_PYTHON_SQL_LIBRARIES.md`](./UNIT_2_PYTHON_SQL_LIBRARIES.md) |
| **Unit 3 (CO3)** | **Data Cleanup & Preprocessing** | Missing Data (MCAR/MAR/MNAR), Imputation, Type Coercion (`errors='coerce'`), Outliers (Tukey's IQR & Z-score), Fuzzy Matching (`fuzzywuzzy`), RegEx (`re` module), Normalization (Min-Max & Z-Score) | [📖 `UNIT_3_DATA_CLEANUP.md`](./UNIT_3_DATA_CLEANUP.md) |
| **Unit 4 (CO4)** | **Data Exploration and Analysis (EDA)** | Ingestion, Slicing (`.loc` vs `.iloc`), Querying, Merges & Anti-Joins, Pearson/Spearman Correlations ($[-1, +1]$), `groupby()`, Pivot Tables, Visual Encodings & Publishing | [📖 `UNIT_4_DATA_EXPLORATION_AND_ANALYSIS.md`](./UNIT_4_DATA_EXPLORATION_AND_ANALYSIS.md) |
| **Unit 5 (CO5)** | **Visualizing Data with Pandas & Matplotlib** | 3-Layer Architecture (Backend, Artist, Scripting), OO API (`fig, ax`), Plot Customization, Pandas `plot()`, `pandas.plotting` (`scatter_matrix`, `lag_plot`, `autocorrelation_plot`, `bootstrap_plot`) | [📖 `UNIT_5_VISUALIZING_DATA_WITH_PANDAS_AND_MATPLOTLIB.md`](./UNIT_5_VISUALIZING_DATA_WITH_PANDAS_AND_MATPLOTLIB.md) |

---

## ⚡ 10-MINUTE QUICK REVISION FORMULA & SYNTAX CHEAT SHEET

### 1. Mathematical & Statistical Formulas (L1 – L3)
* **Tukey's Interquartile Range (IQR) Outlier Rules:**
  * $\text{IQR} = Q3 - Q1$
  * $\text{Lower Fence} = Q1 - 1.5 \times \text{IQR}$
  * $\text{Upper Fence} = Q3 + 1.5 \times \text{IQR}$
  * $\text{Extreme Outliers} = < Q1 - 3 \times \text{IQR} \quad \text{or} \quad > Q3 + 3 \times \text{IQR}$
* **Z-Score (Standard Score):**
  * $Z = \frac{X - \mu}{\sigma}$ (Outlier if $|Z| > 3$)
* **Min-Max Feature Scaling (Range $[0, 1]$):**
  * $X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$
* **Pearson Linear Correlation Coefficient ($r$):**
  * Range: $-1.0 \le r \le +1.0$ ($+1.0$ perfect positive, $-1.0$ perfect negative, $0.0$ no linear correlation)

---

### 2. High-Yield Python & Library Syntax Summary

#### File Handling & Serialization (Unit 1)
* **JSON Module Rules:**
  * `json.loads(str)`: String ➔ Python Dict/List.
  * `json.load(fp)`: File Pointer ➔ Python Dict/List.
  * `json.dumps(obj)`: Python Dict/List ➔ JSON String.
  * `json.dump(obj, fp)`: Python Dict/List ➔ Written to File.
  * *Trap:* JSON keys & strings **must** use double quotes (`"key": "val"`). Booleans are `true`/`false`; null is `null`.
* **CSV Module Rules:**
  * `csv.writer(f)`: Always open file with `newline=''` to avoid blank lines on Windows.
  * `csv.DictReader(f)`: Reads first row as fieldnames, yields each row as a dictionary.
* **XML (`xml.etree.ElementTree as ET`):**
  * `tree = ET.parse('file.xml'); root = tree.getroot()`
  * `elem.tag` (Tag string), `elem.attrib` (Dict of attributes), `elem.text` (Inner text).
  * `.find('tag')` (First direct child), `.findall('tag')` (List of direct children), `.iter('tag')` (Recursive search all depths).

#### SQL Databases & CRUD (Unit 2)
* **Connection Strings:**
  * SQLite: `sqlite3.connect('app.db')` or `sqlite3.connect(':memory:')` (RAM-based).
  * MySQL: `mysql.connector.connect(host='...', user='...', password='...', database='...', port=3306)`
  * PostgreSQL: `psycopg2.connect(dbname='...', user='...', password='...', host='...', port=5432)`
* **Parameter Placeholders (Prevent SQL Injection):**
  * SQLite uses: **`?`** (`cursor.execute("INSERT INTO t VALUES (?, ?)", (v1, v2))`)
  * MySQL & PostgreSQL use: **`%s`** (`cursor.execute("INSERT INTO t VALUES (%s, %s)", (v1, v2))`)
* **Commits:**
  * `conn.commit()` is **strictly required** to persist `INSERT`, `UPDATE`, `DELETE` to disk!
* **Fetching Rows:**
  * `cursor.fetchone()` ➔ Returns single `tuple` or `None`.
  * `cursor.fetchall()` ➔ Returns `list` of `tuples` (empty `[]` if no rows match).

#### Data Cleaning & Preprocessing (Unit 3)
* **Type Coercion:**
  * `pd.to_numeric(df['col'], errors='coerce')`: Non-numbers become `NaN`; dtype upcasts to `float64`.
* **Missing Value Imputation:**
  * Skewed data / Outliers present ➔ Impute with **Median**.
  * Normal / Symmetric data ➔ Impute with **Mean**.
  * Categorical ➔ Impute with **Mode** or `'Unknown'`.
  * Time series ➔ `df.ffill()` (forward fill) or `df.bfill()` (backward fill).
* **Fuzzy String Matching (`fuzzywuzzy.fuzz`):**
  * `fuzz.ratio`: Standard Levenshtein edit distance.
  * `fuzz.partial_ratio`: Substring matching (e.g. "Apple" in "Apple Inc.").
  * `fuzz.token_sort_ratio`: Word-order independent ("John Smith" vs "Smith, John" ➔ 100).
  * `fuzz.token_set_ratio`: Duplicate word & length independent ("Google" vs "Google Google Inc" ➔ 100).
* **RegEx (`import re`):**
  * `re.match()`: Checks only start of string.
  * `re.search()`: Scans entire string for first match.
  * `re.findall()`: Returns list of all matching substrings.
  * `re.sub(r'[^a-zA-Z0-9\s]', '', text)`: Strips non-alphanumerics.

#### Advanced Exploratory Analysis & Joins (Unit 4)
* **`.loc` vs `.iloc`:**
  * `.loc['A':'C']`: Label-based, **INCLUSIVE** of end label `'C'`.
  * `.iloc[0:3]`: Integer-based, **EXCLUSIVE** of stop integer `3` (returns indices 0, 1, 2).
* **Boolean Filtering in Pandas:**
  * Must use bitwise operators `&`, `|`, `~` with parentheses around each condition: `(df['age'] > 18) & (df['cgpa'] >= 8.0)`.
* **Pandas Joins (`pd.merge`):**
  * Default `how='inner'`.
  * Anti-Join: `df1[~df1['key'].isin(df2['key'])]`.
* **Groupby vs Transform:**
  * `df.groupby('dept')['salary'].agg('mean')`: Collapses to 1 row per department.
  * `df.groupby('dept')['salary'].transform('mean')`: Broadcasts group mean back to all original rows.

#### Diagnostic Visualizations (Unit 5)
* **Architecture:** Backend Layer (Output rendering) ➔ Artist Layer (All visual canvas objects) ➔ Scripting Layer (`pyplot`).
* **Object-Oriented Idiom:** `fig, ax = plt.subplots(figsize=(8, 5))`
* **`pandas.plotting` Special Charts:**
  1. `scatter_matrix(df, diagonal='kde')`: Pairwise scatter plots; diagonal shows univariate KDE or Hist.
  2. `lag_plot(series, lag=1)`:
     * **Shapeless / Circular Cloud** ➔ **Random Noise** (No autocorrelation).
     * **Diagonal Line ($y = x$)** ➔ **Strong Positive Autocorrelation**.
  3. `autocorrelation_plot(series)`: Plots autocorrelation across lags. Points crossing horizontal dashed bands indicate **statistically significant seasonality / trend** ($p < 0.05$).
  4. `bootstrap_plot(series, size=50, samples=500)`: Evaluates sampling uncertainty for **Mean**, **Median**, and **Midrange** via repeated resampling with replacement.

---

## 💡 EXAM TIME MANAGEMENT & STRATEGY (180 QUESTIONS)
1. **Pacing:** 180 questions in 180 minutes = **1 minute per question**.
2. **First Pass (L1 & L2 Questions):** Answer rapid-fire definitions, syntax, and conceptual differences in 20-30 seconds each to bank time.
3. **Second Pass (L3 & L4 Questions):** Execute IQR calculations, code tracing, and regex replacements in 1 minute each.
4. **Third Pass (L5 & L6 Scenario Questions):** Carefully analyze system trade-offs, architecture decisions, and multi-step pipeline designs.
