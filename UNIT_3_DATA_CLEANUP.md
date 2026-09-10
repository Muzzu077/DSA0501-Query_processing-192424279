# UNIT 3: DATA CLEANUP & PREPROCESSING (CO3)
**Course:** DSA05 / DSA0501 – Query Processing for Data Science  
**Target:** 180-Question MCQ Exam Preparation & Comprehensive Concept Mastery  
**Assessment Framework:** Bloom's Revised Taxonomy (Levels L1 to L6)

---

## 📌 TABLE OF CONTENTS
1. [Core Concepts of Data Quality & Cleanup](#1-core-concepts-of-data-quality--cleanup)
   - 1.1 Why Clean Data? The GIGO Principle
   - 1.2 The 6 Dimensions of Data Quality
   - 1.3 Missing Data Mechanisms (MCAR, MAR, MNAR)
2. [Handling Missing Values & Type Coercion](#2-handling-missing-values--type-coercion)
   - 2.1 Detection (`isnull`, `isna`, `info`, `describe`)
   - 2.2 Deletion Strategies (`dropna`)
   - 2.3 Imputation Techniques (Mean, Median, Mode, `ffill`, `bfill`, `interpolate`)
   - 2.4 Type Coercion (`pd.to_numeric`, `pd.to_datetime`, `errors='coerce'`)
3. [Outlier & Anomaly Detection](#3-outlier--anomaly-detection)
   - 3.1 Tukey's Interquartile Range (IQR) Method & Formulas
   - 3.2 Z-Score / Standard Score (3-Sigma Rule)
   - 3.3 Domain Validation & Rule-Based Boundaries
4. [Duplicate Detection & Record Linkage](#4-duplicate-detection--record-linkage)
   - 4.1 `duplicated()` Parameters (`first`, `last`, `False`)
   - 4.2 `drop_duplicates()` Operations
5. [Fuzzy String Matching & Distance Metrics](#5-fuzzy-string-matching--distance-metrics)
   - 5.1 Levenshtein Distance Theory
   - 5.2 `fuzzywuzzy` Functions (`ratio`, `partial_ratio`, `token_sort_ratio`, `token_set_ratio`)
   - 5.3 Best Match Extraction (`process.extract`, `process.extractOne`)
6. [Regular Expressions (RegEx) for Data Wrangling](#6-regular-expressions-regex-for-data-wrangling)
   - 6.1 Python `re` Module (`match`, `search`, `findall`, `finditer`, `sub`, `split`)
   - 6.2 Metacharacters, Quantifiers, and Special Character Classes
   - 6.3 Standard Cleanup Patterns (Emails, Phone Numbers, Dates, Alphanumerics)
7. [Data Normalization & Standardization](#7-data-normalization--standardization)
   - 7.1 Min-Max Normalization (Formula & Scaling to $[0, 1]$)
   - 7.2 Z-Score Standardization (Formula, Mean $= 0$, Variance $= 1$)
   - 7.3 Categorical Encoding (`pd.get_dummies`)
8. [Scripting Automated Cleanup Pipelines & Exporting](#8-scripting-automated-cleanup-pipelines--exporting)
9. [High-Yield Exam Tips & Common MCQ Traps](#9-high-yield-exam-tips--common-mcq-traps)
10. [Bloom's Taxonomy-Aligned MCQ Question Bank (40+ Questions)](#10-blooms-taxonomy-aligned-mcq-question-bank)
   - [10.1 Level 1: Remember (Knowledge & Recall)](#101-level-1-remember-knowledge--recall)
   - [10.2 Level 2: Understand (Comprehension & Explanation)](#102-level-2-understand-comprehension--explanation)
   - [10.3 Level 3: Apply (Application, Computation & Code Output)](#103-level-3-apply-application-computation--code-output)
   - [10.4 Level 4: Analyze (Analysis, Logic & Bug Detection)](#104-level-4-analyze-analysis-logic--bug-detection)
   - [10.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)](#105-level-5--6-evaluate--create-judgment-architecture--design)

---

## 1. CORE CONCEPTS OF DATA QUALITY & CLEANUP

### 1.1 Why Clean Data? The GIGO Principle
* **Garbage In, Garbage Out (GIGO):** Faulty input data produces faulty predictions and invalid business analytics.
* **The 6 Dimensions of Data Quality:** Accuracy, Completeness, Consistency, Timeliness, Validity, and Uniqueness.

### 1.2 Missing Data Mechanisms
* **MCAR (Missing Completely at Random):** Missingness is completely independent of observed and unobserved data.
* **MAR (Missing at Random):** Missingness is related to observed variables, but not the missing value itself.
* **MNAR (Missing Not at Random):** Missingness depends directly on the unobserved value itself.

---

## 2. HANDLING MISSING VALUES & TYPE COERCION

```python
# Total missing per column
df.isnull().sum()

# Coerce non-numbers to NaN (column becomes float64)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Imputation
df['Salary'] = df['Salary'].fillna(df['Salary'].median())  # Skewed data with outliers
df['Name'] = df['Name'].fillna('Unknown')                  # Categorical
df['Stock'] = df['Stock'].ffill()                          # Time-series forward fill
```

---

## 3. OUTLIER DETECTION FORMULAS

$$\text{IQR} = Q3 - Q1$$
$$\text{Lower Bound / Fence} = Q1 - (1.5 \times \text{IQR})$$
$$\text{Upper Bound / Fence} = Q3 + (1.5 \times \text{IQR})$$
$$\text{Extreme Outlier Fences} = Q1 - 3 \times \text{IQR} \quad \text{and} \quad Q3 + 3 \times \text{IQR}$$
$$\text{Z-Score} = \frac{X - \mu}{\sigma} \quad (\text{Outlier if } |Z| > 3)$$

---

## 4. FUZZY MATCHING SCORING FUNCTIONS (`fuzzywuzzy`)

* `fuzz.ratio(s1, s2)`: Standard Levenshtein edit distance ratio.
* `fuzz.partial_ratio(s1, s2)`: Substring matching.
* `fuzz.token_sort_ratio(s1, s2)`: Sorts tokens alphabetically before matching (handles out-of-order words: `"John Smith"` vs `"Smith John"` ➔ `100`).
* `fuzz.token_set_ratio(s1, s2)`: Matches intersection and remainder tokens (handles duplicate words and different lengths: `"Google"` vs `"Google Inc"` ➔ `100`).

---

## 5. REGULAR EXPRESSIONS (`import re`)

* `re.sub(r'[^a-zA-Z0-9\s]', '', text)`: Strips non-alphanumeric special characters.
* `re.sub(r'\D', '', phone)`: Strips all non-digit characters.
* `re.findall(pattern, text)`: Extracts all non-overlapping matches as a list.
* `re.match()` (Start of string) vs `re.search()` (Anywhere in string).

---

## 6. NORMALIZATION & STANDARDIZATION

* **Min-Max Normalization (Range $[0, 1]$):**
  $$X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$$
* **Z-Score Standardization (Mean $= 0$, Std $= 1$):**
  $$Z = \frac{X - \mu}{\sigma}$$

---

## 10. BLOOM'S TAXONOMY-ALIGNED MCQ QUESTION BANK

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

### 10.1 Level 1: Remember (Knowledge & Recall)

#### Question 1 [Bloom's Level: L1 - Remember]
**What is the formula for calculating the Interquartile Range (IQR)?**  
A) $Q3 + Q1$  
B) $(Q3 - Q1) / 2$  
C) $Q3 - Q1$  
D) $Q1 - 1.5 \times Q3$  
**Answer: C**  
*Explanation:* $\text{IQR} = Q3 - Q1$, where $Q3$ is the 75th percentile and $Q1$ is the 25th percentile.

---

#### Question 2 [Bloom's Level: L1 - Remember]
**In Tukey's IQR outlier detection method, what is the formula for the Upper Bound (Upper Fence)?**  
A) $Q3 + 1.5 \times \text{IQR}$  
B) $Q1 + 1.5 \times \text{IQR}$  
C) $Q3 - 1.5 \times \text{IQR}$  
D) $Q3 + 3.0 \times \text{IQR}$  
**Answer: A**  
*Explanation:* Upper Fence $= Q3 + (1.5 \times \text{IQR})$.

---

#### Question 3 [Bloom's Level: L1 - Remember]
**In Tukey's method, what is the formula for the Lower Bound (Lower Fence)?**  
A) $Q1 - 1.5 \times \text{IQR}$  
B) $Q3 - 1.5 \times \text{IQR}$  
C) $Q1 + 1.5 \times \text{IQR}$  
D) $\text{Median} - 1.5 \times \text{IQR}$  
**Answer: A**  
*Explanation:* Lower Fence $= Q1 - (1.5 \times \text{IQR})$.

---

#### Question 4 [Bloom's Level: L1 - Remember]
**What is the mathematical definition of Levenshtein Distance?**  
A) The Euclidean distance between coordinates  
B) The minimum number of single-character insertions, deletions, or substitutions required to transform one string into another  
C) The number of shared words between two sentences  
D) The cosine angle between two text vectors  
**Answer: B**  
*Explanation:* Levenshtein distance is an edit-distance metric counting the minimum single-character insertions, deletions, and substitutions to morph string A into string B.

