# UNIT 1: DATA WRANGLING & MACHINE-READABLE FORMATS (CO1)
**Course:** DSA05 / DSA0501 – Query Processing for Data Science  
**Target:** 180-Question MCQ Exam Preparation & Comprehensive Concept Mastery  
**Assessment Framework:** Bloom's Revised Taxonomy (Levels L1 to L6)

---

## 📌 TABLE OF CONTENTS
1. [Core Concepts & Theoretical Framework](#1-core-concepts--theoretical-framework)
   - 1.1 What is Data Wrangling? Definition, Scope, & Goals
   - 1.2 Importance of Data Wrangling & GIGO Principle
   - 1.3 The 6-Step Data Wrangling Process / Lifecycle
   - 1.4 Core Tasks of Data Wrangling
   - 1.5 Data Wrangling Tools (Python Ecosystem, OpenRefine, Tabula, etc.)
2. [Python Basics for Data Wrangling](#2-python-basics-for-data-wrangling)
   - 2.1 Core Data Structures & Mutability
   - 2.2 File I/O Operations & Context Managers
   - 2.3 Essential String Manipulation Methods
3. [Machine-Readable Data & File Formats](#3-machine-readable-data--file-formats)
   - 3.1 Human-Readable vs Machine-Readable Data
   - 3.2 CSV Processing (`csv.reader`, `csv.writer`, `DictReader`, `DictWriter`, Quoting)
   - 3.3 JSON Processing (`load`, `loads`, `dump`, `dumps`, nested normalization)
   - 3.4 XML Processing (`xml.etree.ElementTree`, elements, tags, attributes, XPath)
4. [Understanding Database Schemas](#4-understanding-database-schemas)
   - 4.1 Schema Definition & Components
   - 4.2 Constraints & Schema Mapping
5. [High-Yield Exam Tips & Common MCQ Traps](#5-high-yield-exam-tips--common-mcq-traps)
6. [Bloom's Taxonomy-Aligned MCQ Question Bank (40+ Questions)](#6-blooms-taxonomy-aligned-mcq-question-bank)
   - [6.1 Level 1: Remember (Knowledge & Recall)](#61-level-1-remember-knowledge--recall)
   - [6.2 Level 2: Understand (Comprehension & Explanation)](#62-level-2-understand-comprehension--explanation)
   - [6.3 Level 3: Apply (Application, Computation & Code Output)](#63-level-3-apply-application-computation--code-output)
   - [6.4 Level 4: Analyze (Analysis, Logic & Bug Detection)](#64-level-4-analyze-analysis-logic--bug-detection)
   - [6.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)](#65-level-5--6-evaluate--create-judgment-architecture--design)

---

## 1. CORE CONCEPTS & THEORETICAL FRAMEWORK

### 1.1 What is Data Wrangling?
* **Definition:** Data Wrangling (also termed *Data Munging*) is the iterative process of transforming and mapping raw, unstructured, or disparate data into a clean, structured, and standardized format suitable for downstream data analysis, visualization, and machine learning.
* **Key Distinction:**
  * **Data Cleaning:** Sub-phase of wrangling focused specifically on fixing errors, missing values, duplicates, and outliers.
  * **Data Wrangling:** Broader end-to-end pipeline encompassing data ingestion, parsing, structural reshaping, type casting, merging, cleaning, enriching, and exporting.
  * **ETL (Extract, Transform, Load):** Typically an automated, batch-driven enterprise database process. Data wrangling is more exploratory, iterative, and interactive.

### 1.2 Importance of Data Wrangling & The GIGO Principle
* **Garbage In, Garbage Out (GIGO):** Any analytical model or machine learning algorithm trained on dirty, poorly formatted, or inconsistent data will produce unreliable, skewed, or misleading outputs.
* **Industry Reality:** Data scientists spend **70% to 80%** of their total project time on data wrangling and preparation.
* **Objectives:**
  1. Ensure **data accuracy** (correct values) and **completeness** (no unhandled missing data).
  2. Ensure **structural uniformity** across heterogeneous data sources.
  3. Reduce computational overhead during querying and model training.

### 1.3 The 6-Step Data Wrangling Process / Lifecycle
```
[ 1. Discovering / Ingesting ] ➔ [ 2. Structuring / Parsing ] ➔ [ 3. Cleaning / Preprocessing ]
                                                                        │
[ 6. Publishing / Storing ]   ⬅ [ 5. Validating / Auditing ] ⬅ [ 4. Enriching / Transforming ]
```
1. **Discovering (Ingestion):** Understanding raw data sources, inspecting formats (CSV, JSON, XML, SQL), evaluating volume, schema, and identifying initial flaws.
2. **Structuring (Parsing):** Reorganizing unstructured/semi-structured raw data into tabular, hierarchical, or relational formats with distinct rows and typed columns.
3. **Cleaning:** Addressing missing values, parsing incorrect data types, eliminating duplicates, correcting spelling via fuzzy matching, and handling outliers.
4. **Enriching:** Augmenting datasets with external data, creating engineered features (e.g., extracting `day_of_week` from dates), and combining multiple datasets.
5. **Validating:** Verifying that the processed data conforms to structural constraints, business rules, statistical ranges, and schema requirements.
6. **Publishing (Storing):** Exporting the clean dataset to analytical stores (CSV, JSON, SQL database, Parquet, or data warehouse).

### 1.4 Core Tasks of Data Wrangling
* **Extraction & Ingestion:** Loading data from local files, APIs, web scraping, or database connections.
* **Type Casting & Standardization:** Converting string numbers to integers/floats, string dates to `datetime64`, unifying categorical spellings.
* **Data Reshaping:** Pivoting (long to wide), melting (wide to long), stacking/unstacking, grouping, and aggregating.
* **Merging & Joining:** Combining relational datasets using common primary/foreign keys.

### 1.5 Data Wrangling Tools
* **Python Libraries:**
  * `pandas`: In-memory tabular data manipulation (`DataFrame`, `Series`).
  * `numpy`: High-performance numerical computing and vectorization.
  * Standard Library: `csv`, `json`, `xml.etree.ElementTree`, `re`, `sqlite3`.
* **GUI / Dedicated Wrangling Platforms:**
  * **OpenRefine:** Open-source desktop tool for exploring messy data, cleaning, transforming between formats, and clustering for fuzzy matching.
  * **Trifacta Wrangler:** Interactive enterprise data wrangling platform.
  * **Tabula:** Specialized open-source tool to extract tables embedded inside PDF documents into CSV/Excel format.
  * **Beautiful Soup / lxml:** HTML and XML parsing libraries for web scraping.

---

## 2. PYTHON BASICS FOR DATA WRANGLING

### 2.1 Core Data Structures & Mutability
| Data Structure | Syntax | Mutable? | Ordered? | Duplicates? | Common Use in Wrangling |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | `[1, "apple", 3.14]` | **Yes** | **Yes** | Allowed | Storing row records, column values |
| **Tuple** | `(1, "apple", 3.14)` | **No** (Immutable) | **Yes** | Allowed | Database query return records (`cursor.fetchall()`) |
| **Dictionary** | `{"id": 101, "name": "Alice"}` | **Yes** | **Yes** (Python 3.7+) | Unique Keys | JSON objects, mapping columns, record representation |
| **Set** | `{"apple", "banana"}` | **Yes** | **No** | Disallowed | Fast membership checks, removing duplicate IDs |

### 2.2 File I/O Operations & Context Managers
* **Standard Modes:**
  * `'r'`: Read only (Default; file must exist, raises `FileNotFoundError` if missing).
  * `'w'`: Write only (Creates file if missing; **truncates/overwrites** existing content completely).
  * `'a'`: Append (Writes to end of file without truncating).
  * `'r+'`: Read and Write mode (file pointer at beginning).
* **Context Manager (`with` statement):**
  * Guarantees that the file resource is automatically closed even if an unhandled exception occurs during execution.
  ```python
  # Best Practice
  with open('data.csv', mode='r', encoding='utf-8') as f:
      content = f.read()
  ```

### 2.3 Essential String Manipulation Methods
* `s.strip()`: Removes leading and trailing whitespace/newlines. `s.lstrip()` removes leading; `s.rstrip()` removes trailing.
* `s.split(sep=None)`: Splits string by delimiter into a `list` of substrings.
* `sep.join(list_of_strings)`: Concatenates list elements with delimiter `sep`.
* `s.replace(old, new)`: Replaces occurrences of substring `old` with `new`.
* `s.lower()`, `s.upper()`, `s.title()`, `s.capitalize()`: Casing transformations.
* Slicing: `s[start:end:step]` — `s[::-1]` reverses string.

---

## 3. MACHINE-READABLE DATA & FILE FORMATS

### 3.1 Human-Readable vs Machine-Readable Data
* **Human-Readable:** Data formatted for visual consumption by humans (e.g., styled PDF reports, formatted Word documents, spreadsheets with merged cells and visual charts). Hard for parsers to process automatically.
* **Machine-Readable:** Structured, standardized plain-text formats with unambiguous syntactic delimiters, clear hierarchies, and standard character encoding (UTF-8), enabling automated computer parsing without human intervention.
* **Standard Formats:** **CSV** (tabular), **JSON** (hierarchical key-value), **XML** (tagged hierarchical tree).

---

### 3.2 CSV Data Processing (`import csv`)
CSV (Comma-Separated Values) stores tabular data in plain text, with rows separated by line breaks (`\n`) and columns by a delimiter (default `,`).

#### 1. `csv.reader` & `csv.writer` (List-based)
```python
import csv

# Reading CSV rows as lists of strings
with open('students.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)  # Extract header list: ['ID', 'Name', 'Marks']
    for row in reader:     # row is a list of strings: ['101', 'Alice', '88']
        print(row[0], row[1])

# Writing CSV rows from lists
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['ID', 'Name', 'Marks'])
    writer.writerows([
        ['101', 'Alice', 88],
        ['102', 'Bob', 92]
    ])
```

#### 2. `csv.DictReader` & `csv.DictWriter` (Dictionary-based)
* `csv.DictReader`: Reads the first row as field names (keys) and returns each subsequent row as an `OrderedDict` or standard `dict`.
```python
with open('students.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Marks'])  # Access columns by header name!
```
* `csv.DictWriter`: Writes dictionaries using a predefined `fieldnames` list.
```python
fieldnames = ['ID', 'Name', 'Department']
with open('out.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # REQUIRED: writes the column names
    writer.writerow({'ID': '1', 'Name': 'Aarav', 'Department': 'CSE'})
```

#### 3. CSV Quoting Constants
* `csv.QUOTE_MINIMAL` (Default): Quotes fields only if they contain the delimiter, quotechar, or newline.
* `csv.QUOTE_ALL`: Quotes every single field regardless of content type.
* `csv.QUOTE_NONNUMERIC`: Quotes all non-numeric fields; converts unquoted fields to `float`.
* `csv.QUOTE_NONE`: Never quotes fields; requires an `escapechar` parameter to be set if delimiter appears in data.

---

### 3.3 JSON Data Processing (`import json`)
JSON (JavaScript Object Notation) is a lightweight, text-based data interchange format built on key-value pairs (`{}`) and ordered lists (`[]`).

#### 1. JSON Data Types vs Python Equivalents
| JSON Type | Python Type | Syntax Example |
| :--- | :--- | :--- |
| `object` | `dict` | `{"name": "Alice"}` |
| `array` | `list` | `[1, 2, 3]` |
| `string` | `str` | `"Hello"` (Must use double quotes `"`) |
| `number (int/real)` | `int` / `float` | `42`, `3.14` |
| `true` / `false` | `True` / `False` | Lowercase in JSON, capitalized in Python |
| `null` | `None` | `null` in JSON, `None` in Python |

#### 2. The 4 Essential Functions of the `json` Module
* **String-based (`'s'` in function name):**
  * `json.loads(json_string)`: Parses JSON string into a Python object.
  * `json.dumps(python_obj, indent=4, sort_keys=True)`: Serializes Python object into a formatted JSON string.
* **File-based (Takes a file pointer `fp`):**
  * `json.load(file_pointer)`: Reads and parses JSON directly from a file stream.
  * `json.dump(python_obj, file_pointer, indent=4)`: Serializes and writes Python object into a file stream.

```python
import json

# Loading from file
with open('data.json', 'r') as f:
    data = json.load(f)

# Dumping to file with pretty indentation
with open('clean_data.json', 'w') as f:
    json.dump(data, f, indent=4)
```

#### 3. Normalizing Nested JSON in Pandas
* Use `pd.json_normalize()` to flatten nested hierarchical JSON structures into tabular DataFrames:
```python
import pandas as pd
raw_json = [
    {"id": 1, "name": "Alice", "contact": {"email": "alice@test.com", "city": "Chennai"}},
    {"id": 2, "name": "Bob", "contact": {"email": "bob@test.com", "city": "Bangalore"}}
]
df = pd.json_normalize(raw_json)
# Columns created: 'id', 'name', 'contact.email', 'contact.city'
```

---

### 3.4 XML Data Processing (`import xml.etree.ElementTree as ET`)
XML (eXtensible Markup Language) represents hierarchical tree-structured data using custom tags, elements, attributes, and text nodes.

#### 1. Anatomy of an XML Tree
```xml
<?xml version="1.0" encoding="UTF-8"?> <!-- Prolog -->
<catalog>                              <!-- Root Element -->
    <course id="CS101" level="UG">     <!-- Child Element with Attributes -->
        <title>Data Science</title>    <!-- Sub-element with Text Content -->
        <credits>4</credits>
    </course>
</catalog>
```

#### 2. Parsing XML with `ElementTree`
* **From File:** `tree = ET.parse('courses.xml')` ➔ `root = tree.getroot()`
* **From String:** `root = ET.fromstring(xml_string)`

#### 3. Core Properties & Methods of an `Element`
* `elem.tag`: Tag name string (e.g., `'course'`, `'title'`).
* `elem.attrib`: Dictionary of attributes (e.g., `{'id': 'CS101', 'level': 'UG'}`).
* `elem.get('id')`: Retrieves attribute value by key (returns `'CS101'`).
* `elem.text`: The text content between open and closing tags (e.g., `'Data Science'`).

#### 4. Navigation & Searching Methods
* `root.findall('course')`: Returns a `list` of all direct children matching the tag `'course'`.
* `root.find('course')`: Returns the **first** matching direct child element, or `None`.
* `root.iter('title')`: Recursively iterates over **all descendants** matching `'title'` at any tree depth.

---

## 4. UNDERSTANDING DATABASE SCHEMAS

### 4.1 What is a Database Schema?
* A **Database Schema** is the formal structural blueprint or architecture of a database that defines:
  * Table names and column names.
  * Data types for every column (`INTEGER`, `VARCHAR`, `TEXT`, `REAL`, `DATE`, `BOOLEAN`).
  * Relationships between entities (One-to-One, One-to-Many, Many-to-Many).
  * Integrity constraints.

### 4.2 Essential Relational Schema Constraints
* **`PRIMARY KEY`:** Uniquely identifies each record in a table. Must be `UNIQUE` and cannot contain `NULL` values.
* **`FOREIGN KEY`:** A column (or set of columns) that references the `PRIMARY KEY` of another table, establishing referential integrity.
* **`NOT NULL`:** Guarantees that a column cannot store `NULL` (empty/missing) values.
* **`UNIQUE`:** Ensures that all values in a column are distinct from one another.
* **`CHECK`:** Validates that values in a column satisfy a specific Boolean condition (e.g., `CHECK (age >= 18)`).
* **`DEFAULT`:** Specifies a default fallback value if no value is supplied during `INSERT`.

---

## 5. HIGH-YIELD EXAM TIPS & COMMON MCQ TRAPS

1. **`json.loads` vs `json.load`:**
   * `json.loads(s)` takes a **String**. `json.load(fp)` takes a **File Object / Pointer**.
   * Same rule applies to `json.dumps(obj)` (returns String) vs `json.dump(obj, fp)` (writes to File).
2. **JSON Syntax Rules:**
   * JSON strings **must** use double quotes (`"key": "value"`). Single quotes (`'key': 'value'`) are invalid JSON and raise `json.JSONDecodeError`.
   * JSON booleans and null are lowercase: `true`, `false`, `null`.
3. **`csv.writer` newline parameter:**
   * Always set `newline=''` when opening CSV in write mode in Python 3 to prevent extra blank lines.
4. **XML ElementTree `.find()` vs `.findall()` vs `.iter()`:**
   * `.find()` returns the **first** matching direct child.
   * `.findall()` returns a **list** of matching direct children.
   * `.iter()` searches **recursively at all depths**.

---

## 6. BLOOM'S TAXONOMY-ALIGNED MCQ QUESTION BANK

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

### 6.1 Level 1: Remember (Knowledge & Recall)

#### Question 1 [Bloom's Level: L1 - Remember]
**What is the primary objective of Data Wrangling in the data science lifecycle?**  
A) To deploy machine learning models directly into production  
B) To convert raw, messy, and unstructured data into a clean, structured format suitable for analysis  
C) To compress large database files into ZIP archives  
D) To execute hardware clock cycles  
**Answer: B**  
*Explanation:* Data wrangling is defined as the systematic process of discovering, structuring, cleaning, enriching, and validating raw data to produce an analysis-ready dataset.

---

#### Question 2 [Bloom's Level: L1 - Remember]
**According to industry studies, approximately what percentage of a data scientist's time is typically spent on data preparation and wrangling?**  
A) 10% – 20%  
B) 30% – 40%  
C) 70% – 80%  
D) 95% – 100%  
**Answer: C**  
*Explanation:* Data scientists spend between 70% and 80% of their total project time on data wrangling, cleaning, and preparation tasks.

---

#### Question 3 [Bloom's Level: L1 - Remember]
**Which open-source desktop tool is specifically designed for exploring, cleaning, transforming messy data, and performing fuzzy clustering without writing code?**  
A) Postman  
B) OpenRefine  
C) Wireshark  
D) Docker  
**Answer: B**  
*Explanation:* OpenRefine (formerly Google Refine) is a premier open-source tool for exploring, cleaning, facet clustering, and transforming messy datasets.

