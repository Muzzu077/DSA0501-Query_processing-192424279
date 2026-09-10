# UNIT 2: INTRODUCTION TO PYTHON SQL LIBRARIES (CO2)
**Course:** DSA05 / DSA0501 – Query Processing for Data Science  
**Target:** 180-Question MCQ Exam Preparation & Comprehensive Concept Mastery  
**Assessment Framework:** Bloom's Revised Taxonomy (Levels L1 to L6)

---

## 📌 TABLE OF CONTENTS
1. [Core Concepts & Database Architecture](#1-core-concepts--database-architecture)
   - 1.1 Relational Databases & Python SQL Ecosystem
   - 1.2 Comparison: SQLite vs MySQL vs PostgreSQL
2. [Database Connectivity in Python](#2-database-connectivity-in-python)
   - 2.1 Connecting to SQLite (`sqlite3`)
   - 2.2 Connecting to MySQL (`mysql.connector` / `pymysql`)
   - 2.3 Connecting to PostgreSQL (`psycopg2`)
   - 2.4 Connection vs Cursor Objects
3. [CRUD Operations & DDL/DML Commands](#3-crud-operations--ddldml-commands)
   - 3.1 Creating Tables (`CREATE TABLE`, Data Types, Constraints)
   - 3.2 Inserting Records (`INSERT INTO`, `execute`, `executemany`, Placeholders)
   - 3.3 Selecting Records (`SELECT`, `fetchone`, `fetchall`, `fetchmany`, `row_factory`)
   - 3.4 Updating Records (`UPDATE ... SET ... WHERE`)
   - 3.5 Deleting Records (`DELETE` vs `TRUNCATE` vs `DROP`)
4. [Advanced SQL Operations with Python](#4-advanced-sql-operations-with-python)
   - 4.1 SQL Joins (INNER, LEFT, RIGHT, FULL OUTER)
   - 4.2 Aggregations & Grouping (`COUNT`, `SUM`, `AVG`, `GROUP BY`, `HAVING`)
   - 4.3 Transaction Management (Commit, Rollback, ACID Properties)
   - 4.4 Pandas & SQL Integration (`pd.read_sql_query`, `df.to_sql`)
5. [High-Yield Exam Tips & Common MCQ Traps](#5-high-yield-exam-tips--common-mcq-traps)
6. [Bloom's Taxonomy-Aligned MCQ Question Bank (40+ Questions)](#6-blooms-taxonomy-aligned-mcq-question-bank)
   - [6.1 Level 1: Remember (Knowledge & Recall)](#61-level-1-remember-knowledge--recall)
   - [6.2 Level 2: Understand (Comprehension & Explanation)](#62-level-2-understand-comprehension--explanation)
   - [6.3 Level 3: Apply (Application, Computation & Code Output)](#63-level-3-apply-application-computation--code-output)
   - [6.4 Level 4: Analyze (Analysis, Logic & Bug Detection)](#64-level-4-analyze-analysis-logic--bug-detection)
   - [6.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)](#65-level-5--6-evaluate--create-judgment-architecture--design)

---

## 1. CORE CONCEPTS & DATABASE ARCHITECTURE

### 1.1 Relational Databases & Python SQL Ecosystem
* **RDBMS (Relational Database Management System):** Stores data in structured 2D tables composed of rows (records/tuples) and columns (attributes/fields).
* **Python Database API Specification v2.0 (DB-API 2.0):** Standardized interface defining how Python interacts with databases across different database drivers (`connect()`, `cursor()`, `execute()`, `commit()`, `rollback()`, `close()`).

### 1.2 Comparison: SQLite vs MySQL vs PostgreSQL
| Feature | SQLite (`sqlite3`) | MySQL (`mysql.connector`) | PostgreSQL (`psycopg2`) |
| :--- | :--- | :--- | :--- |
| **Architecture** | **Serverless**, file-based or in-memory | **Client-Server** (Network daemon) | **Client-Server** (Object-Relational) |
| **Installation** | Built into Python standard library | Requires MySQL server & driver | Requires Postgres server & driver |
| **Default Port** | N/A (Local Disk File) | `3306` | `5432` |
| **Concurrency** | Single writer (file locks) | Multi-threaded, high concurrent writes | Multi-process MVCC, enterprise grade |
| **Auto Increment** | `INTEGER PRIMARY KEY AUTOINCREMENT` | `INT AUTO_INCREMENT PRIMARY KEY` | `SERIAL PRIMARY KEY` |
| **Parameter Placeholder**| **`?`** (qmark) or `:name` | **`%s`** (format) | **`%s`** (format) |
| **RIGHT / FULL JOIN** | ❌ Not supported directly | ✅ RIGHT JOIN, ❌ FULL JOIN | ✅ Both RIGHT and FULL JOIN |

---

## 2. DATABASE CONNECTIVITY IN PYTHON

### 2.1 Connecting to SQLite (`import sqlite3`)
```python
import sqlite3

# Connect to a file-based database (creates 'university.db' if missing)
conn = sqlite3.connect('university.db')

# Connect to a temporary in-memory database (erased when connection closes)
mem_conn = sqlite3.connect(':memory:')

cursor = conn.cursor()
conn.close()
```

### 2.2 Connecting to MySQL (`import mysql.connector`)
```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="my_password",
    database="company_db",
    port=3306
)
cursor = conn.cursor(dictionary=True)
```

### 2.3 Connecting to PostgreSQL (`import psycopg2`)
```python
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    dbname="hospital_db",
    user="postgres",
    password="secure_password",
    host="localhost",
    port=5432
)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
```

---

## 3. CRUD OPERATIONS & DDL/DML COMMANDS

```
╔══════════════════════════════════════════════════════════════════════════╗
║                     CRUD ➔ SQL COMMAND MAPPING                           ║
╠════════════════╦═══════════════════╦═════════════════════════════════════╣
║ Operation      ║ SQL Statement     ║ Category                            ║
╠════════════════╬═══════════════════╬═════════════════════════════════════╣
║ **C** - Create ║ `INSERT INTO ...` ║ DML (Data Manipulation Language)    ║
║ **R** - Read   ║ `SELECT ...`      ║ DQL (Data Query Language)           ║
║ **U** - Update ║ `UPDATE ... SET`  ║ DML (Data Manipulation Language)    ║
║ **D** - Delete ║ `DELETE FROM ...` ║ DML (Data Manipulation Language)    ║
╚════════════════╩═══════════════════╩═════════════════════════════════════╝
```

### 3.1 Creating Tables (DDL)
```python
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    cgpa REAL CHECK(cgpa >= 0.0 AND cgpa <= 10.0),
    admission_date DATE DEFAULT CURRENT_DATE
);
''')
conn.commit()
```

### 3.2 Inserting Records (Create)
```python
# SQLite (uses '?' placeholder)
sql = "INSERT INTO students (name, department, cgpa) VALUES (?, ?, ?)"
cursor.execute(sql, ("Aarav Sharma", "Computer Science", 8.85))
conn.commit()

# Bulk Insert
student_records = [
    ("Ananya Patel", "Data Science", 9.15),
    ("Rohan Gupta", "Artificial Intelligence", 8.45)
]
cursor.executemany("INSERT INTO students (name, department, cgpa) VALUES (?, ?, ?)", student_records)
conn.commit()
```

### 3.3 Selecting Records (Read)
```python
cursor.execute("SELECT student_id, name, cgpa FROM students WHERE cgpa >= ?", (8.5,))

row = cursor.fetchone()   # Returns single tuple or None
all_rows = cursor.fetchall()  # Returns list of tuples
```

### 3.4 Updating Records (Update)
```python
update_sql = "UPDATE students SET cgpa = ? WHERE student_id = ?"
cursor.execute(update_sql, (9.05, 1))
conn.commit()
```

### 3.5 Deleting Records (Delete)
```python
delete_sql = "DELETE FROM students WHERE student_id = ?"
cursor.execute(delete_sql, (3,))
conn.commit()
```

---

## 4. ADVANCED SQL OPERATIONS WITH PYTHON

### 4.1 SQL Joins
* **INNER JOIN:** Returns matching records in both tables.
* **LEFT (OUTER) JOIN:** Retains all rows from Left table; unmatched Right fields are `NULL`.
* **RIGHT (OUTER) JOIN:** Retains all rows from Right table.
* **FULL (OUTER) JOIN:** Retains all rows from both tables.

### 4.2 Aggregations & Grouping
```sql
SELECT department, COUNT(*) AS total_students, AVG(cgpa) AS avg_cgpa
FROM students
WHERE cgpa >= 6.0
GROUP BY department
HAVING COUNT(*) >= 5
ORDER BY avg_cgpa DESC;
```

### 4.3 Transaction Management & ACID
```python
try:
    cursor.execute("UPDATE accounts SET balance = balance - 500 WHERE acc_no = 101")
    cursor.execute("UPDATE accounts SET balance = balance + 500 WHERE acc_no = 102")
    conn.commit()
except Exception as e:
    conn.rollback()
finally:
    cursor.close()
    conn.close()
```

### 4.4 Pandas & SQL Integration
```python
import pandas as pd
df = pd.read_sql_query("SELECT * FROM students WHERE cgpa >= 8.0", conn)
df.to_sql('top_students', conn, if_exists='append', index=False)
```

---

## 5. HIGH-YIELD EXAM TIPS & COMMON MCQ TRAPS

1. **Autocommit is OFF by default:** Always call `conn.commit()` after `INSERT`, `UPDATE`, `DELETE`.
2. **Placeholders:** SQLite = `?` ; MySQL/PostgreSQL = `%s`.
3. **`cursor.fetchall()` on empty results:** Returns `[]` (empty list), NOT `None`.
4. **`WHERE` vs `HAVING`:** `WHERE` cannot evaluate aggregate functions (`AVG()`, `COUNT()`); `HAVING` can.
5. **Deleting without WHERE:** `UPDATE` or `DELETE` without a `WHERE` clause modifies/deletes **ALL records** in the table!

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
**Which Python standard library module provides built-in support for an embedded relational database without requiring an external database server?**  
A) `psycopg2`  
B) `mysql.connector`  
C) `sqlite3`  
D) `pymongo`  
**Answer: C**  
*Explanation:* `sqlite3` is built into Python standard libraries, providing a serverless, zero-configuration disk/memory database engine.

---

#### Question 2 [Bloom's Level: L1 - Remember]
**What is the default TCP/IP network port for MySQL server connections?**  
A) 5432  
B) 1521  
C) 3306  
D) 8080  
**Answer: C**  
*Explanation:* MySQL listens on default port 3306. PostgreSQL listens on default port 5432.

---

#### Question 3 [Bloom's Level: L1 - Remember]
**What is the default TCP/IP port used by PostgreSQL server?**  
A) 3306  
B) 1433  
C) 5432  
D) 27017  
**Answer: C**  
*Explanation:* PostgreSQL's standard daemon port is 5432.

