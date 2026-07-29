import sqlite3

def retail_inventory_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Product (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER CHECK(quantity >= 0),
            unit_price REAL CHECK(unit_price > 0)
        )
    """)
    
    products = [
        ("Wireless Mouse", "Electronics", 25, 599.00),
        ("Mechanical Keyboard", "Electronics", 5, 2499.00),
        ("USB-C Hub", "Accessories", 8, 899.00),
        ("27-inch Monitor", "Monitors", 15, 14500.00),
        ("HD Webcam", "Electronics", 4, 1800.00)
    ]
    cursor.executemany("INSERT INTO Product (product_name, category, quantity, unit_price) VALUES (?, ?, ?, ?)", products)
    conn.commit()
    
    cursor.execute("UPDATE Product SET quantity = quantity + 20 WHERE quantity < 10")
    conn.commit()
    
    cursor.execute("SELECT * FROM Product")
    records = cursor.fetchall()
    
    print("--- Updated Product Inventory ---")
    print(f"{'ID':<4} | {'Product Name':<22} | {'Category':<14} | {'Stock Qty':<10} | {'Unit Price (INR)'}")
    print("-" * 75)
    for p in records:
        print(f"{p[0]:<4} | {p[1]:<22} | {p[2]:<14} | {p[3]:<10} | Rs. {p[4]:<10.2f}")
        
    conn.close()

if __name__ == "__main__":
    retail_inventory_db()