---

#### Question 5 [Bloom's Level: L1 - Remember]
**Under standard statistical Z-score outlier detection, a data point is flagged as an outlier if its absolute Z-score exceeds what threshold?**  
A) $|Z| > 1$  
B) $|Z| > 2$  
C) $|Z| > 3$  
D) $|Z| < 0$  
**Answer: C**  
*Explanation:* Under the empirical 3-sigma rule for normal distributions, values with $|Z| > 3$ are considered statistical outliers ($> 3\sigma$ from the mean).

---

#### Question 6 [Bloom's Level: L1 - Remember]
**What does the regex character class `\d` match in Python?**  
A) Any letter  
B) Any whitespace  
C) Any digit from 0 to 9 (`[0-9]`)  
D) Any punctuation character  
**Answer: C**  
*Explanation:* `\d` represents any single digit `[0-9]`. `\D` represents any non-digit.

---

#### Question 7 [Bloom's Level: L1 - Remember]
**What is the formula for Min-Max Feature Normalization to scale values into $[0, 1]$?**  
A) $(X - \mu) / \sigma$  
B) $(X - X_{\min}) / (X_{\max} - X_{\min})$  
C) $(X - \text{Median}) / \text{IQR}$  
D) $X / \text{Mean}(X)$  
**Answer: B**  
*Explanation:* $X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$.