---

#### Question 4 [Bloom's Level: L1 - Remember]
**What parameter placeholder is used in SQLite parameterized queries in Python?**  
A) `%s`  
B) `?`  
C) `@param`  
D) `$`  
**Answer: B**  
*Explanation:* SQLite uses the question mark `?` (qmark style) for parameterized queries.

---

#### Question 5 [Bloom's Level: L1 - Remember]
**What parameter placeholder format is used by `mysql.connector` and `psycopg2`?**  
A) `?`  
B) `%s`  
C) `:val`  
D) `&1`  
**Answer: B**  
*Explanation:* Both `mysql.connector` and `psycopg2` use `%s` (format style) for parameter interpolation.

---

#### Question 6 [Bloom's Level: L1 - Remember]
**What does the "A" in ACID database properties stand for?**  
A) Availability  
B) Atomicity  
C) Accuracy  
D) Asynchronous  
**Answer: B**  
*Explanation:* ACID stands for Atomicity, Consistency, Isolation, and Durability.

---

#### Question 7 [Bloom's Level: L1 - Remember]
**Which cursor attribute gives the primary key ID generated by the most recent `INSERT` operation in SQLite?**  
A) `cursor.primary_id`  
B) `cursor.lastrowid`  
C) `cursor.insert_id`  
D) `cursor.latest_key`  
**Answer: B**  
*Explanation:* `cursor.lastrowid` provides the auto-generated rowid of the last inserted record.