---

#### Question 4 [Bloom's Level: L1 - Remember]
**Which specialized open-source tool is designed specifically to extract tabular data locked inside PDF documents into CSV or Excel format?**  
A) Beautiful Soup  
B) Tabula  
C) PyMongo  
D) Sqlite3  
**Answer: B**  
*Explanation:* Tabula is a dedicated open-source utility built to liberate tabular data from PDF documents into structured CSV/Excel spreadsheets.

---

#### Question 5 [Bloom's Level: L1 - Remember]
**Which of the following built-in Python data structures is IMMUTABLE?**  
A) `list`  
B) `dict`  
C) `tuple`  
D) `set`  
**Answer: C**  
*Explanation:* In Python, tuples (along with strings, integers, and floats) are immutable, meaning their elements cannot be modified in-place after creation.

---

#### Question 6 [Bloom's Level: L1 - Remember]
**What is the return type of `f.readlines()` when executed on an open text file object `f`?**  
A) A single continuous string  
B) A dictionary mapping line numbers to text  
C) A list of strings, where each element represents a single line termination  
D) A generator object  
**Answer: C**  
*Explanation:* `f.readlines()` reads all remaining lines from the file and returns them as a Python `list` of strings.

---

#### Question 7 [Bloom's Level: L1 - Remember]
**In Python's `json` module, which function is used to deserialize a JSON-formatted STRING into a Python dictionary or list?**  
A) `json.load()`  
B) `json.loads()`  
C) `json.dump()`  
D) `json.dumps()`  
**Answer: B**  
*Explanation:* `json.loads()` ("load string") deserializes a JSON string into Python objects. `json.load()` reads from a file pointer.