---

#### Question 8 [Bloom's Level: L1 - Remember]
**Which dimension of data quality is violated when a person's age is recorded as `-25`?**  
A) Timeliness  
B) Validity  
C) Completeness  
D) Uniqueness  
**Answer: B**  
*Explanation:* Validity measures adherence to domain rules and acceptable ranges. A negative age violates domain validity.

---

### 10.2 Level 2: Understand (Comprehension & Explanation)

#### Question 9 [Bloom's Level: L2 - Understand]
**Why does a Pandas integer column automatically change its data type to `float64` after `pd.to_numeric(..., errors='coerce')` introduces `NaN` values?**  
A) Floats take less memory than integers  
B) Standard Pandas numeric arrays use IEEE 754 floating-point representation for `numpy.nan`  
C) It is a bug in the CPython interpreter  
D) Python does not support integer data types  
**Answer: B**  
*Explanation:* In standard Pandas, `NaN` is represented as a floating-point value. An integer column containing `NaN` is upcast to `float64`.

---

#### Question 10 [Bloom's Level: L2 - Understand]
**When imputing missing values in a numerical column with severe positive skewness and extreme outliers, why is Median preferred over Mean?**  
A) Median is faster to calculate  
B) The Mean is heavily pulled by extreme outliers, whereas the Median is a non-parametric, robust measure of central tendency  
C) Mean cannot be computed on floats  
D) Median eliminates negative numbers  
**Answer: B**  
*Explanation:* The mean is sensitive to extreme values, while the median represents the 50th percentile and remains stable despite severe outliers.

---

#### Question 11 [Bloom's Level: L2 - Understand]
**In Python's `re` module, what is the functional difference between `re.match()` and `re.search()`?**  
A) `re.match()` works only on numbers; `re.search()` works on text  
B) `re.match()` checks for a match only at the beginning (index 0) of the string; `re.search()` scans the entire string for the first match  
C) `re.match()` returns a list of all matches  
D) There is no difference  
**Answer: B**  
*Explanation:* `re.match()` anchors strictly at the start of the string, while `re.search()` searches through the entire string.