---

#### Question 8 [Bloom's Level: L1 - Remember]
**Which PostgreSQL data type is used to define auto-incrementing integer primary keys?**  
A) `AUTO_INCREMENT`  
B) `SERIAL`  
C) `IDENTITY_INT`  
D) `SEQUENCE`  
**Answer: B**  
*Explanation:* PostgreSQL uses `SERIAL` (or `BIGSERIAL`) to define auto-incrementing integer primary key sequences.

---

### 6.2 Level 2: Understand (Comprehension & Explanation)

#### Question 9 [Bloom's Level: L2 - Understand]
**Why is calling `conn.commit()` mandatory after executing `INSERT`, `UPDATE`, or `DELETE` statements in Python DB-API?**  
A) To close the database connection  
B) Because autocommit is disabled by default, and `conn.commit()` is required to persist transactional changes to disk  
C) To encrypt the database file  
D) To convert SQL output into a DataFrame  
**Answer: B**  
*Explanation:* In standard DB-API drivers, DML statements run inside an active transaction. Failing to commit results in changes being discarded upon connection close.

---

#### Question 10 [Bloom's Level: L2 - Understand]
**Why must SQL statements use parameterized queries (e.g. `cursor.execute("... VALUES (?)", (val,))`) instead of Python string formatting?**  
A) To improve CPU caching speed  
B) To protect the application against SQL Injection attacks and handle data type escaping automatically  
C) Because Python f-strings cannot be used in database scripts  
D) To format tables in ASCII  
**Answer: B**  
*Explanation:* Parameterized queries treat parameters strictly as data values rather than executable code, neutralizing SQL injection vectors.