---

#### Question 8 [Bloom's Level: L1 - Remember]
**In Python's `xml.etree.ElementTree`, what property holds the dictionary of XML attributes for a given element?**  
A) `elem.tag`  
B) `elem.text`  
C) `elem.attrib`  
D) `elem.values`  
**Answer: C**  
*Explanation:* In `ElementTree`, `element.attrib` is a Python dictionary containing all the attribute name-value pairs defined inside the opening XML tag.

---

### 6.2 Level 2: Understand (Comprehension & Explanation)

#### Question 9 [Bloom's Level: L2 - Understand]
**What does the Garbage In, Garbage Out (GIGO) principle emphasize in data processing?**  
A) Fast processors make clean data  
B) Even the most advanced analytical models will produce flawed and misleading outputs if fed dirty or inaccurate input data  
C) Machine learning models can automatically fix all dirty data during training  
D) All deleted files must be sent to the Recycle Bin  
**Answer: B**  
*Explanation:* GIGO states that the quality of output is bounded by the quality of input. Faulty data produces flawed insights.

---

#### Question 10 [Bloom's Level: L2 - Understand]
**What is the primary difference between `json.load()` and `json.loads()`?**  
A) `json.load()` parses numbers, while `json.loads()` parses strings  
B) `json.load()` takes a file pointer stream as input, whereas `json.loads()` takes a string variable as input  
C) `json.load()` is deprecated in Python 3  
D) There is no functional difference  
**Answer: B**  
*Explanation:* The 's' in `loads()` stands for string (`json.loads(str)`), while `load(fp)` expects a readable file-like object.