---

#### Question 12 [Bloom's Level: L2 - Understand]
**What is the difference between `fuzz.ratio` and `fuzz.token_sort_ratio` in `fuzzywuzzy`?**  
A) `fuzz.ratio` is faster  
B) `fuzz.ratio` is sensitive to word order, while `fuzz.token_sort_ratio` tokenizes and sorts words alphabetically before comparing, scoring 100 on out-of-order words  
C) `fuzz.token_sort_ratio` works only on numbers  
D) There is no difference  
**Answer: B**  
*Explanation:* For `"John Smith"` vs `"Smith John"`, `fuzz.ratio` gives a low score, but `fuzz.token_sort_ratio` gives 100 because sorted tokens are identical.

---

#### Question 13 [Bloom's Level: L2 - Understand]
**What does `df.duplicated(subset=['email'], keep=False)` do compared to `keep='first'`?**  
A) Marks only the first duplicate as `True`  
B) Marks ALL occurrences of duplicate rows as `True`, allowing inspection of every conflicting record  
C) Deletes duplicates immediately  
D) Raises an exception  
**Answer: B**  
*Explanation:* `keep=False` flags every duplicate instance as `True`, whereas `keep='first'` flags only subsequent occurrences after the first.

---

#### Question 14 [Bloom's Level: L2 - Understand]
**What happens to data mean and standard deviation after applying Z-score standardization?**  
A) $\text{Mean} = 1, \text{Std} = 0$  
B) $\text{Mean} = 0, \text{Std} = 1$  
C) $\text{Mean} = 100, \text{Std} = 15$  
D) $\text{Mean} = 0, \text{Std} = 0$  
**Answer: B**  
*Explanation:* Z-score standardization centers the distribution at mean 0 and scales standard deviation to 1.

---

#### Question 15 [Bloom's Level: L2 - Understand]
**If data is Missing Completely at Random (MCAR), what does this imply?**  
A) Missingness depends on the unobserved value itself  
B) Missingness is completely independent of both observed and unobserved data  
C) Missingness is predictable based on gender  
D) The entire column is corrupted  
**Answer: B**  
*Explanation:* MCAR means missingness occurs purely at random without dependency on any variable in the dataset.

---

#### Question 16 [Bloom's Level: L2 - Understand]
**What does `df.dropna(how='all')` do?**  
A) Drops a row if any column is NaN  
B) Drops a row ONLY if EVERY column in that row is NaN  
C) Drops all rows in the DataFrame  
D) Drops all columns  
**Answer: B**  
*Explanation:* `how='all'` requires all values in the row to be `NaN` before dropping it.

---

### 10.3 Level 3: Apply (Application, Computation & Code Output)

#### Question 17 [Bloom's Level: L3 - Apply]
**Given a dataset where $Q1 = 200$ and $Q3 = 300$, what is the upper outlier cutoff threshold using Tukey's $1.5 \times \text{IQR}$ rule?**  
A) 400  
B) 450  
C) 500  
D) 350  
**Answer: B**  
*Explanation:* $\text{IQR} = 300 - 200 = 100$. $\text{Upper Bound} = Q3 + 1.5 \times \text{IQR} = 300 + (1.5 \times 100) = 450$.

---

#### Question 18 [Bloom's Level: L3 - Apply]
**What is the Levenshtein edit distance between `"cat"` and `"hat"`?**  
A) 0  
B) 1  
C) 2  
D) 3  
**Answer: B**  
*Explanation:* A single character substitution (`'c'` ➔ `'h'`) converts `"cat"` to `"hat"`, yielding an edit distance of 1.

---

#### Question 19 [Bloom's Level: L3 - Apply]
**What will be the output of `re.sub(r'\D', '', 'Order ID: #98401-2026')`?**  
A) `'Order ID: #98401-2026'`  
B) `'984012026'`  
C) `'Order ID'`  
D) `'#'`  
**Answer: B**  
*Explanation:* `\D` matches all non-digit characters. `re.sub` strips letters, spaces, colons, hashes, and hyphens, leaving only the digits `'984012026'`.

---