---

#### Question 11 [Bloom's Level: L2 - Understand]
**What is the operational difference between `DELETE FROM table;` and `DROP TABLE table;`?**  
A) `DELETE` removes table definition, while `DROP` only removes records  
B) `DELETE` removes rows while preserving the table schema/structure; `DROP` destroys both data and table structure entirely  
C) `DELETE` is a DDL command, while `DROP` is DML  
D) There is no difference  
**Answer: B**  
*Explanation:* `DELETE` is DML that purges records but keeps the empty table definition intact. `DROP` is DDL that permanently obliterates the table and its schema from the database.

---

#### Question 12 [Bloom's Level: L2 - Understand]
**What is the difference between `WHERE` and `HAVING` clauses in an SQL query?**  
A) `WHERE` is used with `SELECT`, `HAVING` with `UPDATE`  
B) `WHERE` filters individual rows before grouping; `HAVING` filters aggregated groups after the `GROUP BY` stage  
C) `WHERE` works only on text; `HAVING` works only on numbers  
D) There is no functional difference  
**Answer: B**  
*Explanation:* `WHERE` filters individual rows prior to aggregation and cannot evaluate aggregate functions (e.g. `SUM()`). `HAVING` filters groups post-aggregation.

---

#### Question 13 [Bloom's Level: L2 - Understand]
**What happens to an in-memory SQLite database (`sqlite3.connect(':memory:')`) when the connection `conn.close()` is executed?**  
A) The data is saved to a hidden file on disk  
B) The database and all its tables and records are permanently erased from RAM  
C) The data is uploaded to a remote server  
D) An exception is raised  
**Answer: B**  
*Explanation:* In-memory SQLite databases exist exclusively in process RAM. When the connection closes, the allocated memory is freed and all data is lost.

---

#### Question 14 [Bloom's Level: L2 - Understand]
**Which SQL JOIN returns all records from the left table and matched records from the right table, populating unmatched right fields with `NULL`?**  
A) `INNER JOIN`  
B) `LEFT OUTER JOIN`  
C) `CROSS JOIN`  
D) `FULL OUTER JOIN`  
**Answer: B**  
*Explanation:* A `LEFT OUTER JOIN` preserves every row from the left table, joining right table attributes where keys match, and supplying `NULL` where no match exists.

---