---

#### Question 11 [Bloom's Level: L2 - Understand]
**Why must `newline=''` be passed to `open()` when writing CSV files using `csv.writer` in Python 3?**  
A) To force UTF-8 character encoding  
B) To prevent the CSV writer from writing double carriage-return newline sequences (`\r\r\n`) on Windows platforms  
C) To convert numeric strings to integers  
D) To enable row encryption  
**Answer: B**  
*Explanation:* In Python 3, the `csv` module handles newlines internally. Omitting `newline=''` causes Python's default text mode to insert extra blank lines on Windows.

---

#### Question 12 [Bloom's Level: L2 - Understand]
**Why is JSON `null` converted to `None` in Python, while JSON `true` is converted to `True`?**  
A) Because Python syntax requires uppercase singletons for Boolean and null objects  
B) It is a legacy bug in the CPython interpreter  
C) Because JSON cannot represent numbers  
D) Python does not have Boolean values  
**Answer: A**  
*Explanation:* JSON uses lowercase keywords (`null`, `true`, `false`), which map directly to Python's standard singleton primitives (`None`, `True`, `False`).

---

#### Question 13 [Bloom's Level: L2 - Understand]
**What is the difference between `element.find('course')` and `element.findall('course')` in `xml.etree.ElementTree`?**  
A) `find()` searches recursively across all subtrees, while `findall()` searches only direct children  
B) `find()` returns the first matching direct child element (or `None`), while `findall()` returns a list of all matching direct children  
C) `find()` returns text; `findall()` returns attributes  
D) There is no difference  
**Answer: B**  
*Explanation:* `.find()` stops and returns the first occurrence of the child tag, whereas `.findall()` returns all matching direct child elements as a list.

