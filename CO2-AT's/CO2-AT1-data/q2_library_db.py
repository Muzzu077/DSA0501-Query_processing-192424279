import sqlite3

def manage_library_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Book (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            publisher TEXT NOT NULL,
            price REAL CHECK(price > 0)
        )
    """)
    
    books = [
        ("Database System Concepts", "Silberschatz", "McGraw-Hill", 650.00),
        ("Python Data Science Handbook", "Jake VanderPlas", "O'Reilly", 550.00),
        ("Introduction to Algorithms", "Cormen", "MIT Press", 850.00),
        ("Learning SQL", "Alan Beaulieu", "O'Reilly", 420.00),
        ("Pattern Recognition and Machine Learning", "Christopher Bishop", "Springer", 920.00)
    ]
    cursor.executemany("INSERT INTO Book (title, author, publisher, price) VALUES (?, ?, ?, ?)", books)
    conn.commit()
    
    cursor.execute("UPDATE Book SET price = ? WHERE title = ?", (600.00, "Python Data Science Handbook"))
    conn.commit()
    
    cursor.execute("SELECT * FROM Book")
    records = cursor.fetchall()
    
    print("--- Updated Library Book Inventory ---")
    print(f"{'ID':<4} | {'Book Title':<42} | {'Author':<20} | {'Price (INR)'}")
    print("-" * 80)
    for b in records:
        print(f"{b[0]:<4} | {b[1]:<42} | {b[2]:<20} | Rs. {b[4]:<8.2f}")
        
    conn.close()

if __name__ == "__main__":
    manage_library_database()