#### Question 15 [Bloom's Level: L2 - Understand]
**What is the consequence of executing `UPDATE employees SET salary = 75000;` without a `WHERE` clause?**  
A) A syntax error is raised  
B) Only the first row in the table is updated  
C) Every single employee's salary in the entire table is updated to 75000  
D) The query is ignored  
**Answer: C**  
*Explanation:* Without a `WHERE` filter condition, an `UPDATE` statement executes across all tuples in the table unconditionally.

---

#### Question 16 [Bloom's Level: L2 - Understand]
**What does `conn.rollback()` accomplish in Python database programming?**  
A) Restores a backup from yesterday  
B) Undoes/cancels all pending modifications made in the current uncommitted transaction  
C) Re-executes the last query  
D) Deletes the database  
**Answer: B**  
*Explanation:* `conn.rollback()` aborts the active transaction, reverting the database state to the point of the last successful `commit()`.

---

### 6.3 Level 3: Apply (Application, Computation & Code Output)

#### Question 17 [Bloom's Level: L3 - Apply]
**Consider the code snippet:**
```python
import sqlite3
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE t (val INT)")
cursor.executemany("INSERT INTO t VALUES (?)", [(10,), (20,), (30,), (40,)])
conn.commit()
cursor.execute("SELECT * FROM t WHERE val > 15")
rows = cursor.fetchall()
print(len(rows))
```
**What is the output?**  
A) 1  
B) 2  
C) 3  
D) 4  
**Answer: C**  
*Explanation:* Among `[10, 20, 30, 40]`, values `20`, `30`, and `40` satisfy `val > 15`. `cursor.fetchall()` returns a list of 3 tuples, so `len()` is 3.

---

#### Question 18 [Bloom's Level: L3 - Apply]
**What does `cursor.fetchone()` return when a query produces zero matching rows?**  
A) An empty tuple `()`  
B) `None`  
C) An empty list `[]`  
D) Raises `StopIteration`  
**Answer: B**  
*Explanation:* `cursor.fetchone()` returns the next row as a tuple, or `None` if the result set is exhausted or empty.

---

#### Question 19 [Bloom's Level: L3 - Apply]
**What does `cursor.fetchall()` return when a `SELECT` query finds no matching rows?**  
A) `None`  
B) An empty list `[]`  
C) An empty tuple `()`  
D) Raises `NoDataFoundError`  
**Answer: B**  
*Explanation:* `cursor.fetchall()` returns a `list`. When no records match, it returns an empty list `[]`.

---

#### Question 20 [Bloom's Level: L3 - Apply]
**How do you configure SQLite in Python to enable dictionary-like column name access on query rows (e.g. `row['name']`)?**  
A) `conn.dict_mode = True`  
B) `conn.row_factory = sqlite3.Row`  
C) `cursor.enable_dict()`  
D) `sqlite3.set_format('DICT')`  
**Answer: B**  
*Explanation:* Setting `conn.row_factory = sqlite3.Row` wraps result tuples in `Row` objects supporting key-based lookup.

---

#### Question 21 [Bloom's Level: L3 - Apply]
**Which Pandas function directly executes an SQL query against a database connection and returns the result as a DataFrame?**  
A) `pd.sql_to_df()`  
B) `pd.read_sql_query()`  
C) `pd.query_db()`  
D) `pd.load_sql()`  
**Answer: B**  
*Explanation:* `pd.read_sql_query(sql_query, conn)` runs the SQL query and automatically loads the results into a Pandas `DataFrame`.

---

#### Question 22 [Bloom's Level: L3 - Apply]
**When exporting a DataFrame using `df.to_sql('sales', conn, if_exists='append')`, what happens if the table `'sales'` already exists?**  
A) An exception is raised  
B) The existing table is dropped and replaced  
C) The DataFrame rows are inserted into the existing table without dropping it  
D) All existing rows are overwritten  
**Answer: C**  
*Explanation:* `if_exists='append'` inserts the DataFrame's records as new rows into the existing table.

---