---

#### Question 14 [Bloom's Level: L2 - Understand]
**What is the purpose of the `pandas.json_normalize()` function?**  
A) To validate JSON syntax against a formal schema  
B) To flatten nested, semi-structured JSON objects and dictionaries into a 2D tabular DataFrame  
C) To convert XML trees into JSON strings  
D) To compress JSON files  
**Answer: B**  
*Explanation:* `pd.json_normalize()` takes nested hierarchical JSON keys (e.g. `{"user": {"address": {"city": "Chennai"}}}`) and flattens them into tabular columns (`user.address.city`).

---

#### Question 15 [Bloom's Level: L2 - Understand]
**How does a `PRIMARY KEY` constraint differ from a `UNIQUE` constraint in a relational database schema?**  
A) `UNIQUE` columns cannot be indexed, while `PRIMARY KEY` is always indexed  
B) A table can have multiple `UNIQUE` columns and they permit `NULL` values, whereas a table has only one `PRIMARY KEY` which strictly forbids `NULL` values  
C) `PRIMARY KEY` is only used for foreign keys  
D) There is no distinction  
**Answer: B**  
*Explanation:* A `PRIMARY KEY` enforces entity integrity (unique + strictly NOT NULL, one per table). `UNIQUE` permits `NULL` values in SQL standards and can be applied to multiple columns.

---

#### Question 16 [Bloom's Level: L2 - Understand]
**What is the role of the context manager (`with open(...) as f:`) in Python file handling?**  
A) It runs file operations in a parallel background thread  
B) It guarantees deterministic file closure and resource deallocation upon exiting the block, even if an exception is raised  
C) It encrypts the target file  
D) It converts the file into a Pandas DataFrame  
**Answer: B**  
*Explanation:* The `with` statement utilizes the context management protocol (`__enter__` and `__exit__`), ensuring resources are freed cleanly under all conditions.

---

### 6.3 Level 3: Apply (Application, Computation & Code Output)

#### Question 17 [Bloom's Level: L3 - Apply]
**What will be the output of the following Python code snippet?**
```python
import json
raw = '{"course": "Query Processing", "credits": 4, "active": true}'
data = json.loads(raw)
print(type(data["active"]), data["credits"] * 2)
```
A) `<class 'str'> 8`  
B) `<class 'bool'> 8`  
C) `<class 'bool'> 44`  
D) `<class 'int'> 8`  
**Answer: B**  
*Explanation:* `json.loads` converts `true` into Python Boolean `True` (`<class 'bool'>`), and `credits` is parsed as integer `4`, so `4 * 2 = 8`.

---

#### Question 18 [Bloom's Level: L3 - Apply]
**What will be the output of the following string processing code?**
```python
text = "   CS101:Data Wrangling:2026\n"
fields = text.strip().split(":")
print(fields[1])
```
A) `'   CS101'`  
B) `'Data Wrangling'`  
C) `'2026\n'`  
D) `['CS101', 'Data Wrangling', '2026']`  
**Answer: B**  
*Explanation:* `.strip()` removes leading whitespace and the trailing newline. `.split(":")` breaks the string into `['CS101', 'Data Wrangling', '2026']`. Index `1` is `'Data Wrangling'`.

