import sqlite3

def banking_account_db():
    conn = sqlite3.connect("bank_accounts.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Account (
            account_no TEXT PRIMARY KEY,
            customer_name TEXT NOT NULL,
            account_type TEXT NOT NULL,
            balance REAL CHECK(balance >= 500.0)
        )
    """)
    
    accounts = [
        ("ACC1001", "Rajesh Khanna", "Savings", 25000.00),
        ("ACC1002", "Sunita Menon", "Current", 85000.00),
        ("ACC1003", "Amitabh Roy", "Savings", 15000.00),
        ("ACC1004", "Kavita Desai", "Savings", 45000.00),
        ("ACC1005", "Suresh Prabhu", "Current", 120000.00)
    ]
    cursor.executemany("INSERT OR IGNORE INTO Account VALUES (?, ?, ?, ?)", accounts)
    conn.commit()
    
    cursor.execute("UPDATE Account SET balance = balance + ? WHERE account_no = ?", (5000.00, "ACC1001"))
    conn.commit()
    
    cursor.execute("SELECT * FROM Account")
    records = cursor.fetchall()
    
    print("--- Bank Account Database Records ---")
    print(f"{'Account No':<12} | {'Customer Name':<16} | {'Type':<10} | {'Updated Balance ($)'}")
    print("-" * 65)
    for a in records:
        print(f"{a[0]:<12} | {a[1]:<16} | {a[2]:<10} | ${a[3]:<12,.2f}")
        
    conn.close()

if __name__ == "__main__":
    banking_account_db()