#### Question 23 [Bloom's Level: L3 - Apply]
**What is the default value of the `if_exists` parameter in `df.to_sql()`?**  
A) `'fail'`  
B) `'replace'`  
C) `'append'`  
D) `'ignore'`  
**Answer: A**  
*Explanation:* The default is `if_exists='fail'`, which raises a `ValueError` if the table already exists in the database.

---

#### Question 24 [Bloom's Level: L3 - Apply]
**What is the output of `cursor.fetchmany(5)` if exactly 2 rows remain in the cursor result set?**  
A) Raises an `IndexError`  
B) Returns a list containing the 2 available rows  
C) Returns `None`  
D) Returns a list of 5 items padded with `None`  
**Answer: B**  
*Explanation:* `cursor.fetchmany(size)` returns up to `size` rows. If fewer are available, it returns all remaining rows without error.

---

#### Question 25 [Bloom's Level: L3 - Apply]
**What is printed by this code?**
```python
import sqlite3
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute("CREATE TABLE emp (id INT, salary REAL)")
cursor.execute("INSERT INTO emp VALUES (1, 50000)")
cursor.execute("UPDATE emp SET salary = salary + 5000 WHERE id = 1")
print(cursor.rowcount)
```
A) 0  
B) 1  
C) 2  
D) 5000  
**Answer: B**  
*Explanation:* `cursor.rowcount` returns the number of rows affected by the last SQL command. Exactly 1 row was updated.

---

#### Question 26 [Bloom's Level: L3 - Apply]
**Which SQL statement correctly creates a table with a check constraint on student age?**  
A) `CREATE TABLE student (id INT, age INT CHECK (age >= 18 AND age <= 100));`  
B) `CREATE TABLE student (id INT, age INT IF (age >= 18));`  
C) `CREATE TABLE student (id INT, age INT VALIDATE (18, 100));`  
D) `CREATE TABLE student (id INT, age INT CONSTRAINT >= 18);`  
**Answer: A**  
*Explanation:* Standard SQL syntax for a domain check constraint is `CHECK (condition)`.

---

### 6.4 Level 4: Analyze (Analysis, Logic & Bug Detection)

#### Question 27 [Bloom's Level: L4 - Analyze]
**Analyze the following SQL query for syntax errors:**
```sql
SELECT department, AVG(salary) 
FROM employees 
WHERE AVG(salary) > 50000 
GROUP BY department;
```
**Why will this query fail to execute?**  
A) `AVG` is not a valid SQL function  
B) Aggregate functions like `AVG(salary)` cannot be evaluated in a `WHERE` clause; filtering on aggregated metrics must be written inside a `HAVING` clause  
C) `GROUP BY` must precede `WHERE`  
D) Column `department` cannot be selected  
**Answer: B**  
*Explanation:* The `WHERE` clause evaluates individual rows before grouping. Group-level aggregate filtering must be placed in `HAVING AVG(salary) > 50000`.

---

#### Question 28 [Bloom's Level: L4 - Analyze]
**Analyze what happens if a database operation inside a Python transaction block encounters an unhandled exception before `conn.commit()` is reached:**
```python
try:
    cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
    raise ValueError("Network glitch")
    cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
    conn.commit()
except Exception:
    conn.rollback()
```
**What is the final state of Account 1's balance in the database?**  
A) Deducted by 100 permanently  
B) Unchanged (original balance preserved due to `conn.rollback()`)  
C) Deducted by 200  
D) Set to NULL  
**Answer: B**  
*Explanation:* The exception triggers the `except` block, executing `conn.rollback()`, which undoes the deduction on Account 1 and preserves database consistency.

---

#### Question 29 [Bloom's Level: L4 - Analyze]
**What error occurs if code attempts to execute `cursor.fetchone()` after calling `cursor.close()`?**  
A) Returns `None` silently  
B) Raises a `ProgrammingError` (or `InterfaceError`) because operations cannot be performed on a closed cursor  
C) Automatically re-opens the cursor  
D) Returns cached results  
**Answer: B**  
*Explanation:* In Python DB-API, invoking methods on a closed cursor or connection raises a programming interface exception.

---