---

#### Question 19 [Bloom's Level: L3 - Apply]
**Consider the following CSV file `grades.csv`:**
```csv
StudentID,Name,Grade
101,Aarav,A
102,Priya,B
```
**What is printed by this code?**
```python
import csv
with open('grades.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], end=' ')
```
A) `StudentID Name Grade`  
B) `Aarav Priya `  
C) `101 102 `  
D) `A B `  
**Answer: B**  
*Explanation:* `csv.DictReader` reads the first row as dictionary keys (`StudentID`, `Name`, `Grade`). Iterating over `reader` yields dicts where `row['Name']` produces `'Aarav'` and `'Priya'`.

---

#### Question 20 [Bloom's Level: L3 - Apply]
**Consider the XML document:**
```xml
<hospital>
    <patient id="P101"><name>Sunita Patil</name><age>32</age></patient>
    <patient id="P102"><name>Ramesh Bose</name><age>61</age></patient>
</hospital>
```
**What does the following Python script print?**
```python
import xml.etree.ElementTree as ET
root = ET.fromstring('''<hospital>
    <patient id="P101"><name>Sunita Patil</name><age>32</age></patient>
    <patient id="P102"><name>Ramesh Bose</name><age>61</age></patient>
</hospital>''')
first_patient = root.find('patient')
print(first_patient.attrib['id'], first_patient.find('name').text)
```
A) `P101 Sunita Patil`  
B) `P102 Ramesh Bose`  
C) `hospital P101`  
D) `AttributeError`  
**Answer: A**  
*Explanation:* `root.find('patient')` returns the first `<patient>` element (`id="P101"`). `.attrib['id']` returns `'P101'` and `find('name').text` returns `'Sunita Patil'`.

---

#### Question 21 [Bloom's Level: L3 - Apply]
**Which `csv` module quoting constant instructs the writer to quote non-numeric fields and convert unquoted numeric fields to `float` when reading?**  
A) `csv.QUOTE_MINIMAL`  
B) `csv.QUOTE_ALL`  
C) `csv.QUOTE_NONNUMERIC`  
D) `csv.QUOTE_NONE`  
**Answer: C**  
*Explanation:* `csv.QUOTE_NONNUMERIC` quotes all non-numeric fields during writing and automatically casts non-quoted fields to floats during reading.

---

#### Question 22 [Bloom's Level: L3 - Apply]
**What will be the output of `len(root.findall('item'))` if `root` is `<catalog><category><item/><item/></category></catalog>`?**  
A) 2  
B) 0  
C) 1  
D) Raises an `Exception`  
**Answer: B**  
*Explanation:* `.findall('item')` searches ONLY direct children of `root` (`<catalog>`). Since `<item>` elements are nested inside `<category>`, `findall('item')` finds 0 direct children. (To find all nested descendants, `root.iter('item')` would return 2).

---

#### Question 23 [Bloom's Level: L3 - Apply]
**What is the output of the following dictionary access on deserialized JSON?**
```python
import json
raw = '{"faculty": {"name": "Dr. Veena", "dept": "CSE", "courses": ["DSA05", "CS101"]}}'
data = json.loads(raw)
print(data["faculty"]["courses"][0])
```
A) `Dr. Veena`  
B) `CSE`  
C) `DSA05`  
D) `CS101`  
**Answer: C**  
*Explanation:* `data["faculty"]["courses"]` returns the list `["DSA05", "CS101"]`. Index `0` evaluates to `'DSA05'`.

---

#### Question 24 [Bloom's Level: L3 - Apply]
**How do you write a Python dictionary to a JSON file named `'clean_data.json'` with 4 spaces of indentation?**  
A) `json.dump(data, 'clean_data.json', indent=4)`  
B) `with open('clean_data.json', 'w') as f: json.dump(data, f, indent=4)`  
C) `with open('clean_data.json', 'w') as f: json.dumps(data, f, indent=4)`  
D) `json.write(data, 'clean_data.json', spaces=4)`  
**Answer: B**  
*Explanation:* `json.dump(obj, fp, indent=4)` takes the data object and the open writable file pointer `fp`.

---

#### Question 25 [Bloom's Level: L3 - Apply]
**What does `element.get('status', 'Pending')` do in `xml.etree.ElementTree`?**  
A) Raises an error if `'status'` attribute is missing  
B) Retrieves the value of the XML attribute `'status'`, returning `'Pending'` as fallback default if the attribute does not exist  
C) Renames the tag to `'Pending'`  
D) Creates a new child tag `'status'`  
**Answer: B**  
*Explanation:* Similar to Python dictionary `.get()`, `element.get(key, default)` safely returns the attribute value or the default fallback.

---

#### Question 26 [Bloom's Level: L3 - Apply]
**What is the result of the string slicing operation `"MACHINE_DATA"[::-1]`?**  
A) `"MACHINE_DATA"`  
B) `"ATAD_ENIHCAM"`  
C) `"MACHINE"`  
D) `"DATA"`  
**Answer: B**  
*Explanation:* The slice step `-1` reverses the string completely, yielding `"ATAD_ENIHCAM"`.

---

### 6.4 Level 4: Analyze (Analysis, Logic & Bug Detection)