#### Question 20 [Bloom's Level: L3 - Apply]
**What is the output of the following Pandas code?**
```python
import pandas as pd
df = pd.DataFrame({'date': ['2025-01-15', '2025-06-20']})
df['date'] = pd.to_datetime(df['date'])
print(df['date'].dt.month_name().tolist())
```
A) `[1, 6]`  
B) `['January', 'June']`  
C) `['Jan', 'Jun']`  
D) `['2025-01', '2025-06']`  
**Answer: B**  
*Explanation:* `.dt.month_name()` extracts full English month names from `datetime64` objects.

---

#### Question 21 [Bloom's Level: L3 - Apply]
**What is the output of `re.findall(r'\b[A-Z]\w+', 'Saveetha School of Engineering')`?**  
A) `['Saveetha', 'School', 'Engineering']`  
B) `['Saveetha']`  
C) `['of']`  
D) `['S', 'S', 'E']`  
**Answer: A**  
*Explanation:* `\b[A-Z]\w+` matches words starting with an uppercase letter. `'of'` is skipped because it starts with lowercase `'o'`.

---

#### Question 22 [Bloom's Level: L3 - Apply]
**What is returned by `process.extractOne("Banglore", ["Chennai", "Bangalore", "Delhi"])`?**  
A) Just the string `'Bangalore'`  
B) A tuple containing the best match and score: `('Bangalore', score)`  
C) A list of all choices  
D) An integer  
**Answer: B**  
*Explanation:* `process.extractOne()` returns a 2-tuple `(matched_string, similarity_score)`.

---

#### Question 23 [Bloom's Level: L3 - Apply]
**Which Pandas function is used to convert categorical variables into binary dummy (one-hot encoded) columns?**  
A) `pd.categorize()`  
B) `pd.get_dummies()`  
C) `pd.one_hot()`  
D) `pd.to_binary()`  
**Answer: B**  
*Explanation:* `pd.get_dummies(df, columns=['cat_col'])` generates binary 0/1 indicator columns for categorical variables.

---

#### Question 24 [Bloom's Level: L3 - Apply]
**What is the output of `re.findall(r'\d{2,4}', 'Phone 12345, Code 12, ID 9')`?**  
A) `['1234', '12']`  
B) `['1234', '5', '12']`  
C) `['12345', '12']`  
D) `['9']`  
**Answer: A**  
*Explanation:* `\d{2,4}` matches between 2 and 4 consecutive digits. On `'12345'`, it matches the first 4 digits `'1234'`. On `'12'`, it matches `'12'`. `'9'` is ignored (only 1 digit).

---

#### Question 25 [Bloom's Level: L3 - Apply]
**Given raw values $[10, 20, 30, 40, 50]$, what is the Min-Max normalized value of $30$?**  
A) 0.3  
B) 0.5  
C) 0.6  
D) 0.75  
**Answer: B**  
*Explanation:* $X_{\text{norm}} = (30 - 10) / (50 - 10) = 20 / 40 = 0.5$.

---

#### Question 26 [Bloom's Level: L3 - Apply]
**Which regex pattern correctly matches an email address?**  
A) `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`  
B) `^\w+@\w+$`  
C) `^email:\d+$`  
D) `^.*@.*$`  
**Answer: A**  
*Explanation:* Option A enforces alphanumeric username characters, the `@` symbol, a valid domain name, and a 2+ character top-level domain (`.com`, `.edu`).

---

### 10.4 Level 4: Analyze (Analysis, Logic & Bug Detection)

#### Question 27 [Bloom's Level: L4 - Analyze]
**Analyze why Min-Max Normalization is severely distorted by the presence of extreme outliers, while Z-Score Standardization is more resilient:**  
A) Z-Score cannot be computed on negative numbers  
B) Min-Max relies directly on $X_{\max}$ and $X_{\min}$, so an extreme outlier dramatically inflates the denominator and crushes all standard data into a narrow sub-range near 0; Z-Score scales relative to standard deviation  
C) Min-Max is only for categorical data  
D) There is no distortion  
**Answer: B**  
*Explanation:* Because Min-Max bounds data strictly to $[0, 1]$ using extrema, an outlier at $X_{\max} = 100,000$ compresses standard values into $[0.001, 0.002]$.

---