#### Question 30 [Bloom's Level: L4 - Analyze]
**Analyze the behavior of `FOREIGN KEY (dept_id) REFERENCES departments(id) ON DELETE CASCADE` when a department record is deleted:**  
A) Deleting a department sets `dept_id` to NULL for all employees in that department  
B) Deleting a department automatically deletes all employee rows associated with that department  
C) Deletion of the department is blocked with an error  
D) It renames the department table  
**Answer: B**  
*Explanation:* `ON DELETE CASCADE` cascades the deletion of a parent record down to all dependent child records referencing its primary key.

---

#### Question 31 [Bloom's Level: L4 - Analyze]
**Why does SQLite NOT support native `RIGHT OUTER JOIN` or `FULL OUTER JOIN`?**  
A) Because SQLite is not an SQL database  
B) SQLite is designed as a minimalist embedded engine; unsupported outer joins must be simulated using `LEFT OUTER JOIN` combined with `UNION`  
C) Outer joins are forbidden in Python  
D) SQLite only supports single-table queries  
**Answer: B**  
*Explanation:* SQLite keeps its footprint compact by omitting native right/full outer join syntax, requiring developers to combine `LEFT JOIN` queries via `UNION`.

---

#### Question 32 [Bloom's Level: L4 - Analyze]
**Compare `cursor.execute()` inside a 1,000-iteration loop versus a single `cursor.executemany()` call. Why is `executemany()` drastically faster?**  
A) `executemany()` skips table constraints  
B) `executemany()` prepares and compiles the query execution plan once and sends parameter tuples in optimized batches, minimizing driver round-trips  
C) `executemany()` compresses data on disk  
D) `executemany()` executes on GPU cores  
**Answer: B**  
*Explanation:* `executemany()` amortizes query parsing and communication overhead by batching parameter bindings into a single compiled statement.

---

#### Question 33 [Bloom's Level: L4 - Analyze]
**What happens if you execute `INSERT INTO students (id, name) VALUES (1, 'Alice');` followed immediately by `INSERT INTO students (id, name) VALUES (1, 'Bob');` where `id` is the `PRIMARY KEY`?**  
A) Bob overwrites Alice  
B) An `IntegrityError` (Unique constraint failed) is raised on the second insert  
C) Both rows are inserted with duplicate IDs  
D) The database crashes  
**Answer: B**  
*Explanation:* Primary keys strictly enforce uniqueness. Inserting a duplicate primary key value violates entity integrity and raises an `IntegrityError`.

---

#### Question 34 [Bloom's Level: L4 - Analyze]
**Why does `SELECT DISTINCT dept FROM faculty;` return fewer rows than `SELECT dept FROM faculty;`?**  
A) `DISTINCT` deletes rows from the table  
B) `DISTINCT` eliminates duplicate values from the output result set, returning each unique department name only once  
C) `DISTINCT` filters out departments with odd IDs  
D) There is no difference  
**Answer: B**  
*Explanation:* `DISTINCT` eliminates duplicate tuples from query projection, returning unique values.

---

### 6.5 Level 5 & 6: Evaluate & Create (Judgment, Architecture & Design)

#### Question 35 [Bloom's Level: L5 - Evaluate]
**Evaluate the database architectural choice: An application requires concurrent multi-user write transactions across a local area network with complex analytical window functions. Which database is the optimal selection?**  
A) SQLite, because it requires zero setup  
B) PostgreSQL, because of its robust client-server architecture, multi-version concurrency control (MVCC), and rich SQL analytics support  
C) JSON flat files on a shared network drive  
D) CSV files  
**Answer: B**  
*Explanation:* PostgreSQL is an enterprise client-server RDBMS with advanced concurrency (MVCC) and analytics. SQLite locks the entire database file during writes, making it unsuitable for high concurrent multi-user network writes.

---

#### Question 36 [Bloom's Level: L5 - Evaluate]
**When transferring money between bank accounts, which isolation and transaction strategy guarantees that funds cannot be lost if a server crash occurs midway?**  
A) Execute separate `UPDATE` queries without transactions  
B) Wrap both debit and credit queries inside a single atomic transaction enclosed in a `try...except` block with `conn.commit()` on success and `conn.rollback()` on failure  
C) Write balances to a text file first  
D) Turn on `autocommit = True`  
**Answer: B**  
*Explanation:* Wrapping interdependent financial operations in a single atomic transaction satisfies the Atomicity property of ACID: both accounts update together, or neither does.