#### Question 27 [Bloom's Level: L4 - Analyze]
**A developer attempts to parse the following JSON string in Python:**
```python
import json
json_str = "{'student_id': 101, 'name': 'Muzammil'}"
data = json.loads(json_str)
```
**Why does this code throw a `json.JSONDecodeError`?**  
A) `student_id` should not be a number  
B) JSON standard syntax strictly requires double quotes (`"`) for keys and string values; single quotes (`'`) are invalid JSON  
C) `json.loads` can only parse lists  
D) Python dictionaries cannot have integer values  
**Answer: B**  
*Explanation:* The official JSON standard (RFC 8259) specifies that string literals and keys must be delimited by double quotes (`"`). Using single quotes causes a decode error.

---

#### Question 28 [Bloom's Level: L4 - Analyze]
**Analyze the difference between `.findall()` and `.iter()` in `xml.etree.ElementTree`:**
```python
tree = ET.parse('catalog.xml')
root = tree.getroot()
res1 = len(root.findall('price'))
res2 = len(list(root.iter('price')))
```
**If `<price>` tags appear inside nested `<book>` elements under `<catalog>`, why is `res1 == 0` while `res2 == 50`?**  
A) `findall()` searches only direct children of `root`, while `iter()` searches recursively across all descendant nodes at any nesting depth  
B) `findall()` is limited to 10 elements  
C) `iter()` converts elements into strings  
D) `findall()` works only on root tags  
**Answer: A**  
*Explanation:* `findall(tag)` checks direct child elements of `root`. `iter(tag)` recursively traverses the entire element hierarchy at arbitrary depths.

---

#### Question 29 [Bloom's Level: L4 - Analyze]
**Consider an incoming banking transaction CSV with missing account numbers and duplicate transaction IDs. What sequence of wrangling operations must be applied to ensure database schema conformity?**  
A) Insert raw rows ➔ Run database triggers ➔ Delete failed rows  
B) Filter out records with blank account numbers (enforcing NOT NULL) ➔ Deduplicate transaction IDs (enforcing PRIMARY KEY) ➔ Cast numerical amounts ➔ Insert clean records  
C) Convert all numbers to strings ➔ Append rows  
D) Drop the database schema table  
**Answer: B**  
*Explanation:* Relational databases reject rows that violate `NOT NULL` and `PRIMARY KEY` uniqueness. Cleaning and validating records before insertion prevents runtime SQL constraint exceptions.

---

#### Question 30 [Bloom's Level: L4 - Analyze]
**Analyze the following code for exporting library books to CSV:**
```python
import csv
books = [{"id": 1, "title": "Data Wrangling"}, {"id": 2, "title": "SQL Mastery"}]
with open("books.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "title"])
    # Line X
    writer.writerows(books)
```
**What essential line of code is missing at `Line X`?**  
A) `writer.start()`  
B) `writer.writeheader()`  
C) `writer.set_columns()`  
D) `writer.flush()`  
**Answer: B**  
*Explanation:* `csv.DictWriter` requires an explicit call to `writer.writeheader()` to write the column names (`id,title`) as the first row of the CSV file.

---

#### Question 31 [Bloom's Level: L4 - Analyze]
**What error will occur if an incoming JSON payload has a field `"year": "Twenty-Twenty-Six"` when mapped to a SQL schema column `year INTEGER NOT NULL`?**  
A) The database will automatically translate the English text to integer 2026  
B) A type mismatch / conversion error will be raised during database insertion  
C) The year will be set to 0 silently  
D) The database will change the column type to VARCHAR  
**Answer: B**  
*Explanation:* Strongly typed relational columns (`INTEGER`) reject arbitrary alphabetic strings, resulting in SQL type violation exceptions unless preprocessed and typecasted during wrangling.

---

#### Question 32 [Bloom's Level: L4 - Analyze]
**In an XML document with namespace declarations (e.g. `<root xmlns:h="http://www.w3.org/TR/html4/">`), why does `root.find('h:table')` fail without a namespace dictionary?**  
A) `ElementTree` requires qualified Universal Resource Identifiers (URI) syntax or an explicit namespace dictionary mapping prefix `'h'` to the URI  
B) Namespaces cannot be used in Python  
C) Colons `:` are forbidden in XML  
D) `ElementTree` only supports JSON  
**Answer: A**  
*Explanation:* `ElementTree` parses namespaced tags as `{URI}tag`. To search using prefixes, you must supply a namespace map: `root.find('h:table', namespaces={'h': 'http://...'})`.

---

#### Question 33 [Bloom's Level: L4 - Analyze]
**Compare `csv.reader` and `csv.DictReader` when column positions in the CSV file change unexpectedly from `[ID, Name, Dept]` to `[Dept, ID, Name]`. Which reader is more resilient to this change?**  
A) `csv.reader` because it uses numeric indices `row[0]`  
B) `csv.DictReader` because it accesses values via header keys (`row['Dept']`), making code resilient to column reordering  
C) Both are equally vulnerable  
D) Neither can read reordered CSV files  
**Answer: B**  
*Explanation:* `DictReader` maps columns by header name, so `row['Dept']` correctly retrieves the department regardless of which physical column position it occupies.

---