#### Question 28 [Bloom's Level: L4 - Analyze]
**A developer runs `df['Age'].fillna(df['Age'].mean(), inplace=True)` on an integer column with `NaN` values, but encounters a deprecation warning in Pandas 2.0+. What is the modern best practice?**  
A) Use `df['Age'] = df['Age'].fillna(df['Age'].mean())`  
B) Use `df.dropna()`  
C) Delete the column  
D) Use Python `eval()`  
**Answer: A**  
*Explanation:* `inplace=True` on Series is deprecated in modern Pandas; explicit reassignment (`df['col'] = df['col'].fillna(...)`) is the standard practice.

---

#### Question 29 [Bloom's Level: L4 - Analyze]
**Analyze the effect of `df.drop_duplicates(subset=['ID'], keep='last')` on records with duplicate IDs `[1, 2, 3, 2, 4, 2]`:**  
A) Retains index 1 (first 2)  
B) Retains index 5 (last 2) and drops earlier duplicates at index 1 and index 3  
C) Drops all records with ID 2  
D) Keeps all records  
**Answer: B**  
*Explanation:* `keep='last'` instructs Pandas to retain only the final occurrence of duplicate values and discard all preceding instances.

---

#### Question 30 [Bloom's Level: L4 - Analyze]
**What is the consequence of setting `errors='ignore'` in `pd.to_numeric(df['Salary'], errors='ignore')` when the column contains strings like `"Sixty Thousand"`?**  
A) Strings become NaN  
B) Conversion is silently aborted and the entire column remains as `object` (string) dtype without raising an error  
C) Strings are converted to integers  
D) An error is raised  
**Answer: B**  
*Explanation:* `errors='ignore'` suppresses exceptions and leaves the Series unmodified with its original datatype.

---

#### Question 31 [Bloom's Level: L4 - Analyze]
**Why does `re.sub(r'[^a-zA-Z0-9\s]', '', raw_text)` safely clean textual data for NLP models?**  
A) It deletes all vowels  
B) It preserves alphabetic characters, numbers, and whitespace while eliminating punctuation noise and special symbols  
C) It converts text to uppercase  
D) It encrypts words  
**Answer: B**  
*Explanation:* The negated set `[^a-zA-Z0-9\s]` matches everything EXCEPT alphanumeric letters, digits, and spaces, replacing punctuation noise with empty strings.

---

#### Question 32 [Bloom's Level: L4 - Analyze]
**Compare `fuzz.token_sort_ratio("Microsoft Corporation", "Microsoft")` vs `fuzz.token_set_ratio("Microsoft Corporation", "Microsoft")`. Why does `token_set_ratio` score higher?**  
A) `token_sort_ratio` is broken  
B) `token_set_ratio` computes intersection and remainder token subsets, recognizing that `"Microsoft"` is fully contained in the token set, yielding a score of 100  
C) `token_set_ratio` ignores letters  
D) Both score 50  
**Answer: B**  
*Explanation:* `token_set_ratio` isolates intersecting common tokens and scores 100 when one string's tokens are a subset of the other.

---

#### Question 33 [Bloom's Level: L4 - Analyze]
**If a dataset has 100 rows and 10 rows have missing salaries, what is the mean of the salary column after imputing with `df['Salary'].mean()` compared to before imputation?**  
A) Increases by 10%  
B) Decreases by 10%  
C) Exactly identical to the pre-imputation mean  
D) Becomes 0  
**Answer: C**  
*Explanation:* Imputing missing values with the arithmetic mean of observed values does not change the sample mean: $\frac{\sum X + k \bar{X}}{N + k} = \bar{X}$.

---

#### Question 34 [Bloom's Level: L4 - Analyze]
**Why must string `.strip()` be applied to categorical columns before running `drop_duplicates()` or groupby operations?**  
A) To convert characters to UTF-8  
B) Hidden leading/trailing spaces (e.g. `' CSE'` vs `'CSE'`) make identical categories appear distinct to string equality operators  
C) To remove numbers  
D) To shorten text length  
**Answer: B**  
*Explanation:* Whitespace differences prevent string equality matches, leading to fragmented duplicate groups and incorrect aggregations.

---

### 10.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)