---

#### Question 37 [Bloom's Level: L6 - Create]
**Which Python function implementation correctly handles inserting a list of patient appointment dictionaries into SQLite safely using parameterized batch execution?**  
A)
```python
def insert_appointments(conn, appts):
    cursor = conn.cursor()
    sql = "INSERT INTO appointments (patient_id, doctor, appt_date) VALUES (?, ?, ?)"
    records = [(a['patient_id'], a['doctor'], a['date']) for a in appts]
    cursor.executemany(sql, records)
    conn.commit()
    cursor.close()
```
B)
```python
def insert_appointments(conn, appts):
    cursor = conn.cursor()
    for a in appts:
        cursor.execute(f"INSERT INTO appointments VALUES ('{a['patient_id']}', '{a['doctor']}')")
```
C)
```python
def insert_appointments(conn, appts):
    conn.save(appts)
```
D)
```python
def insert_appointments(conn, appts):
    cursor = conn.cursor()
    cursor.execute("INSERT ALL", appts)
```
**Answer: A**  
*Explanation:* Option A extracts parameters safely into a sequence of tuples, uses parameterized `?` placeholders with `cursor.executemany()`, commits the transaction, and closes the cursor.

---

#### Question 38 [Bloom's Level: L6 - Create]
**Design the correct SQL schema for a `courses` table where `course_id` is a unique text primary key, `credits` must be between 1 and 6, and `created_at` defaults to the current date:**  
A)
```sql
CREATE TABLE courses (
    course_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    credits INTEGER CHECK (credits >= 1 AND credits <= 6),
    created_at DATE DEFAULT CURRENT_DATE
);
```
B)
```sql
CREATE TABLE courses (
    course_id TEXT,
    title TEXT,
    credits INTEGER RANGE 1 TO 6
);
```
C)
```sql
CREATE TABLE courses (
    id AUTO_INCREMENT,
    title TEXT,
    credits BETWEEN 1 AND 6
);
```
D)
```sql
CREATE TABLE courses (
    course_id STRING,
    created_at NOW()
);
```
**Answer: A**  
*Explanation:* Option A employs valid SQL DDL: `PRIMARY KEY`, `NOT NULL`, `CHECK` domain constraint, and `DEFAULT CURRENT_DATE`.

---

#### Question 39 [Bloom's Level: L5 - Evaluate]
**Evaluate the outcome: A Data Engineer executes `df.to_sql('metrics', conn, if_exists='replace')` every minute in a live streaming pipeline. What unintended consequence will occur?**  
A) Data will accumulate smoothly row by row  
B) The table will be dropped and recreated every minute, losing all historical data collected from previous minutes  
C) SQLite will automatically convert to PostgreSQL  
D) Nothing will happen  
**Answer: B**  
*Explanation:* `if_exists='replace'` drops the existing table and creates a fresh table with only the current DataFrame's rows, wiping all historical data. In streaming, `if_exists='append'` should be used.

---

#### Question 40 [Bloom's Level: L6 - Create]
**Which query extracts the top 3 highest-earning departments by total salary budget, considering only employees with salary $\ge 30,000$?**  
A)
```sql
SELECT department, SUM(salary) AS total_budget
FROM employees
WHERE salary >= 30000
GROUP BY department
ORDER BY total_budget DESC
LIMIT 3;
```
B)
```sql
SELECT department, SUM(salary)
FROM employees
HAVING salary >= 30000
ORDER BY salary DESC;
```
C)
```sql
SELECT department, salary
FROM employees
LIMIT 3;
```
D)
```sql
SELECT TOP 3 department FROM employees;
```
**Answer: A**  
*Explanation:* Option A filters raw rows (`WHERE salary >= 30000`), aggregates by department (`GROUP BY department`), sums salaries (`SUM(salary)`), sorts descending (`ORDER BY total_budget DESC`), and limits to the top 3 (`LIMIT 3`).