#### Question 34 [Bloom's Level: L4 - Analyze]
**Analyze why semi-structured data like JSON is preferred over CSV when representing complex entities like medical patient records with multiple varying doctor visits.**  
A) CSV files cannot store text  
B) JSON naturally supports nested objects and variable-length arrays without requiring unnatural relational table decomposition or redundant row flattening  
C) JSON is always smaller in file size than CSV  
D) CSV cannot be read by Python  
**Answer: B**  
*Explanation:* JSON's hierarchical tree structure natively represents 1-to-many nested relationships (e.g. patient with an array of visits) within a single self-contained document.

---

### 6.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)

#### Question 35 [Bloom's Level: L5 - Evaluate]
**Evaluate the following scenario: An enterprise system receives 10 GB of product catalog data daily in XML, JSON, and CSV formats. Which format provides the smallest payload size and fastest parsing speed for flat, uniform tabular records?**  
A) XML, because tags provide rich semantic metadata  
B) JSON, because key names are repeated on every line  
C) CSV, because it eliminates repetitive tag and key name overhead, using minimal delimiter separators  
D) PDF  
**Answer: C**  
*Explanation:* For flat tabular data, CSV has zero redundant metadata overhead per row (unlike JSON/XML which repeat keys/tags for every single record), yielding minimum file sizes and maximum parsing throughput.

---

#### Question 36 [Bloom's Level: L5 - Evaluate]
**When deciding between `csv.QUOTE_MINIMAL` and `csv.QUOTE_ALL`, in which situation is `csv.QUOTE_ALL` strictly necessary?**  
A) When all data is integer  
B) When the receiving legacy downstream system cannot handle unquoted text or requires absolute delimiter isolation across all text fields  
C) When the CSV contains only 1 column  
D) When saving memory is the top priority  
**Answer: B**  
*Explanation:* `QUOTE_ALL` guarantees that every single field is enclosed in quotation marks, ensuring strict compatibility with rigid parsers that require uniform quoting.

---

#### Question 37 [Bloom's Level: L6 - Create]
**You are tasked with writing a validation function to clean raw book records before SQL insertion. Which implementation correctly handles missing titles, duplicate IDs, and invalid publication years?**  
A)
```python
def validate_books(books):
    seen_ids = set()
    cleaned = []
    for b in books:
        if not b.get('title') or not b.get('book_id'):
            continue
        if b['book_id'] in seen_ids:
            continue
        year = int(b.get('year', 0))
        if 1500 <= year <= 2026:
            seen_ids.add(b['book_id'])
            cleaned.append(b)
    return cleaned
```
B)
```python
def validate_books(books):
    return [b for b in books if b['title'] == 'Data']
```
C)
```python
def validate_books(books):
    return list(set(books))
```
D)
```python
def validate_books(books):
    books.clear()
    return books
```
**Answer: A**  
*Explanation:* Option A validates required keys (`title`, `book_id`), tracks uniqueness using a hash `set()` to eliminate duplicate IDs, and enforces domain bounds on publication years.

---

#### Question 38 [Bloom's Level: L6 - Create]
**Which code structure creates a valid XML document representing a university course using `xml.etree.ElementTree`?**  
A)
```python
import xml.etree.ElementTree as ET
root = ET.Element("university")
course = ET.SubElement(root, "course", id="DSA05")
title = ET.SubElement(course, "title")
title.text = "Query Processing"
tree = ET.ElementTree(root)
tree.write("course.xml", encoding="utf-8", xml_declaration=True)
```
B)
```python
import xml.etree.ElementTree as ET
tree = "<university><course id='DSA05'>Query Processing</course></university>"
tree.save("course.xml")
```
C)
```python
import xml.etree.ElementTree as ET
root = ET.create("university")
root.append_tag("course")
```
D)
```python
import xml.etree.ElementTree as ET
tree = ET.write_xml("university", "DSA05")
```
**Answer: A**  
*Explanation:* Option A uses the standard `ElementTree` API (`ET.Element`, `ET.SubElement`, `.text`, `ET.ElementTree`, `.write()`) to construct and serialize valid XML.

---

#### Question 39 [Bloom's Level: L5 - Evaluate]
**Evaluate the risk of using `inplace=True` versus explicit variable assignment (`df['col'] = df['col'].fillna(...)`) in modern Pandas wrangling workflows:**  
A) `inplace=True` is faster and uses zero RAM  
B) `inplace=True` is being deprecated in modern Pandas (v2.0+) because it can cause chained assignment bugs and does not provide performance gains; explicit assignment is the recommended modern standard  
C) Explicit assignment raises a `SyntaxError`  
D) There is no difference  
**Answer: B**  
*Explanation:* Modern Pandas documentation strongly discourages `inplace=True` due to unpredictable memory view behavior and chained indexing pitfalls. Explicit reassignment is best practice.

---

#### Question 40 [Bloom's Level: L6 - Create]
**You need to convert a complex nested JSON list of students with nested department objects into a clean tabular CSV for database loading. What is the most efficient Python/Pandas design?**  
A) Parse with regex character by character  
B) Use `pd.json_normalize(data)` to flatten nested keys into dot-separated columns, followed by `df.to_csv('students.csv', index=False)`  
C) Convert each JSON dictionary to a string and write to a text file  
D) Loop with 10 nested for-loops  
**Answer: B**  
*Explanation:* `pd.json_normalize()` flattens nested dictionaries in a vectorized, optimized manner, and `df.to_csv(index=False)` outputs a clean tabular CSV ready for RDBMS import.