#### Question 35 [Bloom's Level: L5 - Evaluate]
**Evaluate the optimal strategy for handling missing values in a machine learning dataset where the target variable column `Loan_Status` has 2% missing values:**  
A) Impute with the mode (`"Approved"`)  
B) Impute with a random value  
C) Drop rows where the target label is missing (`df.dropna(subset=['Loan_Status'])`) because imputing target labels introduces artificial ground-truth bias  
D) Replace with 0  
**Answer: C**  
*Explanation:* In supervised machine learning, imputing the target label contaminates ground truth and introduces false supervisory signals. Rows with missing target labels should be dropped.

---

#### Question 36 [Bloom's Level: L5 - Evaluate]
**Evaluate which string distance metric is best suited for matching messy vendor names across international bank invoices (e.g. `"Acme Corp Pvt Ltd"` vs `"Acme Corporation"`):**  
A) Exact string equality (`==`)  
B) `fuzzywuzzy.fuzz.token_set_ratio`  
C) `re.match`  
D) String length comparison  
**Answer: B**  
*Explanation:* `token_set_ratio` is specifically designed for multi-word corporate names with varying suffixes, duplicates, and abbreviations.

---

#### Question 37 [Bloom's Level: L6 - Create]
**Design an end-to-end Python cleaning pipeline function that deduplicates on ID, coerces invalid ages to numeric, and imputes missing salary with the median:**  
A)
```python
def clean_data(raw_df):
    df = raw_df.copy()
    df = df.drop_duplicates(subset=['ID'], keep='first')
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
    df['Salary'] = df['Salary'].fillna(df['Salary'].median())
    return df
```
B)
```python
def clean_data(raw_df):
    return raw_df.dropna()
```
C)
```python
def clean_data(raw_df):
    return raw_df.fillna(0)
```
D)
```python
def clean_data(raw_df):
    return raw_df.drop(columns=['Age', 'Salary'])
```
**Answer: A**  
*Explanation:* Option A safely operates on a DataFrame copy, eliminates duplicate primary IDs, coerces invalid strings to `NaN`, and robustly imputes missing numerical entries with medians.

---

#### Question 38 [Bloom's Level: L6 - Create]
**Which Python expression correctly filters all outliers in a DataFrame column `'Price'` using Tukey's $1.5 \times \text{IQR}$ rule?**  
A)
```python
q1 = df['Price'].quantile(0.25)
q3 = df['Price'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['Price'] < q1 - 1.5 * iqr) | (df['Price'] > q3 + 1.5 * iqr)]
```
B)
```python
outliers = df[df['Price'] > df['Price'].mean() * 1.5]
```
C)
```python
outliers = df[df['Price'] < 0]
```
D)
```python
outliers = df.filter(regex='Price')
```
**Answer: A**  
*Explanation:* Option A computes percentiles $Q1$ and $Q3$, derives $\text{IQR} = Q3 - Q1$, and applies lower ($Q1 - 1.5 \times \text{IQR}$) and upper ($Q3 + 1.5 \times \text{IQR}$) fence filters.

---

#### Question 39 [Bloom's Level: L5 - Evaluate]
**Evaluate the risk of deleting all rows with missing values (`df.dropna()`) when 40% of rows contain at least one missing field:**  
A) No risk; it is always best to drop missing data  
B) Deleting 40% of rows results in catastrophic information loss, statistical power depletion, and potential sampling bias if data is not MCAR  
C) It increases machine learning accuracy automatically  
D) It converts the DataFrame to SQL  
**Answer: B**  
*Explanation:* High deletion rates reduce dataset size drastically and introduce severe bias if missingness correlates with other variables. Imputation is required.

---

#### Question 40 [Bloom's Level: L6 - Create]
**You are designing a customer onboarding data pipeline. How can you standardize all phone numbers into a clean 10-digit format (e.g. `+91-98765-43210` ➔ `9876543210`)?**  
A) `df['phone'] = df['phone'].astype(int)`  
B) `df['phone'] = df['phone'].astype(str).str.replace(r'\D', '', regex=True).str[-10:]`  
C) `df['phone'] = df['phone'].str.strip()`  
D) `df['phone'] = df['phone'].str.lower()`  
**Answer: B**  
*Explanation:* Replacing all non-digits (`\D`) strips country codes, hyphens, and spaces, and `.str[-10:]` slices the standard 10-digit national number.
