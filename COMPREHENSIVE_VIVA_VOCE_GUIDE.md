# 🎓 COMPREHENSIVE VIVA VOCE EXAMINATION MASTER GUIDE
**Course Code & Title:** DSA05 / DSA0501 – Query Processing for Data Science  
**Department:** Department of Computer Science & Engineering | SIMATS Engineering  
**Format:** Complete Oral Examination & Lab Viva Preparation (127 Questions with Model Answers)  

---

## 📌 TABLE OF CONTENTS
1. [Section 1: Viva Voce Strategy & Examiner Psychology](#section-1-viva-voce-examination-strategy--examiner-psychology)
2. [Section 2: Unit 1 Viva Questions – Data Wrangling & File Formats (Q1 – Q15)](#section-2-unit-1-viva-questions--data-wrangling--file-formats)
3. [Section 3: Unit 2 Viva Questions – Python SQL Libraries & Database Design (Q16 – Q35)](#section-3-unit-2-viva-questions--python-sql-libraries--database-design)
4. [Section 4: Unit 3 Viva Questions – Data Cleanup & Preprocessing (Q36 – Q55)](#section-4-unit-3-viva-questions--data-cleanup--preprocessing)
5. [Section 5: Unit 4 Viva Questions – Exploratory Data Analysis & Analytics (Q56 – Q71)](#section-5-unit-4-viva-questions--exploratory-data-analysis--analytics)
6. [Section 6: Unit 5 Viva Questions – Data Visualization with Pandas & Matplotlib (Q72 – Q87)](#section-6-unit-5-viva-questions--data-visualization-with-pandas--matplotlib)
7. [Section 7: Scenario-Based Industry Problems & Schema Analysis (Q88 – Q97)](#section-7-scenario-based-industry-problems--schema-analysis)
8. [Section 8: 30 Rapid-Fire Trick & Trap Questions (Q98 – Q127)](#section-8-30-rapid-fire-trick--trap-questions-examiner-favorites)

---

## SECTION 1: VIVA VOCE EXAMINATION STRATEGY & EXAMINER PSYCHOLOGY

Viva Voce is an oral technical assessment of your depth of understanding. Structure your oral responses using the **3-Step Answer Formula**:

1. **Core Verdict (10 Seconds):** State the direct answer or definition cleanly.

2. **Technical Mechanism (30 Seconds):** Explain why it works, the mathematical formula, or library behavior.

3. **Code Syntax & Edge Case (20 Seconds):** Cite the exact function, parameter, or error mode.


---

## SECTION 2: UNIT 1 VIVA QUESTIONS – DATA WRANGLING & FILE FORMATS

### Q1. What is Data Wrangling? How does it differ from Data Cleaning and traditional ETL?

> 🎯 **Core Answer:**  
> Data Wrangling (or Data Munging) is the end-to-end iterative process of discovering, structuring, cleaning, enriching, and validating raw or disparate data into an analysis-ready format. Data Cleaning is merely a subset of wrangling focused on fixing errors, while ETL is typically an automated, batch-oriented enterprise data warehouse pipeline.

**🔍 Technical Deep-Dive & Syntax:**  
• Data Cleaning: Focuses strictly on fixing dirty data (handling NaNs, removing duplicates, correcting data types, handling outliers).
• Data Wrangling: Broader, exploratory, iterative pipeline including data ingestion from heterogeneous formats (CSV/JSON/XML/SQL), reshaping (pivoting/melting), joining disparate sources, schema mapping, feature enrichment, and publishing.
• ETL (Extract, Transform, Load): Pre-planned, rigid batch pipeline designed by data engineers for operational warehouses. Wrangling is exploratory, dynamic, and hypothesis-driven, typically conducted by data scientists.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Is Data Wrangling the same as Data Cleaning?' Never say yes. State clearly that cleaning is just step 3 of the 6-step wrangling process.

---

### Q2. Explain the GIGO (Garbage In, Garbage Out) principle in Data Science with a real-world example.

> 🎯 **Core Answer:**  
> GIGO states that no matter how sophisticated an analytical algorithm or machine learning model is, if the input data is flawed, corrupted, or biased, the output will inevitably be inaccurate, misleading, or invalid.

**🔍 Technical Deep-Dive & Syntax:**  
Example: If an e-commerce platform trains a churn prediction model using customer spending records where currency symbols ('$', '€', '₹') were stripped without exchange rate conversion, a customer spending 1,000 Yen would be treated the same as one spending 1,000 Dollars. The model produces completely misleading predictions. Similarly, unhandled null values or corrupted outliers skew mean and standard deviation, distorting gradient descent weights.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can advanced deep learning models automatically fix GIGO?' Answer: No. Deep learning models cannot infer missing real-world ground truth and will overfit to corrupted noise or artifacts.

---

### Q3. What are the 6 stages of the Data Wrangling lifecycle? Explain the purpose of each stage.

> 🎯 **Core Answer:**  
> The six standardized stages are: (1) Discovering / Ingesting, (2) Structuring / Parsing, (3) Cleaning / Preprocessing, (4) Enriching / Feature Engineering, (5) Validating / Quality Auditing, and (6) Publishing / Storing.

**🔍 Technical Deep-Dive & Syntax:**  
1. Discovering: Inspecting raw sources, schema, volume, encoding, and identifying anomalies.
2. Structuring: Converting raw semi-structured text (JSON/XML/unstructured logs) into tabular rows and typed columns.
3. Cleaning: Imputing missing values, removing duplicates, filtering outliers, and casting data types.
4. Enriching: Adding third-party datasets, engineered features (e.g., extracting day of week from timestamp), or currency conversions.
5. Validating: Verifying adherence to business logic, domain boundaries, relational constraints, and schema rules.
6. Publishing: Exporting clean data to databases (PostgreSQL, SQLite), Parquet, or analytical dashboards.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Which step takes the longest time?' Answer: Cleaning and Structuring typically consume 70-80% of total wrangling time.

---

### Q4. What makes data 'machine-readable' versus 'human-readable'? Give concrete examples of each.

> 🎯 **Core Answer:**  
> Human-readable data is optimized for visual consumption (formatted PDFs, rich Word documents, spreadsheets with merged cells and visual charts). Machine-readable data consists of standardized, plain-text formats with unambiguous syntactic delimiters, strict hierarchies, and standard encoding (UTF-8) that computer parsers can process without human intervention (CSV, JSON, XML).

**🔍 Technical Deep-Dive & Syntax:**  
• Human-Readable: A PDF invoice containing text tables mixed with logos and merged cells. A computer cannot directly slice a column without complex optical character recognition (OCR) or table extraction algorithms (Tabula).
• Machine-Readable: CSV (comma delimiters, uniform rows), JSON (key-value dictionaries and arrays), XML (nested tags with element attributes). Parsers can deterministically load them into memory with zero visual interpretation.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Is an Excel spreadsheet (.xlsx) always machine-readable?' Answer: Not always. If an Excel sheet contains decorative header banners, merged cells, multiple nested sub-tables on one sheet, or color-coded status cells, it requires significant manual cleanup before automated parsing.

---

### Q5. In Python's built-in `csv` module, why is `newline=''` strictly mandatory when opening a file in write mode?

> 🎯 **Core Answer:**  
> In Python 3, `csv.writer` performs its own internal carriage-return and line-feed handling ('\r\n'). If `newline=''` is omitted when opening the file, Python's default text stream translation layer adds an extra '\r' on Windows systems, creating blank lines between every row.

**🔍 Technical Deep-Dive & Syntax:**  
Syntax:
```python
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'Salary'])
```
Omitting `newline=''` results in `\r\r\n` on Windows, which causes standard CSV parsers to read every second row as an empty record.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Does this issue happen on Linux or macOS?' Answer: Historically on Unix systems '\n' is standard, so the extra blank lines are most prominent on Windows, but PEP 305 specifies `newline=''` as mandatory across all platforms for portability.

---

### Q6. Compare `csv.reader` and `csv.DictReader`. In what scenario is `csv.DictReader` distinctly superior?

> 🎯 **Core Answer:**  
> `csv.reader` parses each row as a Python list of strings indexed by integer position (`row[0]`), whereas `csv.DictReader` maps each row to a dictionary using the header row as keys (`row['Salary']`). `DictReader` is vastly superior when column order is subject to change or when schemas have many columns.

**🔍 Technical Deep-Dive & Syntax:**  
• Resilience to Schema Changes: If a CSV file unexpectedly reorders columns from `[ID, Name, Salary]` to `[Salary, ID, Name]`, code relying on `csv.reader` (`row[2]`) will extract the Name instead of Salary, causing silent logic corruption. `DictReader` accesses `row['Salary']`, completely unaffected by column index shifts.
• Memory/Speed: `csv.reader` has slightly lower memory overhead and runs marginally faster because it creates simple lists rather than dictionary hash tables.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What happens if a CSV has no header row but you want to use DictReader?' Answer: You must supply the `fieldnames` parameter explicitly: `csv.DictReader(f, fieldnames=['ID', 'Name', 'Salary'])`.

---

### Q7. Explain the four CSV quoting constants in Python (`QUOTE_MINIMAL`, `QUOTE_ALL`, `QUOTE_NONNUMERIC`, `QUOTE_NONE`).

> 🎯 **Core Answer:**  
> These constants control when `csv.writer` encloses fields in quotes. `QUOTE_MINIMAL` quotes only fields containing special characters (delimiters, quotes, newlines); `QUOTE_ALL` quotes every field; `QUOTE_NONNUMERIC` quotes non-numeric strings and casts unquoted numbers to floats upon reading; `QUOTE_NONE` never quotes fields and requires an escape character.

**🔍 Technical Deep-Dive & Syntax:**  
• `csv.QUOTE_MINIMAL` (Default): Quotes only when necessary (e.g. text containing a comma like 'Chennai, India').
• `csv.QUOTE_ALL`: Encloses all fields in quotes regardless of data type. Useful when exporting to rigid legacy systems.
• `csv.QUOTE_NONNUMERIC`: Quotes text strings, leaves numbers unquoted. When reading with `csv.reader`, unquoted fields are automatically converted to Python `float`!
• `csv.QUOTE_NONE`: Instructs writer never to quote. If a delimiter appears inside a data string, the programmer must specify `escapechar='\\'` to prevent format corruption.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What happens if you use QUOTE_NONE and a comma exists inside a text value without escapechar?' Answer: Python raises `csv.Error: need to escape, but no escapechar set`.

---

### Q8. Differentiate between `json.load()`, `json.loads()`, `json.dump()`, and `json.dumps()` in Python.

> 🎯 **Core Answer:**  
> Functions ending in 's' operate on Strings; functions without 's' operate on File streams. `loads()` deserializes a JSON string into a Python object; `load()` deserializes from a file pointer. `dumps()` serializes a Python object into a JSON string; `dump()` serializes and writes to a file pointer.

**🔍 Technical Deep-Dive & Syntax:**  
• `json.loads(s)`: String ➔ Python dict/list. Example: `data = json.loads('{"a": 1}')`
• `json.load(fp)`: File Pointer ➔ Python dict/list. Example: `with open('d.json') as f: data = json.load(f)`
• `json.dumps(obj, indent=4)`: Python dict/list ➔ Formatted JSON string.
• `json.dump(obj, fp, indent=4)`: Python dict/list ➔ Written directly into file pointer.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you pass a file path string like 'data.json' directly into json.load()?' Answer: No! `json.load()` requires a file-like object returned by `open()`, not a string path. Passing a string path raises `AttributeError: 'str' object has no attribute 'read'`.

---

### Q9. Can JSON keys or string values be enclosed in single quotes? What happens if they are?

> 🎯 **Core Answer:**  
> No. The official JSON standard (RFC 8259) strictly dictates that all strings and object keys must be enclosed in double quotes (`"key": "value"`). Single quotes are syntactically invalid in JSON.

**🔍 Technical Deep-Dive & Syntax:**  
Attempting to execute `json.loads("{'name': 'Alice'}")` immediately raises `json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes`. If raw data contains single quotes, it must either be fixed using Python's `ast.literal_eval()` or preprocessed with regex before JSON parsing.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Python dictionaries allow single quotes, so why doesn't JSON?' Answer: JSON is a language-agnostic data interchange format, not a Python dictionary. Its grammar is strictly defined by ECMA-404/RFC 8259 to guarantee cross-language interoperability.

---

### Q10. How do JSON primitive data types map to Python native data types?

> 🎯 **Core Answer:**  
> JSON `object` maps to Python `dict`, `array` maps to `list`, `string` maps to `str`, `number (int/float)` maps to `int` or `float`, `true`/`false` maps to `True`/`False`, and JSON `null` maps to Python `None`.

**🔍 Technical Deep-Dive & Syntax:**  
| JSON Type | Python Native Type |
| :--- | :--- |
| `object` | `dict` |
| `array` | `list` |
| `string` | `str` |
| `number (integer)` | `int` |
| `number (real)` | `float` |
| `true` / `false` | `True` / `False` (Booleans) |
| `null` | `None` (NoneType) |

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What does JSON null become in a Pandas DataFrame?' Answer: When imported into a Pandas DataFrame, `null` becomes `numpy.nan` (Not a Number) or `None` depending on column dtype.

---

### Q11. What is the purpose of `pandas.json_normalize()`? How does it handle nested JSON dictionaries and lists?

> 🎯 **Core Answer:**  
> `pd.json_normalize()` is designed to flatten semi-structured, nested hierarchical JSON records into a 2D tabular DataFrame, creating dot-separated column names for nested dictionary keys.

**🔍 Technical Deep-Dive & Syntax:**  
Example:
```python
raw = [{'id': 1, 'info': {'name': 'Aarav', 'city': 'Chennai'}}]
df = pd.json_normalize(raw)
# Generates columns: 'id', 'info.name', 'info.city'
```
For nested lists of records (e.g. a customer having multiple order items), `json_normalize` accepts `record_path` to unroll the child list and `meta` to repeat parent attributes alongside each child row.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is the difference between pd.read_json() and pd.json_normalize()?' Answer: `pd.read_json()` expects uniform, flat JSON arrays. If records have deeply nested dictionaries or variable lists, `pd.read_json()` puts raw dictionaries inside DataFrame cells. `pd.json_normalize()` unpacks them into individual columns.

---

### Q12. How do you parse an XML document using Python's `xml.etree.ElementTree`? What is the difference between parsing a file vs parsing a string?

> 🎯 **Core Answer:**  
> To parse an XML file from disk, use `tree = ET.parse('file.xml')` followed by `root = tree.getroot()`. To parse an XML string directly from memory, use `root = ET.fromstring(xml_string)`.

**🔍 Technical Deep-Dive & Syntax:**  
```python
import xml.etree.ElementTree as ET
# From file:
tree = ET.parse('courses.xml')
root = tree.getroot()

# From string:
xml_data = '<catalog><course id="1">Data Science</course></catalog>'
root = ET.fromstring(xml_data)
```
`ET.parse()` returns an `ElementTree` wrapper object (which supports `tree.write()`), whereas `ET.fromstring()` returns the root `Element` object directly.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'If you use ET.parse(), can you call .tag directly on the tree variable?' Answer: No! `tree.tag` raises `AttributeError`. You must first call `root = tree.getroot()` and then inspect `root.tag`.

---

### Q13. In XML `ElementTree`, explain the difference between `element.find()`, `element.findall()`, and `element.iter()`.

> 🎯 **Core Answer:**  
> `.find('tag')` returns the FIRST matching direct child element (or None); `.findall('tag')` returns a Python LIST of all matching direct child elements; `.iter('tag')` recursively iterates over ALL matching descendant elements at any depth in the entire subtree.

**🔍 Technical Deep-Dive & Syntax:**  
Consider:
```xml
<catalog>
    <dept><course>DS</course></dept>
    <course>AI</course>
</catalog>
```
• `root.find('course')`: Returns the direct child `<course>AI</course>`.
• `root.findall('course')`: Returns a list with only 1 item (`[<course>AI</course>]`), completely missing the nested course inside `<dept>`.
• `root.iter('course')`: Recursively finds BOTH courses (`DS` and `AI`) regardless of nesting level!

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Why did my findall() return an empty list when I can clearly see the tag in the XML file?' Answer: Because `findall()` only checks immediate, direct children. If the tag is nested two levels down, you must use XPath like `root.findall('.//tag')` or use `root.iter('tag')`.

---

### Q14. What is the difference between an XML Attribute and XML Text? How do you access each in Python `ElementTree`?

> 🎯 **Core Answer:**  
> XML Attributes are key-value metadata pairs written inside the opening tag (e.g. `<student id="101">`), accessed via `element.attrib['id']` or `element.get('id')`. XML Text is the character data enclosed between the opening and closing tags (e.g. `<name>Alice</name>`), accessed via `element.text`.

**🔍 Technical Deep-Dive & Syntax:**  
```python
node = ET.fromstring('<book isbn="978-01" price="45.50">Data Wrangling</book>')
# Accessing attributes (returns string values):
isbn = node.attrib['isbn']      # '978-01'
price = float(node.get('price')) # 45.50

# Accessing inner text:
title = node.text.strip()       # 'Data Wrangling'
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What does node.get('missing_attr') return if the attribute is not found?' Answer: It returns `None` safely without throwing an error, or a default value if specified (`node.get('key', 'default')`). In contrast, `node.attrib['key']` raises a `KeyError`.

---

### Q15. What is a Database Schema, and why must schema validation be executed during the data wrangling phase?

> 🎯 **Core Answer:**  
> A Database Schema is the formal architectural blueprint of a database defining table structures, column data types, field lengths, and integrity constraints (Primary Key, Foreign Key, NOT NULL, CHECK, UNIQUE). Schema validation during wrangling ensures raw incoming semi-structured data conforms strictly to these rules before insertion, preventing catastrophic runtime SQL errors or data corruption.

**🔍 Technical Deep-Dive & Syntax:**  
During wrangling of JSON, CSV, or XML data:
1. Type Validation: Ensuring string 'Twenty' is converted to integer 20 before inserting into `INT` column.
2. Nullability Validation: Guaranteeing mandatory fields (`NOT NULL`) exist and are non-empty.
3. Uniqueness Validation: Checking that primary keys have no duplicates in the incoming batch.
4. Referential Integrity: Verifying foreign keys reference existing parent records.
5. Domain Range: Checking that percentages are within 0-100 or dates fall in valid calendar ranges.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What happens if you insert unvalidated raw data directly into an RDBMS?' Answer: The database engine will either abort the entire transaction due to constraint violation (e.g. `IntegrityError`), corrupt financial aggregates, or insert truncated data.

---

## SECTION 3: UNIT 2 VIVA QUESTIONS – PYTHON SQL LIBRARIES & DATABASE DESIGN

### Q16. What is the Python Database API Specification v2.0 (DB-API 2.0)? Name its primary components.

> 🎯 **Core Answer:**  
> DB-API 2.0 (defined in PEP 249) is a standardized interface specification that ensures all Python database drivers (e.g., `sqlite3`, `mysql.connector`, `psycopg2`) expose identical method signatures and connection paradigms, allowing code portability across different database engines.

**🔍 Technical Deep-Dive & Syntax:**  
Core standard interfaces:
1. Module-level `connect()` function.
2. Connection Object (`conn`): Manages transactions (`commit()`, `rollback()`), closes connection (`close()`), and creates cursors (`cursor()`).
3. Cursor Object (`cursor`): Executes commands (`execute()`, `executemany()`), and fetches result rows (`fetchone()`, `fetchall()`, `fetchmany()`).
4. Standard Exceptions: `DatabaseError`, `IntegrityError`, `OperationalError`, `ProgrammingError`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'If you write code for SQLite using DB-API, can it run on PostgreSQL with minimal changes?' Answer: Yes! Only the connection string and parameter placeholder format change; cursor methods and fetch calls remain identical.

---

### Q17. Compare SQLite, MySQL, and PostgreSQL in terms of architecture, concurrency, and typical use cases.

> 🎯 **Core Answer:**  
> SQLite is a serverless, zero-configuration embedded file database ideal for mobile/local storage and rapid testing; MySQL is a multi-threaded client-server RDBMS optimized for web read-heavy workloads (Port 3306); PostgreSQL is an enterprise object-relational RDBMS supporting MVCC concurrency, complex analytical queries, and JSONB data types (Port 5432).

**🔍 Technical Deep-Dive & Syntax:**  
| Feature | SQLite | MySQL | PostgreSQL |
| :--- | :--- | :--- | :--- |
| Architecture | Serverless (Single File) | Client-Server Daemon | Client-Server Daemon |
| Default Port | N/A (Local Disk) | 3306 | 5432 |
| Concurrency | Single writer (file lock) | High (Multi-threaded) | Very High (MVCC Multi-process) |
| Parameter Syntax | `?` (qmark) | `%s` (format) | `%s` (format) |
| Auto-Increment | `INTEGER PRIMARY KEY AUTOINCREMENT` | `INT AUTO_INCREMENT PRIMARY KEY` | `SERIAL PRIMARY KEY` |
| Outer Joins | LEFT JOIN only | LEFT and RIGHT JOIN | FULL, LEFT, and RIGHT JOIN |

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Why not use SQLite for a high-traffic e-commerce banking website?' Answer: SQLite locks the entire database file during write transactions. Under high concurrent writes from multiple users, it causes severe write contention and database locks.

---

### Q18. What is the difference between a Connection object and a Cursor object in Python database programming?

> 🎯 **Core Answer:**  
> A Connection object (`conn`) represents the physical communication channel to the database server/file and manages transactions (`commit`, `rollback`). A Cursor object (`cursor`) is the working control structure spawned from a connection that executes SQL queries and traverses the result set row-by-row.

**🔍 Technical Deep-Dive & Syntax:**  
• Connection (`conn`): Responsible for session lifecycle, database authentication, isolation levels, transaction boundary management (`conn.commit()`, `conn.rollback()`), and closing the socket.
• Cursor (`cursor`): Maintains context of current active query, query execution plan, row buffer pointer, metadata (`cursor.description`, `cursor.lastrowid`, `cursor.rowcount`), and data retrieval methods (`fetchone`, `fetchall`).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you call conn.execute() directly without creating a cursor in SQLite?' Answer: In `sqlite3`, `conn.execute()` is a non-standard convenience shortcut that internally creates a temporary cursor, executes the query, and returns the cursor.

---

### Q19. What is an in-memory SQLite database (`:memory:`)? When should it be used, and what happens when the connection closes?

> 🎯 **Core Answer:**  
> An in-memory SQLite database is created using `sqlite3.connect(':memory:')`. It resides entirely in volatile RAM rather than on disk. It is used for blazing-fast unit testing, temporary staging, and scratch data processing. When `conn.close()` is called, the database and all its tables and records are permanently erased.

**🔍 Technical Deep-Dive & Syntax:**  
Advantages:
1. Execution Speed: Operations are orders of magnitude faster because there is zero disk I/O latency.
2. Clean Isolation: Ideal for automated test suites because each test begins with a pristine environment without disk clutter.
Disadvantage: Total data loss on process termination or connection closure.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'If two different threads or scripts connect to :memory:, do they share the same database?' Answer: No! Each connection to `':memory:'` creates an independent, isolated in-memory database, unless URI shared cache mode is explicitly configured.

---

### Q20. What is SQL Injection? Write a vulnerable code snippet and demonstrate how parameterized queries prevent it.

> 🎯 **Core Answer:**  
> SQL Injection occurs when untrusted user input is directly concatenated or interpolated into an SQL command string, allowing an attacker to inject malicious SQL syntax that alters query logic or grants unauthorized database access. Parameterized queries separate SQL logic from data, completely neutralizing injection.

**🔍 Technical Deep-Dive & Syntax:**  
Vulnerable Code:
```python
# DANGEROUS! String formatting
query = f"SELECT * FROM users WHERE username = '{user_input}' AND password = '{pwd}'"
cursor.execute(query)
```
If attacker supplies `user_input = "admin' --"`, the query becomes:
`SELECT * FROM users WHERE username = 'admin' --' AND password = '...'`
The `--` comments out the password check, granting instant admin access!

Secure Parameterized Code:
```python
# SECURE! Database treats input strictly as literal data
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user_input, pwd))
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What if I put quotes around the placeholder like VALUES ('?')?' Answer: Putting quotes around the placeholder treats `?` as a literal string question mark instead of a placeholder, breaking query parameter binding!

---

### Q21. What parameter placeholders are used across SQLite, MySQL, and PostgreSQL in Python DB-API?

> 🎯 **Core Answer:**  
> SQLite uses the question mark placeholder `?` (qmark style); MySQL (`mysql.connector`) and PostgreSQL (`psycopg2`) use the format placeholder `%s`.

**🔍 Technical Deep-Dive & Syntax:**  
• SQLite:
`cursor.execute("INSERT INTO emp VALUES (?, ?)", (101, 'Aarav'))`
• MySQL / PostgreSQL:
`cursor.execute("INSERT INTO emp VALUES (%s, %s)", (101, 'Aarav'))`
• Named Placeholders:
SQLite supports `:name` (`VALUES (:id, :name)` with a dict `{'id': 101, 'name': 'Aarav'}`). PostgreSQL/psycopg2 supports `%(name)s`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Is %s in MySQL string formatting from Python?' Answer: No! Even though it looks like Python's string formatting operator, it is handled internally by the database driver driver-side parameter binding, ensuring safe type escaping.

---

### Q22. Why is calling `conn.commit()` strictly mandatory in Python DB-API? What happens if you forget it?

> 🎯 **Core Answer:**  
> In Python DB-API drivers, autocommit is disabled by default, meaning all Data Manipulation Language (DML) statements (`INSERT`, `UPDATE`, `DELETE`) execute inside an active transaction. If you forget to call `conn.commit()`, the changes remain uncommitted in temporary buffers and are completely rolled back and discarded when the connection closes.

**🔍 Technical Deep-Dive & Syntax:**  
Code Example:
```python
cursor.execute("INSERT INTO students VALUES (101, 'Muzammil')")
# If you do not call conn.commit(), data is NOT written to disk!
conn.close() # Changes are permanently lost!
```
To persist modifications permanently, you must explicitly call `conn.commit()`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Do SELECT queries require conn.commit()?' Answer: No. `SELECT` queries are read-only Data Query Language (DQL) operations; they do not modify database state and do not require commit.

---

### Q23. What is the purpose of `conn.rollback()` and how is it used in transaction exception handling?

> 🎯 **Core Answer:**  
> `conn.rollback()` aborts the current uncommitted transaction and undoes all database modifications made since the last `commit()`. It is used inside `try...except` blocks to restore the database to a consistent state if an error occurs midway through multi-step operations.

**🔍 Technical Deep-Dive & Syntax:**  
Robust Transaction Template:
```python
try:
    cursor.execute("UPDATE account SET bal = bal - 500 WHERE id = 1")
    cursor.execute("UPDATE account SET bal = bal + 500 WHERE id = 2")
    conn.commit() # Both updates succeed together
except Exception as e:
    conn.rollback() # If either fails, undo ALL changes
    print("Transaction failed, rolled back cleanly:", e)
finally:
    cursor.close()
    conn.close()
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What ACID property does this implement?' Answer: It directly implements Atomicity ('all or nothing').

---

### Q24. Differentiate between `cursor.fetchone()`, `cursor.fetchall()`, and `cursor.fetchmany(size)`.

> 🎯 **Core Answer:**  
> `cursor.fetchone()` returns the next single row as a tuple (or `None` when exhausted); `cursor.fetchall()` returns a list containing all remaining rows as tuples; `cursor.fetchmany(size)` returns a list of up to `size` rows, ideal for batching large result sets.

**🔍 Technical Deep-Dive & Syntax:**  
• Memory Management: Calling `fetchall()` on a 10-million row table will attempt to load all 10 million tuples into Python RAM simultaneously, causing an Out-Of-Memory (OOM) crash. `fetchmany(1000)` or iterating directly over the cursor (`for row in cursor:`) streams rows efficiently in chunks.
• State Tracking: The cursor acts as an internal pointer. If a query returns 10 rows and you call `cursor.fetchone()`, calling `cursor.fetchall()` next will return only the remaining 9 rows!

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you call cursor.fetchall() a second time immediately after the first call to get the data again?' Answer: No! The second call returns an empty list `[]` because the cursor buffer is already exhausted. You must re-execute the query to fetch again.

---

### Q25. What does `cursor.fetchall()` return when zero records match a `SELECT` query? Does it return `None` or an empty list?

> 🎯 **Core Answer:**  
> `cursor.fetchall()` returns an empty list `[]` when no rows match. It NEVER returns `None`.

**🔍 Technical Deep-Dive & Syntax:**  
Contrast with `cursor.fetchone()`:
• `cursor.fetchone()` returns `None` when zero rows match.
• `cursor.fetchall()` returns an empty list `[]`.
This distinction is critical when writing conditional checks: `if cursor.fetchall() is None:` will always evaluate to `False`!

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What does cursor.fetchmany(5) return if there are 0 matching rows?' Answer: It also returns an empty list `[]`.

---

### Q26. What do `cursor.rowcount` and `cursor.lastrowid` represent in Python database drivers?

> 🎯 **Core Answer:**  
> `cursor.rowcount` returns the number of rows modified, updated, or deleted by the last executed DML statement. `cursor.lastrowid` returns the auto-generated integer primary key of the last inserted row in SQLite.

**🔍 Technical Deep-Dive & Syntax:**  
• `cursor.rowcount`: After `DELETE FROM emp WHERE dept = 'IT'`, `cursor.rowcount` tells you exactly how many IT employees were deleted. (Note: In DB-API, for `SELECT` queries, `rowcount` is often `-1` until all rows are fetched).
• `cursor.lastrowid`: Essential after inserting a parent record (e.g. `orders`) to immediately retrieve its generated `order_id` for inserting dependent child records (`order_items`).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'In SQLite, if you execute an UPDATE statement that updates 0 rows because the WHERE condition matched nothing, what is rowcount?' Answer: `cursor.rowcount` will be 0.

---

### Q27. How can you configure SQLite in Python to return rows as dictionaries with column-name access (e.g., `row['salary']`)?

> 🎯 **Core Answer:**  
> Set `conn.row_factory = sqlite3.Row` on the connection object before creating the cursor. This wraps returned rows in `sqlite3.Row` instances, enabling both name-based key indexing (`row['salary']`) and integer index access (`row[2]`).

**🔍 Technical Deep-Dive & Syntax:**  
```python
import sqlite3
conn = sqlite3.connect('company.db')
conn.row_factory = sqlite3.Row # Enable name-based access
cursor = conn.cursor()
cursor.execute('SELECT emp_id, name, salary FROM employees')
row = cursor.fetchone()
print(row['name'], row['salary']) # Name access
print(row[0])                    # Index access also works!
print(row.keys())                # Lists column names: ['emp_id', 'name', 'salary']
```
In MySQL, the equivalent is `cursor = conn.cursor(dictionary=True)`.
In PostgreSQL, the equivalent is `cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Is sqlite3.Row a true Python dict?' Answer: No, it is an optimized C-based mapping object that behaves like a dictionary and a tuple. To convert it into a pure dictionary, call `dict(row)`.

---

### Q28. What is the catastrophic risk of executing `UPDATE` or `DELETE` statements without a `WHERE` clause?

> 🎯 **Core Answer:**  
> An `UPDATE` or `DELETE` statement without a `WHERE` filtering clause executes unconditionally across every single record in the entire table. In an `UPDATE`, every row has its column overwritten; in a `DELETE`, all records are permanently erased.

**🔍 Technical Deep-Dive & Syntax:**  
Example:
`cursor.execute("UPDATE employees SET salary = 100000")` overwrites the salary of EVERY employee in the company to 100,000.
`cursor.execute("DELETE FROM accounts")` wipes all account records in the bank.
Best Practice: Always verify query string syntax and execute with explicit `WHERE id = ?` or use dry-run transactions with `conn.rollback()` before final commit.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Does the SQL engine prompt for confirmation before deleting all rows?' Answer: No. SQL engines execute statements deterministically as instructed without confirmation prompts.

---

### Q29. Compare `DELETE`, `TRUNCATE`, and `DROP` in terms of SQL category, execution speed, rollback capability, and schema retention.

> 🎯 **Core Answer:**  
> `DELETE` is a DML command that removes specific or all rows one-by-one, can be rolled back in a transaction, and retains table structure; `TRUNCATE` is a DDL command that swiftly purges all rows by deallocating storage pages, resets identity counters, and retains structure; `DROP` is a DDL command that permanently destroys both the data and the entire table schema definition.

**🔍 Technical Deep-Dive & Syntax:**  
| Feature | `DELETE FROM t` | `TRUNCATE TABLE t` | `DROP TABLE t` |
| :--- | :--- | :--- | :--- |
| SQL Category | DML (Data Manipulation) | DDL (Data Definition) | DDL (Data Definition) |
| WHERE Clause | Supported (`WHERE id=1`) | NOT Supported | NOT Supported |
| Speed | Slower (logs each row delete) | Extremely Fast (page deallocation) | Instantaneous |
| Schema Kept? | YES (Structure preserved) | YES (Empty structure preserved) | NO (Completely obliterated) |
| Auto-Increment | Does NOT reset counter | RESETS auto-increment counter | Destroys table definition |
| Rollback | Fully rollable in transaction | Cannot be rolled back in most DBs | Cannot be rolled back |

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Does SQLite support TRUNCATE TABLE?' Answer: No! SQLite does not implement the `TRUNCATE` keyword. Running `DELETE FROM table;` in SQLite achieves equivalent optimization if SQLite's truncate optimization is active.

---

### Q30. Differentiate between `WHERE` and `HAVING` clauses in SQL. Why can't aggregate functions appear in a `WHERE` clause?

> 🎯 **Core Answer:**  
> `WHERE` filters individual raw rows BEFORE any grouping or aggregation takes place; `HAVING` filters aggregated group records AFTER the `GROUP BY` stage. Aggregate functions (`AVG`, `SUM`, `COUNT`) cannot appear in `WHERE` because individual rows do not yet possess aggregated group values.

**🔍 Technical Deep-Dive & Syntax:**  
Query Processing Pipeline Order:
1. `FROM` & `JOIN`: Collect all participating tables.
2. `WHERE`: Filter individual raw tuples. (Aggregates NOT allowed here!).
3. `GROUP BY`: Partition remaining rows into category groups.
4. `HAVING`: Filter groups based on aggregate criteria (e.g. `HAVING AVG(salary) > 50000`).
5. `SELECT`: Project columns and compute aliases.
6. `ORDER BY`: Sort the final output.
7. `LIMIT`: Restrict output row count.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you use HAVING without GROUP BY?' Answer: Yes! If `HAVING` is used without `GROUP BY`, the entire table is treated as a single aggregate group (e.g. `SELECT AVG(salary) FROM emp HAVING AVG(salary) > 50000`).

---

### Q31. Explain the ACID properties of database transactions using a banking fund transfer scenario ($500 from Alice to Bob).

> 🎯 **Core Answer:**  
> ACID guarantees transactional reliability:
• Atomicity: Either both debit ($500 from Alice) and credit ($500 to Bob) succeed, or neither happens.
• Consistency: Total system funds remain constant; balances cannot violate constraints like `CHECK (balance >= 0)`.
• Isolation: Concurrent transfers on Alice's account execute without reading intermediate uncommitted balances.
• Durability: Once committed, the transfer records persist permanently even if power fails immediately.

**🔍 Technical Deep-Dive & Syntax:**  
1. Atomicity: If power dies right after deducting from Alice, the database rolls back, preventing Alice's money from vanishing.
2. Consistency: If Alice has only $300, a `CHECK (balance >= 0)` constraint prevents the transaction from completing, maintaining valid state.
3. Isolation: Bob checking his balance during the transfer sees either pre-transfer balance or post-transfer balance, never a half-committed state.
4. Durability: Once `conn.commit()` returns success, transaction logs are written to write-ahead logs (WAL) on disk, surviving crashes.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What isolation problem occurs when one transaction reads uncommitted changes of another?' Answer: A Dirty Read (mitigated by Read Committed or Serializable isolation levels).

---

### Q32. What SQL joins are supported natively in SQLite? How can a FULL OUTER JOIN be achieved in SQLite?

> 🎯 **Core Answer:**  
> SQLite natively supports `INNER JOIN`, `LEFT OUTER JOIN`, and `CROSS JOIN`. It does NOT natively support `RIGHT OUTER JOIN` or `FULL OUTER JOIN`. A FULL OUTER JOIN is simulated in SQLite by combining a `LEFT OUTER JOIN` with a simulated right join using `UNION`.

**🔍 Technical Deep-Dive & Syntax:**  
Simulating FULL OUTER JOIN in SQLite:
```sql
-- Left join part
SELECT a.id, a.val, b.val FROM TableA a LEFT JOIN TableB b ON a.id = b.id
UNION
-- Right join simulated by swapping table order
SELECT b.id, a.val, b.val FROM TableB b LEFT JOIN TableA a ON a.id = b.id;
```
`UNION` automatically deduplicates common overlapping records produced by both queries, yielding an exact FULL OUTER JOIN result.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Why use UNION instead of UNION ALL when simulating FULL OUTER JOIN?' Answer: `UNION ALL` retains duplicate rows, which would cause rows matching in both tables to appear twice! `UNION` eliminates the duplicates.

---

### Q33. What is a Foreign Key constraint, and what does `ON DELETE CASCADE` guarantee in a relational database?

> 🎯 **Core Answer:**  
> A Foreign Key establishes referential integrity by linking a column in a child table to the Primary Key of a parent table. `ON DELETE CASCADE` guarantees that when a record in the parent table is deleted, all corresponding dependent child rows are automatically deleted by the database engine.

**🔍 Technical Deep-Dive & Syntax:**  
Example:
```sql
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER REFERENCES departments(dept_id) ON DELETE CASCADE
);
```
If Department `DEPT1` is deleted, all employees belonging to `DEPT1` are automatically purged by the database engine, preventing orphaned foreign keys.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What happens in SQLite if foreign keys are not enabled?' Answer: By default, SQLite has foreign key enforcement turned OFF for backwards compatibility! You must explicitly execute `PRAGMA foreign_keys = ON;` in SQLite to enforce constraints.

---

### Q34. What is a Bridge (Junction / Associative) table? Why is it essential for Many-to-Many relationships?

> 🎯 **Core Answer:**  
> A Bridge (or Junction) table resolves a Many-to-Many (M:N) relationship between two entities into two clean One-to-Many (1:N) relationships. Relational databases cannot directly implement M:N links without massive data duplication; the junction table stores composite primary keys from both entities.

**🔍 Technical Deep-Dive & Syntax:**  
Example: Students and Courses.
One student enrolls in many courses; one course contains many students.
Bridge Table: `Enrollment(student_id, course_id, enrollment_date, grade)`.
• Primary Key: Composite key `(student_id, course_id)`.
• Foreign Keys: `student_id` references `Student(id)`, `course_id` references `Course(id)`.
Attributes specific to the relationship itself (such as `enrollment_date` or `grade`) reside naturally inside the bridge table.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you store a comma-separated list of course IDs inside a single Student table column instead?' Answer: Absolutely not! Storing comma-separated lists violates First Normal Form (1NF) requiring atomic values, completely prevents indexing, and makes JOIN queries impossible.

---

### Q35. How do `pd.read_sql_query()` and `df.to_sql()` integrate Pandas with SQL databases? What does `if_exists='replace'` do?

> 🎯 **Core Answer:**  
> `pd.read_sql_query(sql, conn)` executes a query and loads results directly into a DataFrame. `df.to_sql('table_name', conn)` exports a DataFrame into an SQL table. The parameter `if_exists='replace'` drops the existing table and recreates it with new DataFrame data.

**🔍 Technical Deep-Dive & Syntax:**  
`df.to_sql()` options for `if_exists`:
• `'fail'` (Default): Raises a `ValueError` if table already exists.
• `'replace'`: Drops the table completely and recreates schema from DataFrame.
• `'append'`: Preserves existing table schema and appends DataFrame rows.
```python
# Loading SQL query into DataFrame
df = pd.read_sql_query("SELECT * FROM patients WHERE age > 50", conn)

# Writing DataFrame to SQL
df.to_sql('senior_patients', conn, if_exists='append', index=False)
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is the danger of using if_exists='replace' in an operational production database?' Answer: It drops the existing table, permanently destroying all existing primary key indices, foreign key constraints, triggers, and historical records!

---

## SECTION 4: UNIT 3 VIVA QUESTIONS – DATA CLEANUP & PREPROCESSING

### Q36. What are the 6 dimensions of data quality? Give a concrete real-world violation for each dimension.

> 🎯 **Core Answer:**  
> The six standardized dimensions of data quality are: (1) Accuracy, (2) Completeness, (3) Consistency, (4) Timeliness, (5) Validity, and (6) Uniqueness.

**🔍 Technical Deep-Dive & Syntax:**  
1. Accuracy: Real-world correctness. Violation: Patient body temperature recorded as 450°C instead of 45.0°C.
2. Completeness: Absence of missing data. Violation: An online loan application submitted with a blank Monthly Income field.
3. Consistency: Uniformity across disparate systems. Violation: Customer marked as 'Active' in CRM table but 'Closed' in Core Banking table.
4. Timeliness: Currency of information. Violation: Running 2026 demand forecasting using 2015 census demographic figures.
5. Validity: Conformity to business rules/schemas. Violation: Customer age entered as -25 or email entered as 'john#gmail'.
6. Uniqueness: Absence of redundant entities. Violation: The same customer registered twice with two different CustomerIDs due to typo in name.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is the difference between Accuracy and Validity?' Answer: Validity means the data conforms to the expected format/rules (e.g. '9999-99-99' is syntactically a valid date string format), whereas Accuracy means it reflects real-world truth (the year 9999 is factually inaccurate).

---

### Q37. Explain the three theoretical missing data mechanisms: MCAR, MAR, and MNAR with practical examples.

> 🎯 **Core Answer:**  
> • MCAR (Missing Completely at Random): Missingness has zero relationship to any observed or unobserved data.
• MAR (Missing at Random): Missingness depends on other observed variables, but not the missing value itself.
• MNAR (Missing Not at Random): Missingness depends directly on the unobserved missing value itself.

**🔍 Technical Deep-Dive & Syntax:**  
• MCAR: A physical laboratory test tube is accidentally dropped and shattered on the floor. Missingness is completely independent of test results or patient health.
• MAR: In an employee survey, female employees are statistically less likely to report their weight than male employees. The missingness depends on observed gender, but within females, it is random.
• MNAR: High-earning individuals ($500k+) refuse to report their annual income on tax surveys because their income is high. The missingness is directly caused by the high value of the variable itself!

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you simply drop missing rows if data is MNAR?' Answer: No! Dropping rows when data is MNAR introduces severe systematic bias into the dataset because you are selectively discarding high-value entities.

---

### Q38. How do you detect missing values in Pandas? What is the difference between `isna()` and `isnull()`?

> 🎯 **Core Answer:**  
> Use `df.isnull().sum()` or `df.isna().sum()` to count missing values per column. In Pandas, `isna()` and `isnull()` are exact functional aliases of each other with zero performance or behavioral difference.

**🔍 Technical Deep-Dive & Syntax:**  
```python
# Count missing values per column
missing_counts = df.isnull().sum()

# Percentage of missingness
missing_pct = df.isnull().mean() * 100

# Check if ANY missing value exists in DataFrame
has_nulls = df.isnull().values.any()
```
Historical Context: In R (which influenced Pandas), `is.na` detects missing values (NA) while `is.null` detects empty object references (NULL). To make R users comfortable while adhering to Python conventions, Pandas created `isna()` and aliased it to `isnull()`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Does isnull() detect empty strings like "" or whitespace "   "?' Answer: No! `isnull()` detects only `None` and `numpy.nan`. Empty strings `""` or spaces are valid string objects and must be replaced using `df.replace('', np.nan)` before detection.

---

### Q39. When should you use Mean vs Median vs Mode vs Forward Fill for missing data imputation?

> 🎯 **Core Answer:**  
> Use Mean for symmetric, normally distributed numerical data without outliers; use Median for skewed numerical data or datasets with severe outliers; use Mode (or placeholder 'Unknown') for categorical data; use Forward Fill (`ffill`) for temporal time-series data.

**🔍 Technical Deep-Dive & Syntax:**  
• Mean: Highly sensitive to extreme values. Imputing with mean preserves overall sum, but skews distributions if outliers exist.
• Median: Robust non-parametric metric. If salary data has extremes (CEO earning $5M vs workers $50k), median reflects typical employee income accurately.
• Mode: Most frequent class for nominal variables (e.g. imputing missing blood groups).
• Forward Fill (`df['stock'].ffill()`): Propagates last known valid price forward in financial time series where yesterday's closing price is the best estimate of today's missing tick.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'If you impute 1,000 missing values with the mean, what happens to the column's variance and standard deviation?' Answer: The variance and standard deviation decrease because adding identical mean values clusters more data at the center!

---

### Q40. What happens when you execute `pd.to_numeric(df['Age'], errors='coerce')`? Why does the column become `float64` instead of `int64`?

> 🎯 **Core Answer:**  
> `errors='coerce'` converts unparseable string values (e.g. 'Thirty', 'Unknown', '#NA') into `numpy.nan`. The column becomes `float64` because in standard Pandas, integer arrays (`int64`) cannot represent `NaN`, which is defined as an IEEE 754 floating-point standard.

**🔍 Technical Deep-Dive & Syntax:**  
Code Example:
```python
df = pd.DataFrame({'Age': [25, 'Thirty', 29, None]})
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
# Output:
# 0    25.0
# 1     NaN   <- 'Thirty' coerced to NaN
# 2    29.0
# 3     NaN
# dtype: float64
```
Note: In modern Pandas, you can cast to nullable integer type `df['Age'].astype('Int64')` (capital 'I') which supports integer `pd.NA` without converting to float.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What happens if errors='ignore' was used instead?' Answer: If conversion fails, Pandas silently aborts the conversion and leaves the entire column completely unchanged as `object` (string) dtype!

---

### Q41. Explain the three modes of the `errors` parameter in Pandas conversion functions (`'raise'`, `'coerce'`, `'ignore'`).

> 🎯 **Core Answer:**  
> • `'raise'` (Default): Raises a `ValueError` immediately upon encountering an invalid parsing value, halting script execution.
• `'coerce'`: Forces invalid values to be converted to `NaN` (or `NaT` for datetime).
• `'ignore'`: Suppresses errors silently and returns the original input unmodified.

**🔍 Technical Deep-Dive & Syntax:**  
```python
# 'raise' (halting exception):
pd.to_numeric(['10', 'bad'], errors='raise') # Raises ValueError

# 'coerce' (safe fallback):
pd.to_numeric(['10', 'bad'], errors='coerce') # Returns [10.0, NaN]

# 'ignore' (silent bypass):
pd.to_numeric(['10', 'bad'], errors='ignore') # Returns array(['10', 'bad'], dtype=object)
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Is errors='ignore' deprecated in latest Pandas versions?' Answer: Yes, `errors='ignore'` in `to_datetime` and `to_numeric` has been deprecated in recent Pandas 2.2+ because silent bypasses hide critical data parsing bugs.

---

### Q42. What is Tukey's Interquartile Range (IQR) method? State the exact mathematical formulas for IQR, Lower Fence, and Upper Fence.

> 🎯 **Core Answer:**  
> Tukey's IQR method is a non-parametric outlier detection technique based on the spread of the middle 50% of data. Any data point lying outside the lower and upper fences is flagged as an outlier.

**🔍 Technical Deep-Dive & Syntax:**  
Mathematical Formulas:
$$\text{IQR} = Q3 - Q1$$
$$\text{Lower Bound / Fence} = Q1 - (1.5 \times \text{IQR})$$
$$\text{Upper Bound / Fence} = Q3 + (1.5 \times \text{IQR})$$
$$\text{Extreme Outlier Boundaries} = Q1 - 3.0 \times \text{IQR} \quad \text{and} \quad Q3 + 3.0 \times \text{IQR}$$
Where $Q1$ is the 25th percentile and $Q3$ is the 75th percentile.
Code Implementation:
```python
q1 = df['val'].quantile(0.25)
q3 = df['val'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['val'] < q1 - 1.5 * iqr) | (df['val'] > q3 + 1.5 * iqr)]
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Given Q1 = 100, Q3 = 160. Calculate the upper outlier boundary.'
Answer: IQR = 160 - 100 = 60. Upper Fence = 160 + (1.5 * 60) = 160 + 90 = 250.

---

### Q43. Why is 1.5 used as the multiplier in Tukey's IQR rule? What multiplier is used for extreme outliers?

> 🎯 **Core Answer:**  
> John Tukey selected 1.5 because for a Gaussian (normal) distribution, the range $[Q1 - 1.5 \times \text{IQR}, Q3 + 1.5 \times \text{IQR}]$ corresponds to approximately $\pm 2.7\sigma$ from the mean, encompassing ~99.3% of data and flagging only the top/bottom 0.7% as mild outliers. A multiplier of 3.0 is used for extreme outliers (approx. $\pm 4.7\sigma$).

**🔍 Technical Deep-Dive & Syntax:**  
• Mild Outlier Fence: $1.5 \times \text{IQR}$ (captures values beyond 2.7 standard deviations in normal distributions).
• Extreme Outlier Fence: $3.0 \times \text{IQR}$ (captures values beyond 4.7 standard deviations; probability of occurrence under normal distribution is < 0.0002%).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Does Tukey's IQR method assume normal distribution?' Answer: No! It is a non-parametric method based on percentiles, meaning it works effectively on any distribution shape (skewed, uniform, bimodal).

---

### Q44. What is the Z-score method for outlier detection and what is the empirical 3-sigma rule?

> 🎯 **Core Answer:**  
> The Z-score measures how many standard deviations an observation $X$ lies away from the mean $\mu$: $Z = \frac{X - \mu}{\sigma}$. The 3-sigma rule states that for a Gaussian distribution, 99.73% of observations fall within $|Z| \le 3$; any point with $|Z| > 3$ is classified as an outlier.

**🔍 Technical Deep-Dive & Syntax:**  
Empirical Rule Distribution Breakdown:
• Within $\pm 1\sigma$ ($|Z| \le 1$): ~68.27% of data.
• Within $\pm 2\sigma$ ($|Z| \le 2$): ~95.45% of data.
• Within $\pm 3\sigma$ ($|Z| \le 3$): ~99.73% of data.
• Outside $\pm 3\sigma$ ($|Z| > 3$): Top/Bottom 0.27% (severe outliers).
```python
from scipy import stats
z_scores = np.abs(stats.zscore(df['Sales']))
outliers = df[z_scores > 3]
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you use Z-score on heavily skewed or non-normal data?' Answer: No! The Z-score relies on the mean and standard deviation, which are heavily distorted by skewness and extreme outliers. For non-normal data, Tukey's IQR or Median Absolute Deviation (MAD) is preferred.

---

### Q45. How does Pandas `df.duplicated()` handle `keep='first'`, `keep='last'`, and `keep=False`?

> 🎯 **Core Answer:**  
> `keep='first'` marks all duplicate rows as `True` except the first occurrence; `keep='last'` marks all duplicates as `True` except the last occurrence; `keep=False` marks ALL occurrences of duplicate rows as `True` without preserving any.

**🔍 Technical Deep-Dive & Syntax:**  
Given IDs: `[101, 102, 101, 103, 101]`:
• `keep='first'` ➔ `[False, False, True, False, True]` (Keeps index 0; drops 2, 4).
• `keep='last'` ➔ `[True, False, True, False, False]` (Keeps index 4; drops 0, 2).
• `keep=False` ➔ `[True, False, True, False, True]` (Flags every instance of ID 101; useful for auditing conflicting records before deciding which one is correct).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What does df.drop_duplicates(keep=False) do?' Answer: It deletes ALL rows that have duplicate entries, keeping only rows that were completely unique from the start!

---

### Q46. What is Levenshtein Distance? What are the three allowable single-character edit operations?

> 🎯 **Core Answer:**  
> Levenshtein Distance is an edit-distance metric that counts the minimum number of single-character operations required to transform one string into another. The three allowable operations are: (1) Insertion, (2) Deletion, and (3) Substitution.

**🔍 Technical Deep-Dive & Syntax:**  
Example: Converting 'kitten' to 'sitting':
1. Substitute 'k' ➔ 's' ('sitten')
2. Substitute 'e' ➔ 'i' ('sittin')
3. Insert 'g' at end ('sitting')
Total edits = 3 ➔ Levenshtein Distance = 3.
If two strings are identical, distance is 0. If strings are completely disjoint, distance equals the length of the longer string.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Does Levenshtein distance allow character transposition (swapping adjacent letters)?' Answer: Standard Levenshtein does NOT treat transposition as a single edit (it counts as 2 edits: substitution or deletion+insertion). The Damerau-Levenshtein distance variant adds transposition as a 4th operation.

---

### Q47. In `fuzzywuzzy`, compare `fuzz.ratio()`, `fuzz.partial_ratio()`, `fuzz.token_sort_ratio()`, and `fuzz.token_set_ratio()`.

> 🎯 **Core Answer:**  
> • `fuzz.ratio`: Standard edit distance similarity (0-100); sensitive to order and length.
• `fuzz.partial_ratio`: Substring matching; finds best matching substring of shorter string.
• `fuzz.token_sort_ratio`: Tokenizes, sorts words alphabetically, then compares; handles out-of-order words.
• `fuzz.token_set_ratio`: Takes intersection and remainder token sets; handles duplicate words and varying lengths.

**🔍 Technical Deep-Dive & Syntax:**  
Scoring Matrix Example:
| String 1 | String 2 | `ratio` | `partial_ratio` | `token_sort_ratio` | `token_set_ratio` |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 'John Smith' | 'Smith John' | 60 | 60 | **100** | **100** |
| 'Apple' | 'Apple Inc Corp' | 53 | **100** | 53 | **100** |
| 'Google' | 'Google Google Inc' | 48 | **100** | 52 | **100** |

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Which function is best for matching company names like 'Amazon India Pvt Ltd' vs 'Amazon'?' Answer: `fuzz.token_set_ratio`, because it isolates intersecting common tokens ('Amazon') and ignores extra suffix tokens.

---

### Q48. How does `process.extractOne()` work for fuzzy record linkage? What does it return?

> 🎯 **Core Answer:**  
> `process.extractOne(query, choices, scorer=...)` searches a list/array of candidate strings (`choices`) and returns the single candidate that yields the highest fuzzy similarity score with `query`.

**🔍 Technical Deep-Dive & Syntax:**  
```python
from fuzzywuzzy import process, fuzz
choices = ['Chennai', 'Bangalore', 'Mumbai', 'Hyderabad']
best_match = process.extractOne('chenai', choices, scorer=fuzz.ratio)
# Returns a tuple: ('Chennai', 92)
matched_city, score = best_match
if score >= 85:
    clean_city = matched_city
```
Return Structure: A 2-tuple `(matched_string, similarity_score)` or 3-tuple including the index in the original list.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What does process.extract() return compared to extractOne()?' Answer: `process.extract()` returns a list of top-N matches (default `limit=5`), whereas `extractOne()` returns only the single top-scoring match.

---

### Q49. In Python's `re` module, what is the difference between `re.match()`, `re.search()`, `re.findall()`, and `re.sub()`?

> 🎯 **Core Answer:**  
> • `re.match()`: Matches only from the very beginning (index 0) of the string.
• `re.search()`: Scans the entire string and returns the first match anywhere.
• `re.findall()`: Scans the entire string and returns all non-overlapping matches as a list of strings.
• `re.sub()`: Substitutes/replaces matches with a specified replacement string.

**🔍 Technical Deep-Dive & Syntax:**  
Code Demonstration:
```python
text = "Phone: 98401, Alt: 98402"
re.match(r'\d+', text)    # None (because text starts with 'Phone', not digits)
re.search(r'\d+', text)   # <Match object; span=(7, 12), match='98401'>
re.findall(r'\d+', text)  # ['98401', '98402']
re.sub(r'\d+', 'XXX', text) # 'Phone: XXX, Alt: XXX'
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What does re.finditer() return?' Answer: `re.finditer()` returns a lazy iterator yielding `Match` objects (allowing extraction of start/end index spans using `.start()` and `.end()`), saving memory on massive text files.

---

### Q50. Explain regex metacharacters: `\d`, `\D`, `\w`, `\W`, `\s`, `\S`, `^`, `$`, `*`, `+`, `?`, `{n,m}`.

> 🎯 **Core Answer:**  
> • `\d` / `\D`: Digit `[0-9]` / Non-digit.
• `\w` / `\W`: Word character `[a-zA-Z0-9_]` / Non-word character.
• `\s` / `\S`: Whitespace `[ \t\n\r]` / Non-whitespace.
• `^` / `$`: Start of string / End of string.
• `*`: 0 or more occurrences (greedy).
• `+`: 1 or more occurrences (greedy).
• `?`: 0 or 1 occurrence (optional).
• `{n,m}`: Between $n$ and $m$ repetitions.

**🔍 Technical Deep-Dive & Syntax:**  
Examples:
• `^\d{10}$`: Matches exactly 10 digits from start to end.
• `\s+`: Matches one or more consecutive spaces/tabs.
• `https?`: Matches 'http' or 'https' ('s' is optional).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What does [^0-9] mean compared to ^[0-9]?' Answer: `^[0-9]` matches a digit at the start of the string. `[^0-9]` inside square brackets is a negated character class matching any non-digit character (equivalent to `\D`).

---

### Q51. How do you strip all non-alphanumeric special characters and punctuation from text using regex?

> 🎯 **Core Answer:**  
> Use `re.sub(r'[^a-zA-Z0-9\s]', '', text)`. This replaces every character that is NOT a letter, digit, or whitespace with an empty string.

**🔍 Technical Deep-Dive & Syntax:**  
```python
import re
raw = "Order #1234-A: Price is $45.99 (50% OFF)!!"
clean = re.sub(r'[^a-zA-Z0-9\s]', '', raw)
# Output: 'Order 1234A Price is 4599 50 OFF'
```
To collapse multiple spaces into a single space: `re.sub(r'\s+', ' ', clean).strip()`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What happens if you omit \s from the character class?' Answer: All spaces will be deleted as well, collapsing all words into a single continuous unreadable string: 'Order1234APriceis459950OFF'.

---

### Q52. Compare Min-Max Normalization ($[0, 1]$) and Z-Score Standardization ($\mu=0, \sigma=1$). How do outliers affect each?

> 🎯 **Core Answer:**  
> Min-Max Normalization bounds feature values strictly to the range $[0, 1]$ using $X_{\text{norm}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}$; Z-score Standardization transforms features to have Mean $= 0$ and Std $= 1$ using $Z = \frac{X - \mu}{\sigma}$. Min-Max is heavily crushed by outliers; Z-score handles outliers gracefully.

**🔍 Technical Deep-Dive & Syntax:**  
Outlier Impact:
• Min-Max: If an extreme high outlier exists ($X_{\max} = 100,000$), the denominator becomes massive, squashing all standard data points into a narrow cluster between 0.001 and 0.002.
• Z-Score: Unbounded. Preserves outlier distances from the mean while centering distribution at zero. Recommended for neural networks, linear regression, and PCA.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'When is Min-Max normalization preferred over Z-score?' Answer: In algorithms that require bounded inputs strictly in $[0, 1]$, such as Image Processing (pixel values 0-255 scaled to 0-1) and K-Nearest Neighbors (KNN) where bounded distance metrics are critical.

---

### Q53. What is One-Hot Encoding (`pd.get_dummies()`) and why is `drop_first=True` often used?

> 🎯 **Core Answer:**  
> One-Hot Encoding converts categorical variables into multiple binary (0 or 1) indicator columns. `drop_first=True` drops the first dummy category to eliminate multicollinearity (the 'Dummy Variable Trap') in linear models.

**🔍 Technical Deep-Dive & Syntax:**  
Example: Column `Department` with values `['CSE', 'ECE', 'MECH']`.
Without `drop_first`:
Creates 3 columns: `Dept_CSE`, `Dept_ECE`, `Dept_MECH`.
Notice: If an employee is NOT in ECE and NOT in MECH, they are guaranteed to be in CSE! The sum of the columns is always 1 (`Dept_CSE + Dept_ECE + Dept_MECH = 1`), causing perfect linear dependency (singular covariance matrix in Linear Regression).
With `drop_first=True`:
Creates 2 columns: `Dept_ECE`, `Dept_MECH`. When both are 0, it implicitly represents CSE.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Is drop_first=True needed for tree-based models like Random Forest or XGBoost?' Answer: No! Decision trees do not compute matrix inversions and are immune to multicollinearity.

---

### Q54. Why are data cleaning pipelines packaged into modular, idempotent Python functions in production ETL systems?

> 🎯 **Core Answer:**  
> Packaging cleaning into modular, parameterized functions ensures reusability, testability, and idempotence (running the function multiple times produces the identical clean state without side effects), eliminating training-serving skew between model development and real-time inference.

**🔍 Technical Deep-Dive & Syntax:**  
Production Architecture:
```python
def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset=['id'], keep='first')
    df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(df['age'].median())
    df['phone'] = df['phone'].astype(str).str.replace(r'\D', '', regex=True).str[-10:]
    return df
```
Benefits:
1. Unit Testing: Automated PyTest test suites can verify cleaning rules on mock synthetic datasets.
2. Idempotence: `clean(clean(df)) == clean(df)`.
3. Skew Prevention: Exactly the same script runs on offline training batches and live incoming REST API streaming payloads.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is training-serving skew?' Answer: When data preprocessing applied during offline model training differs from preprocessing applied to live production data, degrading model accuracy.

---

### Q55. What is catastrophic backtracking in regular expressions and how can it be avoided?

> 🎯 **Core Answer:**  
> Catastrophic backtracking occurs when a non-deterministic regex engine evaluates nested, overlapping ambiguous quantifiers (such as `(a+)+` or `(a|a)+`) against non-matching text (like 'aaaaaX'), causing the engine to test an exponential number of permutations ($O(2^n)$), freezing the CPU.

**🔍 Technical Deep-Dive & Syntax:**  
Example:
Pattern `(a+)+$` matching against `'aaaaaaaaaaaaaaaaaaaaX'`.
For each character, the outer quantifier and inner quantifier create overlapping branch combinations. For 30 characters, the engine evaluates over 1 billion backtrack states, causing thread lockup (Regular Expression Denial of Service - ReDoS).
Prevention:
1. Eliminate nested quantifiers.
2. Use atomic grouping `(?>...)` or possessive quantifiers `a++`.
3. Use explicit character classes: replace `.*` with negated classes `[^"\n]*`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is ReDoS?' Answer: Regular Expression Denial of Service: an attack where malicious users supply strings designed to trigger catastrophic backtracking, consuming 100% server CPU and crashing web services.

---

## SECTION 5: UNIT 4 VIVA QUESTIONS – EXPLORATORY DATA ANALYSIS & ANALYTICS

### Q56. What is Exploratory Data Analysis (EDA) and what are its primary objectives according to John Tukey?

> 🎯 **Core Answer:**  
> Exploratory Data Analysis (EDA) is an investigative analytical philosophy that employs summary statistics and graphical visualizations to maximize insight into a dataset, uncover underlying structure, detect anomalies and outliers, test hypotheses, and check model assumptions before formal predictive modeling.

**🔍 Technical Deep-Dive & Syntax:**  
Primary Objectives:
1. Data Validation: Verify expected distributions, formats, and ranges.
2. Anomaly Detection: Detect data entry glitches, measurement sensor faults, or severe outliers.
3. Relationship Discovery: Uncover correlations, clusters, and associations between features.
4. Feature Selection: Determine which variables have predictive power.
5. Model Selection: Check statistical assumptions (e.g. normality, linearity, homoscedasticity).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you skip EDA if you have an automated AutoML tool?' Answer: No! AutoML cannot understand domain context, ethical biases, measurement errors, or data leakage.

---

### Q57. Explain the Split-Apply-Combine strategy in data analysis. How is it implemented in Pandas?

> 🎯 **Core Answer:**  
> Split-Apply-Combine is an analytical paradigm where data is: (1) Split into distinct groups based on categorical keys, (2) Apply an independent computation (aggregation, transformation, or filtering) to each group, and (3) Combine the results into a unified output table. In Pandas, it is implemented via `df.groupby()`.

**🔍 Technical Deep-Dive & Syntax:**  
Stages:
• Split: `grouped = df.groupby('Department')` partitions the DataFrame into departmental slices.
• Apply: `.agg({'Salary': 'mean'})` computes the average salary for each slice.
• Combine: Pandas merges the resulting scalar means into a single summary DataFrame indexed by Department.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Does df.groupby() immediately compute data in memory?' Answer: No! `df.groupby()` is lazy; it creates a `DataFrameGroupBy` object and only executes computation when an aggregation method (like `.sum()`, `.mean()`, `.agg()`) is called.

---

### Q58. Compare `.loc[]` vs `.iloc[]` in Pandas. What are the indexing mechanisms and slice boundary rules for each?

> 🎯 **Core Answer:**  
> `.loc[]` is label-based indexing using row index names and column names, and its slice end-boundary is strictly INCLUSIVE. `.iloc[]` is integer-position-based indexing using integer offsets from 0 to $N-1$, and its slice stop-boundary is strictly EXCLUSIVE.

**🔍 Technical Deep-Dive & Syntax:**  
Comparison:
```python
# .loc (Label-based, INCLUSIVE of end label):
df.loc['2025-01':'2025-03', ['Sales', 'Profit']]
# Slices January, February, AND March (all 3 months included!).

# .iloc (Integer-based, EXCLUSIVE of stop index):
df.iloc[0:3, 0:2]
# Slices rows 0, 1, 2 (row 3 is EXCLUDED) and columns 0, 1 (col 2 is EXCLUDED).
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'If a DataFrame has default integer index [0, 1, 2, 3], what does df.loc[0:2] return vs df.iloc[0:2]?' Answer: `df.loc[0:2]` returns 3 rows (labels 0, 1, 2)! `df.iloc[0:2]` returns only 2 rows (offsets 0, 1)!

---

### Q59. Why must bitwise operators (`&`, `|`, `~`) with parentheses be used for Pandas boolean filtering instead of standard Python keywords (`and`, `or`, `not`)?

> 🎯 **Core Answer:**  
> Standard Python `and`, `or`, `not` evaluate the truth value of an entire object as a single truthy/falsy scalar. A Pandas Series contains multiple Boolean elements, raising `ValueError: The truth value of a Series is ambiguous`. Bitwise operators (`&`, `|`, `~`) perform element-wise vector operations across the entire Series.

**🔍 Technical Deep-Dive & Syntax:**  
Why parentheses are required:
In Python's operator precedence table, bitwise operators (`&`, `|`) have HIGHER precedence than comparison operators (`>`, `<`, `==`).
Writing `df['age'] > 20 & df['salary'] < 50000` evaluates as `df['age'] > (20 & df['salary']) < 50000`, causing syntax crashes.
Wrapping in parentheses: `(df['age'] > 20) & (df['salary'] < 50000)` guarantees comparisons evaluate first.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'How does the .query() method bypass this?' Answer: `df.query('age > 20 and salary < 50000')` accepts clean string expressions where standard 'and'/'or' keywords are parsed internally.

---

### Q60. What is the operational difference between `df.groupby().agg()` and `df.groupby().transform()`?

> 🎯 **Core Answer:**  
> `.agg()` collapses/reduces each group into a single summary row, producing an output DataFrame whose row count equals the number of unique groups. `.transform()` computes the group-level statistic and broadcasts it back to every row in the original DataFrame, maintaining the exact original row count.

**🔍 Technical Deep-Dive & Syntax:**  
Demonstration:
```python
# .agg (collapses):
df.groupby('dept')['salary'].agg('mean')
# Output: 3 rows (one per dept: CSE, ECE, MECH)

# .transform (broadcasts):
df['dept_avg'] = df.groupby('dept')['salary'].transform('mean')
# Output: 100 rows (each employee gets their department's average salary alongside their own)
```
`.transform()` is ideal for calculating relative metrics, such as employee salary deviation from department mean: `df['diff'] = df['salary'] - df['dept_avg']`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you use .transform() to add a percentage share column?' Answer: Yes! `df['share'] = df['sales'] / df.groupby('region')['sales'].transform('sum') * 100` calculates each store's percentage share of regional sales.

---

### Q61. Differentiate between `pd.merge()` and `pd.concat()`. What do `axis=0` and `axis=1` signify in `pd.concat()`?

> 🎯 **Core Answer:**  
> `pd.merge()` performs relational database-style joins based on matching key column values (like SQL `JOIN`). `pd.concat()` stitches/stacks DataFrames along an axis without evaluating key value matches. `axis=0` stacks rows vertically; `axis=1` aligns index and concatenates columns horizontally.

**🔍 Technical Deep-Dive & Syntax:**  
• `pd.merge(df1, df2, on='student_id', how='inner')`: Matches records where `student_id` is equal.
• `pd.concat([df_jan, df_feb], axis=0)`: Appends rows of February below January.
• `pd.concat([df_features, df_labels], axis=1)`: Glues feature columns and label columns side-by-side along row index.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What happens if you use pd.concat(axis=1) on DataFrames with non-matching index labels?' Answer: Pandas performs an outer join on the index, filling unmatched row entries with `NaN`!

---

### Q62. What is an Anti-Join? How is it implemented in Pandas?

> 🎯 **Core Answer:**  
> An Anti-Join returns all rows from the Left DataFrame that have NO matching key in the Right DataFrame. In Pandas, it is implemented by negating the `.isin()` membership operator: `df1[~df1['key'].isin(df2['key'])]`.

**🔍 Technical Deep-Dive & Syntax:**  
Use Case: Identify customers who have never placed an order.
```python
# Anti-Join:
non_purchasers = customers[~customers['cust_id'].isin(orders['cust_id'])]
```
Alternative Implementation: Performing an outer merge with indicator:
```python
merged = pd.merge(customers, orders, on='cust_id', how='left', indicator=True)
anti_join = merged[merged['_merge'] == 'left_only']
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Does SQL have an ANTI JOIN keyword?' Answer: Standard ANSI SQL does not have a native `ANTI JOIN` keyword; it is written as `SELECT * FROM A WHERE NOT EXISTS (SELECT 1 FROM B WHERE A.id = B.id)` or `A LEFT JOIN B ON ... WHERE B.id IS NULL`.

---

### Q63. What is a Semi-Join and how is it implemented in Pandas?

> 🎯 **Core Answer:**  
> A Semi-Join returns rows from the Left DataFrame that have at least one match in the Right DataFrame, but unlike an inner join, it does NOT duplicate left rows and does NOT pull columns from the right table. In Pandas, it is implemented using `df1[df1['key'].isin(df2['key'])]`.

**🔍 Technical Deep-Dive & Syntax:**  
Use Case: Filter all departments that have at least one active project.
```python
# Semi-Join:
active_depts = departments[departments['dept_id'].isin(projects['dept_id'])]
```
Why not use Inner Join? If Department 1 has 10 projects, an Inner Join duplicates Department 1 ten times. A Semi-Join preserves Department 1 as a single row.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'How is Semi-Join written in SQL?' Answer: Using `WHERE id IN (SELECT id FROM ...)` or `WHERE EXISTS (...)`.

---

### Q64. What is Pearson Correlation Coefficient ($r$)? What is its valid range and how are $r = 1$, $r = -1$, and $r = 0$ interpreted?

> 🎯 **Core Answer:**  
> Pearson's $r$ measures the strength and direction of a linear relationship between two continuous variables. Its mathematical range is $-1.0 \le r \le +1.0$. $r = +1.0$ indicates a perfect positive linear relationship; $r = -1.0$ indicates a perfect negative (inverse) linear relationship; $r = 0.0$ indicates no linear correlation.

**🔍 Technical Deep-Dive & Syntax:**  
Formula:
$$r = \frac{\sum (X - \bar{X})(Y - \bar{Y})}{\sqrt{\sum (X - \bar{X})^2 \sum (Y - \bar{Y})^2}}$$
Guidelines for Interpretation:
• $|r| \ge 0.7$: Strong linear correlation.
• $0.3 \le |r| < 0.7$: Moderate correlation.
• $|r| < 0.3$: Weak linear correlation.
• $r = 0$: No linear relationship (note: a non-linear relationship like $Y = X^2$ can still exist!).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can Pearson correlation evaluate relationship between categorical variables like Gender and Department?' Answer: No! Pearson correlation requires continuous numeric variables. For categorical associations, Chi-Square test or Cramer's V must be used.

---

### Q65. Compare Pearson linear correlation ($r$) vs Spearman rank correlation ($\rho$). When is Spearman preferred?

> 🎯 **Core Answer:**  
> Pearson ($r$) evaluates strictly linear relationships and assumes continuous, normally distributed variables without outliers. Spearman ($\rho$) evaluates monotonic relationships using ordinal rank values. Spearman is preferred when data is skewed, contains severe outliers, or exhibits non-linear monotonic trends.

**🔍 Technical Deep-Dive & Syntax:**  
Comparison Scenario: $Y = e^X$
• As $X$ increases, $Y$ strictly increases (perfect monotonic relationship).
• Pearson $r \approx 0.72$ (penalized heavily because the curve is non-linear).
• Spearman $\rho = 1.0$ (perfect score because rank ordering is strictly preserved!).
In Pandas:
`df.corr(method='pearson')` vs `df.corr(method='spearman')`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'If two variables have Pearson r = 0, can Spearman rho be non-zero?' Answer: Yes! If the relationship is non-linear but monotonic, Spearman can detect it while Pearson fails.

---

### Q66. Why does correlation not imply causation? What is a lurking / confounding variable?

> 🎯 **Core Answer:**  
> Correlation simply measures statistical co-movement between two variables; it does not prove that changes in variable A cause changes in variable B. A lurking (or confounding) variable is an unmeasured third variable that simultaneously influences both variables, creating a false illusion of direct causation.

**🔍 Technical Deep-Dive & Syntax:**  
Classic Example: Strong positive correlation ($r = 0.88$) between ice cream sales and shark attacks.
• Faulty Conclusion: Eating ice cream attracts sharks.
• Reality: The confounding variable is Summer Temperature. Hot weather causes more people to buy ice cream AND more people to swim in the ocean, driving both numbers up independently.
To prove causation, randomized controlled trials (A/B testing) or causal inference techniques must be used.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can regression analysis prove causation?' Answer: No. Standard regression models only capture statistical associations, not underlying causal mechanisms.

---

### Q67. Compare `pd.pivot_table()` and `pd.crosstab()`. When would you use each?

> 🎯 **Core Answer:**  
> `pd.pivot_table()` aggregates numeric metrics across multiple dimensions with customizable aggregation functions (`sum`, `mean`); `pd.crosstab()` specializes in computing frequency distribution (contingency tables) and percentage cross-tabulations between categorical variables.

**🔍 Technical Deep-Dive & Syntax:**  
• `pd.pivot_table()`:
`pd.pivot_table(df, values='sales', index='region', columns='quarter', aggfunc='sum', margins=True)`
Ideal for business financial summaries.
• `pd.crosstab()`:
`pd.crosstab(df['gender'], df['department'], normalize='index') * 100`
Ideal for computing conditional probabilities and frequency distributions between categorical factors.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can crosstab compute averages?' Answer: Yes! By supplying `values=df['salary']` and `aggfunc='mean'`, `crosstab` can aggregate metrics, but `pivot_table` is more idiomatic for that purpose.

---

### Q68. What are the best visual chart types for: (1) Trends over time, (2) Categorical comparison, (3) Bivariate relationship, (4) Distribution?

> 🎯 **Core Answer:**  
> 1. Trends over time ➔ Line Chart.
2. Categorical comparison ➔ Bar Chart (or Horizontal Bar Chart).
3. Bivariate relationship between two continuous variables ➔ Scatter Plot.
4. Distribution of a single continuous variable ➔ Histogram or Box Plot.

**🔍 Technical Deep-Dive & Syntax:**  
| Analytical Goal | Optimal Visualization | Primary Reason |
| :--- | :--- | :--- |
| Longitudinal Trend | Line Chart | Connects points across continuous temporal axis |
| Category Comparison | Bar Chart | Accurate visual judgment of 1D linear bar lengths |
| Correlation / Scatter | Scatter Plot | Maps Cartesian $(X, Y)$ coordinate patterns |
| Spread & Outliers | Box-and-Whisker Plot | 5-number summary and explicit outlier points |
| Probability Density | KDE / Histogram | Binned frequencies and smooth distribution curves |

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Why not use a line chart to compare sales across 5 departments?' Answer: Line charts imply continuous, ordered connection from one point to the next. Departments are discrete, unordered categories; connecting them with a line implies a non-existent sequence!

---

### Q69. What is a Choropleth Map and when is it used in data visualization?

> 🎯 **Core Answer:**  
> A Choropleth map is a thematic geospatial visualization where predefined geographic areas (such as states, countries, or postal districts) are shaded or patterned in proportion to an aggregate statistical variable (e.g., population density, unemployment rate, election results).

**🔍 Technical Deep-Dive & Syntax:**  
Key Considerations:
1. Normalization Requirement: Raw counts should almost always be normalized per capita or area. (e.g. Plotting raw COVID cases makes large population states appear artificially worse; plotting cases per 100,000 residents enables true comparison).
2. Color Scale: Sequential colormaps for continuous scales (0 to max); Diverging colormaps for metrics centered around a baseline (e.g. GDP growth above/below 0%).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What visual flaw is inherent to Choropleth maps?' Answer: Geographic Area Bias. Large geographic regions (like Alaska or Canada) dominate the visual field even if their population is minuscule, creating disproportionate cognitive weight.

---

### Q70. What is a Word Cloud and how does it encode text frequency?

> 🎯 **Core Answer:**  
> A Word Cloud (or Tag Cloud) is a visual text summary where individual words from a corpus are displayed together in a cluster, with the font size and color prominence of each word scaled proportionally to its frequency of occurrence.

**🔍 Technical Deep-Dive & Syntax:**  
Limitations of Word Clouds in Rigorous Analytics:
1. Area Perception: Longer words naturally look larger than short words even if they have identical frequency counts.
2. Lack of Context: Multi-word phrases, sentiment polarity, and syntactic context are lost (e.g. 'not good' is split into 'not' and 'good').
3. Clutter: Hard to extract precise numerical ranking compared to a simple horizontal bar chart of top-N word frequencies.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What preprocessing MUST be done before creating a word cloud?' Answer: Stopword removal (stripping 'the', 'is', 'at'), punctuation removal, lowercasing, and lemmatization.

---

### Q71. What is CKAN and what role do open data platforms play in data science?

> 🎯 **Core Answer:**  
> CKAN (Comprehensive Knowledge Archive Network) is the world's leading open-source data management system for publishing, sharing, and searching open datasets. Open data platforms (CKAN, Data.gov, Kaggle, Hugging Face) provide machine-readable, licensed datasets that foster reproducible research, civic innovation, and benchmark modeling.

**🔍 Technical Deep-Dive & Syntax:**  
Features of CKAN:
• Rich metadata cataloging (DCAT-AP standards).
• Integrated DataStore SQL query API allowing programmatic querying of CSV files.
• Geospatial preview and automated visualization widgets.
• Used by national open data portals worldwide (Data.gov in the US, Open Government Canada, European Data Portal).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is the primary license requirement for open data?' Answer: Permissive licensing (such as Creative Commons CC-BY or Open Data Commons ODC-BY) allowing commercial reuse and analytical redistribution.

---

## SECTION 6: UNIT 5 VIVA QUESTIONS – DATA VISUALIZATION WITH PANDAS & MATPLOTLIB

### Q72. Explain the 3-layer architecture of Matplotlib (Backend, Artist, Scripting Layer). What is the responsibility of each layer?

> 🎯 **Core Answer:**  
> 1. Backend Layer: Handles low-level rendering to output devices (raster PNG via `Agg`, vector PDF/SVG, or interactive GUI windows like `TkAgg`).
2. Artist Layer: The core structural layer; every visual component on canvas (Figure, Axes, Axis, Line2D, Text, Patch) is an Artist.
3. Scripting Layer (`pyplot`): High-level procedural wrapper providing MATLAB-like plotting functions (`plt.plot`).

**🔍 Technical Deep-Dive & Syntax:**  
• Backend Layer: Contains `Renderer` (draws primitives) and `GraphicsContext` (controls line thickness, color). Developers rarely interact with it directly unless writing new GUI backends or exporting headless images on web servers.
• Artist Layer: Two types of Artists:
  - Primitives: Specific geometric shapes (Line2D, Rectangle, Circle, Polygon, Text).
  - Containers: Collections that hold primitives (Figure, Axes, Axis, Tick).
• Scripting Layer: `matplotlib.pyplot` automates figure and axes creation, tracking the 'current' active figure/axes globally.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'In which layer does the Figure object reside?' Answer: In the Artist Layer (specifically, it is a Container Artist).

---

### Q73. Compare the Object-Oriented (OO) interface (`fig, ax = plt.subplots()`) with the state-based `pyplot` interface. Why is the OO interface strongly preferred for dashboards?

> 🎯 **Core Answer:**  
> The state-based `pyplot` interface relies on a hidden global state machine where commands implicitly affect whatever figure or subplot was last touched, causing severe bugs in multi-plot dashboards. The Object-Oriented interface explicitly instantiates Figure (`fig`) and Axes (`ax`) objects, providing complete, predictable control over multiple subplots independently.

**🔍 Technical Deep-Dive & Syntax:**  
OO Interface Syntax:
```python
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].plot(x, y1, label='Trend A')
axes[0, 1].bar(cats, vals)
axes[1, 0].hist(data, bins=20)
axes[1, 1].scatter(x, y2)
fig.tight_layout()
```
Benefits of OO:
1. Explicit Scope: You pass `ax` into plotting functions or methods, eliminating ambiguity.
2. Modular Functions: Custom visualization functions can accept an `ax` argument: `plot_financial_kpi(df, ax=axes[0, 1])`.
3. Eliminates accidental overwriting of plots in complex loops.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can you mix pyplot and OO methods?' Answer: Yes, but it is bad practice because switching between `plt.title()` and `ax.set_title()` leads to confusion regarding which axes object is currently active.

---

### Q74. Explain the hierarchy: Figure vs Axes vs Axis in Matplotlib.

> 🎯 **Core Answer:**  
> • Figure: The top-level canvas window/container that holds everything.
• Axes: An individual plotting area (subplot) residing inside the Figure, containing its own coordinate system, titles, and data graphics.
• Axis: The individual 1D number lines (`ax.xaxis` and `ax.yaxis`) that govern ticks, tick marks, labels, and coordinate limits.

**🔍 Technical Deep-Dive & Syntax:**  
Hierarchy Representation:
```
Figure (Canvas Container)
  └── Axes 1 (Subplot area with coordinate space)
        ├── XAxis (Ticks, Tick Labels, Axis Label)
        ├── YAxis (Ticks, Tick Labels, Axis Label)
        ├── Spines (Bounding box border lines)
        └── Artists (Line2D, Patches, Text, Legend)
  └── Axes 2 (Another subplot inside the same Figure)
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Is Axes the plural form of Axis in Matplotlib?' Answer: In plain English yes, but in Matplotlib NO! An `Axes` object is a complete 2D/3D subplot. An `Axis` object is just one number line (`xaxis` or `yaxis`). A single `Axes` has multiple `Axis` objects.

---

### Q75. What are Spines in Matplotlib, and how do you remove the top and right spines to achieve a clean modern look?

> 🎯 **Core Answer:**  
> Spines are the four boundary lines that enclose the plotting area (`'top'`, `'bottom'`, `'left'`, `'right'`). To remove the top and right spines, set their visibility to `False`: `ax.spines['top'].set_visible(False)` and `ax.spines['right'].set_visible(False)`.

**🔍 Technical Deep-Dive & Syntax:**  
```python
fig, ax = plt.subplots()
ax.plot(x, y)
# Remove cluttering box spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```
Why do this? In data visualization (Edward Tufte's principles), removing unnecessary non-data ink (chartjunk) maximizes the data-ink ratio and makes the visualization look clean and executive-ready.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can Seaborn do this automatically?' Answer: Yes, calling `sns.despine()` performs the exact same spine removal.

---

### Q76. What is the purpose of `plt.tight_layout()`? What specific problem does it solve?

> 🎯 **Core Answer:**  
> `plt.tight_layout()` automatically computes optimal padding between subplots and figure edges, preventing axis labels, tick marks, and subplot titles from overlapping or getting clipped along canvas boundaries.

**🔍 Technical Deep-Dive & Syntax:**  
In multi-panel subplots (e.g. `2x2`), the X-axis label of the top subplot frequently collides with the title of the bottom subplot. `plt.tight_layout()` dynamically resizes subplots to ensure all labels have sufficient clearance.
In modern Matplotlib, you can also pass `layout='constrained'` directly to `plt.subplots()`: `fig, axes = plt.subplots(2, 2, layout='constrained')`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Where should plt.tight_layout() be placed in your script?' Answer: Right before `plt.savefig()` or `plt.show()`, after all plotting, titles, and labels have been added to the axes.

---

### Q77. What does `bbox_inches='tight'` do in `plt.savefig()`?

> 🎯 **Core Answer:**  
> `bbox_inches='tight'` instructs Matplotlib to calculate the tight bounding box encompassing all visible Artist elements (including legends, titles, and annotations positioned outside the main axes area) so that nothing is cropped or truncated in the exported image file.

**🔍 Technical Deep-Dive & Syntax:**  
Syntax:
```python
plt.savefig('dashboard.png', dpi=300, bbox_inches='tight')
```
Common Scenario: An external legend placed at `bbox_to_anchor=(1.05, 1)` sits outside standard figure margins. Without `bbox_inches='tight'`, the exported PNG cuts the legend in half.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What does dpi=300 mean?' Answer: Dots Per Inch; 300 DPI produces crisp, high-resolution publication-quality graphics (standard screen resolution is 72-100 DPI).

---

### Q78. What does the `alpha` parameter control in Matplotlib and Pandas plotting?

> 🎯 **Core Answer:**  
> `alpha` controls the blending transparency (opacity) of graphical elements on a scale from `0.0` (completely transparent / invisible) to `1.0` (completely solid / opaque).

**🔍 Technical Deep-Dive & Syntax:**  
Critical Use in Scatter Plots: When plotting 100,000 data points, solid dots overlap into an opaque black blob (overplotting). Setting `alpha=0.2` or `alpha=0.05` allows overlapping points to accumulate into darker shades, visually revealing true underlying point density.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What happens if alpha=0.0?' Answer: The data elements are plotted but rendered completely invisible on the canvas.

---

### Q79. What plot types are supported directly by `df.plot(kind=...)` in Pandas?

> 🎯 **Core Answer:**  
> Supported values for `kind` include: `'line'` (default), `'bar'` (vertical bars), `'barh'` (horizontal bars), `'hist'` (histogram), `'box'` (box plot), `'kde'` / `'density'` (kernel density), `'area'` (area plot), `'pie'` (pie chart), `'scatter'` (scatter plot), and `'hexbin'` (hexagonal binning).

**🔍 Technical Deep-Dive & Syntax:**  
```python
# Shorthand method syntax:
df.plot.line()
df.plot.bar()
df.plot.barh()
df.plot.hist(bins=20)
df.plot.box()
df.plot.kde()
df.plot.scatter(x='age', y='salary')
df.plot.hexbin(x='age', y='salary', gridsize=20)
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Which two plot types REQUIRE explicit x and y column arguments in df.plot()?' Answer: `scatter` and `hexbin`. If you omit `x` or `y`, Pandas raises a `ValueError`.

---

### Q80. Why is `df.plot.hexbin()` superior to `df.plot.scatter()` for large datasets with high point overlap?

> 🎯 **Core Answer:**  
> `df.plot.scatter()` suffers from severe overplotting with large datasets ($N > 50,000$), where overlapping dots merge into a solid blob that hides true density variations. `df.plot.hexbin()` tiles the 2D coordinate plane into regular hexagonal bins and color-codes each hexagon by the count of points falling inside it, cleanly revealing density distributions.

**🔍 Technical Deep-Dive & Syntax:**  
Syntax:
```python
df.plot.hexbin(x='feature_x', y='feature_y', gridsize=25, cmap='Blues')
```
• `gridsize`: Controls the resolution of hexagons along the X-axis (higher = smaller hexagons).
• Colormap indicates count intensity, functioning as a continuous 2D histogram.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Why use hexagons instead of squares for 2D binning?' Answer: Hexagons are closer to circles than squares, meaning points in a hexagon are more equidistant from the center, producing less directional bias in visual density estimation.

---

### Q81. What is `pandas.plotting.scatter_matrix()`? What is plotted along the main diagonal and why?

> 🎯 **Core Answer:**  
> `scatter_matrix()` generates an $N \times N$ grid of pairwise bivariate scatter plots for all numerical variables in a DataFrame. The main diagonal displays univariate distributions (Histograms or KDE density curves) because plotting a variable against itself would yield an uninformative straight line $y = x$.

**🔍 Technical Deep-Dive & Syntax:**  
```python
from pandas.plotting import scatter_matrix
scatter_matrix(df[['age', 'salary', 'experience']], alpha=0.5, figsize=(8, 8), diagonal='kde')
```
• `diagonal='hist'`: Renders histograms on the diagonal.
• `diagonal='kde'`: Renders smooth Kernel Density Estimation curves on the diagonal.
It allows instant inspection of both bivariate relationships (off-diagonal) and univariate distributions (diagonal) simultaneously.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is the equivalent function in Seaborn?' Answer: `sns.pairplot(df)`.

---

### Q82. What is a Lag Plot (`lag_plot`)? How do you interpret: (1) a random circular cloud, (2) a tight diagonal line?

> 🎯 **Core Answer:**  
> A Lag Plot (`pandas.plotting.lag_plot(series, lag=1)`) plots the value of a time series at time $t$ on the X-axis against its value at time $t+1$ on the Y-axis: $(y_t, y_{t+1})$. A structureless circular cloud indicates the data is completely random white noise (uncorrelated). A tight linear diagonal indicates strong positive autocorrelation (persistence).

**🔍 Technical Deep-Dive & Syntax:**  
Interpretation Matrix for Viva:
1. Shapeless / Spherical / Circular Cloud: Data is independent and identically distributed (i.i.d.) random noise. Time-series forecasting will fail.
2. Tight Diagonal Band ($y = x$): High positive autocorrelation. If value is high today, it will be high tomorrow. Autoregressive AR(1) modeling is highly suitable.
3. Negative Diagonal Band ($y = -x$): High negative autocorrelation (oscillating alternating series).
4. Sinusoidal / Elliptical Ring: Cyclic or harmonic periodic process.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What does lag=7 mean in a lag plot of daily data?' Answer: It plots $(y_t, y_{t+7})$, checking whether observations today depend strongly on observations from the same day last week (weekly seasonality).

---

### Q83. What is an Autocorrelation Plot (`autocorrelation_plot`)? What do the horizontal dashed lines represent?

> 🎯 **Core Answer:**  
> An Autocorrelation Plot (`pandas.plotting.autocorrelation_plot(series)`) plots the autocorrelation coefficient across increasing time lag steps. The horizontal dashed lines represent the 95% and 99% statistical confidence bands. Peaks crossing outside the dashed lines indicate statistically significant autocorrelation or seasonality ($p < 0.05$).

**🔍 Technical Deep-Dive & Syntax:**  
• X-axis: Time lag $k$ ($1, 2, 3, \dots$).
• Y-axis: Autocorrelation coefficient $\rho_k \in [-1.0, +1.0]$.
• Dashed Lines: Critical value bounds $\pm \frac{1.96}{\sqrt{N}}$ (95% CI) and $\pm \frac{2.58}{\sqrt{N}}$ (99% CI).
• Stationary Noise: The curve stays permanently within the confidence bands near zero.
• Trend: Autocorrelation starts very high near +1.0 and decays very slowly towards zero.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'If autocorrelation at lag 0 is plotted, what is its value?' Answer: At lag 0, a series is compared with itself, so autocorrelation at lag 0 is ALWAYS exactly 1.0.

---

### Q84. How do you detect seasonality (e.g. weekly 7-day cycles) using an Autocorrelation plot?

> 🎯 **Core Answer:**  
> Seasonality appears as recurring, periodic spikes or crests that breach the horizontal dashed confidence intervals at regular lag intervals. For daily retail data, prominent spikes at lag 7, 14, 21, and 28 demonstrate statistically significant 7-day weekly seasonality.

**🔍 Technical Deep-Dive & Syntax:**  
In monthly data, a recurring peak at lag 12, 24, 36 indicates annual seasonality. If the spikes remain outside the 95% confidence bands, seasonal differencing ($y_t - y_{t-7}$) is required to stationarize the time series before fitting ARIMA models.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is a stationary time series?' Answer: A time series whose mean, variance, and autocorrelation structure remain constant over time.

---

### Q85. What is a Bootstrap Plot (`bootstrap_plot`)? What are the 3 summary statistics it evaluates?

> 🎯 **Core Answer:**  
> `pandas.plotting.bootstrap_plot()` evaluates the uncertainty, sampling variability, and confidence intervals of statistical estimators by repeatedly resampling the dataset with replacement. It generates sampling distribution plots for three statistics: (1) Mean, (2) Median, and (3) Midrange ($\frac{\min + \max}{2}$).

**🔍 Technical Deep-Dive & Syntax:**  
```python
from pandas.plotting import bootstrap_plot
bootstrap_plot(df['revenue'], size=50, samples=500, color='teal')
```
• `size`: Number of observations in each resample (default 50).
• `samples`: Number of bootstrap resampling repetitions (default 500).
Output: Displays 4 subplots showing the sampling histograms of the Mean, Median, Midrange, and a joint variability scatter plot. A narrow, tightly peaked histogram demonstrates high confidence and stability in the estimated statistic.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is the Midrange?' Answer: $\text{Midrange} = \frac{\text{Maximum} + \text{Minimum}}{2}$. It is an extreme-value estimator of central tendency that is highly sensitive to outliers.

---

### Q86. What is the role of `ax.annotate()` in data visualization and storytelling?

> 🎯 **Core Answer:**  
> `ax.annotate()` is used to direct viewer attention to critical data points (such as peak sales, anomalous dips, structural breaks, or policy changes) by drawing a text callout connected to the target coordinate via a customizable arrow.

**🔍 Technical Deep-Dive & Syntax:**  
Syntax:
```python
ax.annotate(
    text='Peak Sales: $1,850k',
    xy=(5, 1850),          # Arrow tip coordinates (data point)
    xytext=(3.5, 2100),     # Text label position
    arrowprops=dict(facecolor='red', shrink=0.05, width=1.5),
    fontsize=10, fontweight='bold'
)
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is the difference between ax.text() and ax.annotate()?' Answer: `ax.text()` places plain text at a coordinate without an arrow. `ax.annotate()` provides coordinate mapping and connecting arrow pointers.

---

### Q87. What is the default colormap in modern Matplotlib, and why is `'viridis'` preferred over legacy `'jet'`?

> 🎯 **Core Answer:**  
> The default colormap is `'viridis'`. It is perceptually uniform, meaning equal steps in data values correspond to equal perceived steps in color luminance across human vision, and it converts cleanly to grayscale without creating false visual gradient artifacts. Legacy `'jet'` (rainbow) creates artificial bands and is illegible to colorblind viewers.

**🔍 Technical Deep-Dive & Syntax:**  
Flaws of `'jet'`:
1. Non-monotonic luminance: It peaks in yellow, making middle values appear artificially brighter and more prominent than extreme values.
2. Incompatible with color vision deficiency: Red-green colorblind individuals cannot distinguish high from low values.
`'viridis'`, `'plasma'`, `'inferno'`, and `'magma'` were mathematically designed to resolve these flaws.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What is a diverging colormap?' Answer: A colormap (like `'coolwarm'` or `'RdBu'`) that has two contrasting colors at the extremes with a neutral color (white or gray) at the center, ideal for data with a meaningful midpoint (e.g. profit/loss or correlation coefficients from -1 to +1).

---

## SECTION 7: SCENARIO-BASED INDUSTRY PROBLEMS & SCHEMA ANALYSIS

### Q88. [Banking System Scenario] Why must Customer, Account, and Transaction be modeled as three separate tables? Why not store transaction history inside the Account table?

> 🎯 **Core Answer:**  
> 1. Cardinality (1:N): One account accumulates thousands of transactions over time. Storing transactions in Account would cause massive row duplication of account metadata (type, interest rate, customer link).
2. Immutability & Auditing: Transactions are append-only historical ledgers that must remain immutable for regulatory audits, whereas Account represents mutable current state.
3. Performance: Keeping Account lean allows instant balance lookups without scanning millions of transaction log records.

**🔍 Technical Deep-Dive & Syntax:**  
Schema Design:
• `Customer(customer_id, name, phone, kyc_status)`
• `Account(account_no, customer_id, account_type, current_balance)`
• `Transaction(trans_id, account_no, trans_type, amount, timestamp, running_balance)`
Foreign Keys:
`Account.customer_id` ➔ `Customer.customer_id`
`Transaction.account_no` ➔ `Account.account_no`

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'If current_balance is stored in Account, isn't that redundant with SUM(Transaction.amount)?' Answer: In banking, current_balance in Account is an indexed snapshot for sub-millisecond ATM queries. Transactions serve as the source-of-truth audit ledger used for daily reconciliation.

---

### Q89. [Banking Joint Account Scenario] How do you redesign a banking schema to support Joint Accounts where multiple customers co-own a single account?

> 🎯 **Core Answer:**  
> Joint accounts convert the relationship between Customer and Account from One-to-Many (1:N) into Many-to-Many (M:N). Remove `customer_id` from the Account table and introduce a junction table: `CustomerAccount(customer_id, account_no, ownership_role)`.

**🔍 Technical Deep-Dive & Syntax:**  
Redesigned Schema:
• `Customer(customer_id, name, pan_number)`
• `Account(account_no, account_type, balance, opened_date)`
• `CustomerAccount(customer_id, account_no, ownership_role)`
Composite Primary Key: `(customer_id, account_no)`.
`ownership_role` can store `'Primary'`, `'Secondary'`, or `'Authorized Signatory'`.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Can an account have 3 joint owners in this schema?' Answer: Yes! The junction table supports an arbitrary number of owners for any account.

---

### Q90. [Employee & Department Scenario] Why must Department be stored in a separate table from Employee? What 4 database anomalies occur if they are combined into a single table?

> 🎯 **Core Answer:**  
> Separating Department achieves Third Normal Form (3NF) by removing transitive functional dependencies (`emp_id` ➔ `dept_id` ➔ `dept_name`). Combining them introduces four severe anomalies: (1) Data Redundancy, (2) Update Anomaly, (3) Insertion Anomaly, and (4) Deletion Anomaly.

**🔍 Technical Deep-Dive & Syntax:**  
The 4 Anomalies:
1. Data Redundancy: Department name and budget are duplicated for all 500 employees in that department, wasting disk storage.
2. Update Anomaly: Renaming 'Human Resources' to 'People Operations' requires updating 500 rows. If any row is missed due to network timeout, the database becomes inconsistent.
3. Insertion Anomaly: You cannot store details of a newly created department until at least one employee is hired into it (because `emp_id` primary key cannot be NULL).
4. Deletion Anomaly: If the sole employee in a specialized department resigns and their row is deleted, all records of that department's existence are permanently lost from the database!

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What Normal Form specifically addresses transitive dependencies?' Answer: Third Normal Form (3NF).

---

### Q91. [Hotel Reservation Scenario] How do you design a database schema to prevent double-booking of rooms over overlapping date ranges?

> 🎯 **Core Answer:**  
> Separate static physical asset inventory (`Room`) from temporal events (`Reservation`). Double-booking is prevented using PostgreSQL Exclusion Constraints on date ranges (`EXCLUDE USING gist (room_id WITH =, daterange(check_in, check_out) WITH &&)`) or via a database `BEFORE INSERT` trigger checking for date collisions.

**🔍 Technical Deep-Dive & Syntax:**  
Schema Tables:
• `Room(room_id, room_type, price_per_night)`
• `Reservation(res_id, customer_id, room_id, check_in, check_out)`
Conflict Logic Condition:
Two date ranges $[A_{in}, A_{out}]$ and $[B_{in}, B_{out}]$ collide if:
`check_in < existing.check_out AND check_out > existing.check_in`
Trigger Implementation (SQLite):
```sql
CREATE TRIGGER prevent_overlap BEFORE INSERT ON Reservation
BEGIN
    SELECT RAISE(ABORT, 'Room already booked for this date range!')
    WHERE EXISTS (
        SELECT 1 FROM Reservation
        WHERE room_id = NEW.room_id
          AND (NEW.check_in < check_out AND NEW.check_out > check_in)
    );
END;
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Why not simply check if check_in = existing.check_in?' Answer: Because a customer might check in on Day 2 of an existing 5-day booking. You must check date range overlap, not exact equality!

---

### Q92. [Food Delivery Logistics Scenario] Why separate Order from Delivery? How do you support multi-leg delivery transfers (pickup hub -> middle mile -> last mile)?

> 🎯 **Core Answer:**  
> 1. Separation of Concerns: Order tracks customer items, billing, and restaurant fulfillment; Delivery tracks dispatch, transport logistics, and driver tracking.
2. Independent Lifecycles: An order exists before a delivery agent is assigned.
3. Multi-Leg Deliveries: Turn Delivery into a 1:N or M:N tracking table: `Delivery(delivery_id, order_id, agent_id, leg_type, status, start_time, end_time)`.

**🔍 Technical Deep-Dive & Syntax:**  
Multi-Leg Tracking:
`leg_type` distinguishes: `'First Mile Pickup'` (Restaurant to Local Hub), `'Middle Mile Transit'` (Hub to City Hub), `'Last Mile Delivery'` (City Hub to Customer Door).
If an agent gets a flat tire or cancels, a new delivery record is logged without altering the customer's financial order.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What happens if you store agent_id directly in the Orders table?' Answer: You can only assign exactly one agent per order; reassignments overwrite history, and multi-agent hub transfers become impossible.

---

### Q93. [University System Scenario] Explain how the `Enrollment` table resolves the Many-to-Many relationship between Student and Course. How do you track assignment submissions and grades?

> 🎯 **Core Answer:**  
> `Enrollment` acts as an associative bridge table with composite primary key `(student_id, course_id)`. To track assignment submissions, create a `StudentSubmission` table linking `student_id` to `assignment_id`, storing `marks_obtained`, `submission_date`, and `feedback`.

**🔍 Technical Deep-Dive & Syntax:**  
Schema Design:
• `Student(student_id, name, department)`
• `Course(course_id, course_name, credits)`
• `Enrollment(student_id, course_id, semester, final_grade)`
• `Assignment(assignment_id, course_id, max_marks, due_date)`
• `StudentSubmission(submission_id, assignment_id, student_id, marks_obtained, submission_timestamp)`
Constraint: `UNIQUE(assignment_id, student_id)` guarantees each student submits exactly once per assignment.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Why isn't marks_obtained stored inside the Assignment table?' Answer: An assignment has 60 students; storing marks in Assignment would require repeating the assignment 60 times, violating 1NF/2NF.

---

### Q94. [Bus Transportation Scenario] How do you design a bus booking schema that allows one customer to book multiple seats for family members on a single payment transaction?

> 🎯 **Core Answer:**  
> Decouple the financial booking transaction from passenger seat allocation by creating two tables: `Booking` (transaction level) and `BookingPassenger` (seat allocation level).

**🔍 Technical Deep-Dive & Syntax:**  
Schema Design:
• `Bus(bus_id, route, total_seats)`
• `Booking(booking_id, bus_id, booked_by_cust_id, booking_date, total_fare, pnr_number)`
• `BookingPassenger(ticket_id, booking_id, passenger_name, age, gender, seat_number)`
Constraint: `UNIQUE(bus_id, travel_date, seat_number)` ensures no seat is double-sold.

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What primary key ensures seat uniqueness?' Answer: A composite unique constraint on `(bus_id, travel_date, seat_number)`.

---

### Q95. [E-Commerce Data Quality Scenario] How do you classify and clean issues such as missing tax, negative price, corrupt phone numbers, and inconsistent state names?

> 🎯 **Core Answer:**  
> 1. Negative Price: Flagged as Validity / Range violation; clean by taking absolute value or dropping corrupt records.
2. Missing Tax: Completeness issue; impute by calculating `price * state_tax_rate`.
3. Corrupt Phone Numbers: Syntax issue; clean with regex `re.sub(r'\D', '', phone)[-10:]`.
4. Inconsistent State Names: Consistency issue ('TN', 'Tamilnadu', 'Tamil Nadu'); standardize using dictionary mapping or fuzzy token matching.

**🔍 Technical Deep-Dive & Syntax:**  
Standardization Script:
```python
# Clean states using mapping dictionary:
state_map = {'TN': 'Tamil Nadu', 'Tamilnadu': 'Tamil Nadu', 'KA': 'Karnataka'}
df['state'] = df['state'].str.strip().replace(state_map)

# Enforce positive price:
df['price'] = df['price'].abs()

# Recalculate tax if null:
df['tax'] = df['tax'].fillna(df['price'] * 0.18)
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'What business risk occurs if negative prices are not cleaned?' Answer: Aggregations like `df['price'].sum()` compute artificially low revenue, misleading financial audits and earnings reports.

---

### Q96. [Healthcare Diagnosis Cleaning Scenario] How do you standardize varying text diagnoses (e.g. 'type 2 diabetes', 'T2DM', 'Diabetes Mellitus-II') into standard ICD-10 medical codes?

> 🎯 **Core Answer:**  
> Use a two-tier approach: (1) Exact synonym dictionary mapping for known clinical acronyms, and (2) Fuzzy string matching (`fuzzywuzzy.process.extractOne` with `token_set_ratio`) against the official ICD-10 medical terminology lexicon with a confidence threshold $\ge 85$.

**🔍 Technical Deep-Dive & Syntax:**  
```python
from fuzzywuzzy import process, fuzz
icd10_lexicon = {
    'Type 2 Diabetes Mellitus': 'E11',
    'Essential Hypertension': 'I10',
    'Acute Bronchitis': 'J20'
}

def map_diagnosis(diag_str):
    match, score = process.extractOne(diag_str, icd10_lexicon.keys(), scorer=fuzz.token_set_ratio)
    if score >= 85:
        return icd10_lexicon[match]
    return 'UNMAPPED_REVIEW'
```

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Why not use simple regex matching?' Answer: Clinical text contains arbitrary misspellings, permutations ('Diabetes Type 2' vs 'Type 2 Diabetes'), and abbreviations that require token set fuzzy matching.

---

### Q97. [Titanic Survival Analysis Lab Scenario] In the Titanic dataset, how was missing Age imputed, and why was Gender the strongest survival predictor?

> 🎯 **Core Answer:**  
> Missing Age was imputed using median age grouped by Passenger Class and Title (Mr., Mrs., Master, Miss). Gender was the strongest predictor because maritime 'women and children first' evacuation protocols resulted in ~74% female survival versus ~19% male survival.

**🔍 Technical Deep-Dive & Syntax:**  
Imputation Logic:
```python
# Extract title from passenger name:
df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
# Impute missing Age with median of title and passenger class:
df['Age'] = df.groupby(['Pclass', 'Title'])['Age'].transform(lambda x: x.fillna(x.median()))
```
Key Findings:
1. Survival Rate by Gender: Female: 74.2%, Male: 18.9%.
2. Survival by Class: 1st Class: 63%, 2nd Class: 47%, 3rd Class: 24% (socioeconomic priority).
3. Outliers in Fare: Fares reached $512 (extreme high outliers detected via IQR).

> ⚠️ **Examiner Trap & Follow-Up:**  
> Examiner Trap: 'Why not impute missing Age with overall mean?' Answer: A child with title 'Master' would receive an adult age of 29.7, completely destroying the 'children first' behavioral signal!

---

## SECTION 8: 30 RAPID-FIRE TRICK & TRAP QUESTIONS (EXAMINER FAVORITES)

| No. | Rapid-Fire Question | Exact Technical Answer |
| :---: | :--- | :--- |
| **Q98** | Does SQLite support native BOOLEAN data types? | **No! SQLite does not have a distinct Boolean storage class. Booleans are stored as integers 0 (false) and 1 (true).** |
| **Q99** | What is the return type of df.shape? | **A Python tuple of integers: (number_of_rows, number_of_columns).** |
| **Q100** | What happens if you open a file in 'w' mode when it already exists? | **It immediately truncates (erases/wipes) the entire file contents to zero bytes!** |
| **Q101** | What does df['col'].unique() return vs df['col'].nunique()? | **unique() returns a NumPy array of unique values; nunique() returns the integer count of distinct values.** |
| **Q102** | What is the difference between df.dropna() and df.drop()? | **dropna() removes rows/columns containing missing (NaN) values; drop() removes specific rows or columns by label name or position.** |
| **Q103** | Does json.loads() accept Python dictionaries? | **No! It takes a JSON-formatted STRING as input. Passing a dict raises TypeError.** |
| **Q104** | What does pd.to_numeric() do by default if errors is not specified? | **It defaults to errors='raise', throwing a ValueError if any invalid string is encountered.** |
| **Q105** | What is the output of bool(np.nan)? | **True! In Python, floating-point NaN evaluates to True, which is why you must use pd.isna() instead of if val:.** |
| **Q106** | What is the default value of axis in pd.concat()? | **axis=0 (stacks rows vertically).** |
| **Q107** | Can a table have multiple Foreign Keys? | **Yes! A table can have multiple Foreign Key columns referencing different parent tables.** |
| **Q108** | Can a PRIMARY KEY column contain NULL values? | **Never! By definition and ANSI SQL standard, a PRIMARY KEY is strictly UNIQUE and NOT NULL.** |
| **Q109** | Can a UNIQUE column contain NULL values? | **Yes! In most SQL databases (PostgreSQL, MySQL, SQLite), a UNIQUE column allows NULL values because NULL is considered unknown and not equal to another NULL.** |
| **Q110** | What is the default colormap in Matplotlib 2.0+? | **'viridis' (perceptually uniform).** |
| **Q111** | What does plt.show() do behind the scenes? | **It triggers the GUI/backend event loop to render and display the active figure windows.** |
| **Q112** | What is the difference between df.plot(kind='bar') and df.plot(kind='barh')? | **bar creates vertical columns; barh creates horizontal bars.** |
| **Q113** | In pd.merge, what does how='cross' do? | **It computes the Cartesian Product of all rows (N x M rows).** |
| **Q114** | What does df.info() print? | **DataFrame memory usage, row count, column names, non-null counts, and data types.** |
| **Q115** | How do you access the second row and third column using integer indexing in Pandas? | **df.iloc[1, 2] (zero-based).** |
| **Q116** | What is the mathematical range of Spearman's rank correlation? | **Exactly [-1.0, +1.0], identical to Pearson.** |
| **Q117** | What is an i.i.d. dataset? | **Independent and Identically Distributed.** |
| **Q118** | What does re.match('^cat', 'dog and cat') return? | **None! Because 'cat' is not at the start of the string.** |
| **Q119** | What does re.search('cat', 'dog and cat') return? | **A Match object matching 'cat' at index 8.** |
| **Q120** | What does df.reset_index(drop=True) do? | **Resets index to 0, 1, 2... and discards the previous index instead of inserting it as a new column.** |
| **Q121** | What does df.describe(include='all') add for categorical columns? | **'unique', 'top' (mode), and 'freq' (frequency of mode).** |
| **Q122** | What does the diagonal argument in scatter_matrix accept? | **'hist' (histogram) or 'kde' (Kernel Density Estimation).** |
| **Q123** | What is the Tukey IQR lower fence formula? | **Q1 - 1.5 * IQR.** |
| **Q124** | What is the Tukey IQR upper fence formula? | **Q3 + 1.5 * IQR.** |
| **Q125** | In a lag plot, what does a tight diagonal line indicate? | **Strong positive autocorrelation.** |
| **Q126** | In an autocorrelation plot, what do the horizontal dashed lines indicate? | **95% and 99% statistical confidence bounds.** |
| **Q127** | Why should you never commit inside a loop for 10,000 inserts? | **Calling commit() flushes transaction logs to disk on every single row, destroying disk I/O performance. Wrap all 10,000 in one transaction and commit once at the end!** |

---
