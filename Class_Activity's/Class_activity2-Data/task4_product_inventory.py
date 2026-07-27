import json

def create_products_json():
    filename = "products.json"
    
    products = [
        {"Product ID": "P1001", "Product Name": "Wireless Mechanical Keyboard", "Category": "Electronics", "Price": 129.99, "Quantity Available": 45},
        {"Product ID": "P1002", "Product Name": "Ergonomic Gaming Mouse", "Category": "Electronics", "Price": 59.99, "Quantity Available": 80},
        {"Product ID": "P1003", "Product Name": "UltraWide 34-inch Monitor", "Category": "Monitors", "Price": 499.50, "Quantity Available": 20},
        {"Product ID": "P1004", "Product Name": "Noise Cancelling Headphones", "Category": "Audio", "Price": 249.00, "Quantity Available": 35},
        {"Product ID": "P1005", "Product Name": "USB-C Multi-Port Hub", "Category": "Accessories", "Price": 39.95, "Quantity Available": 150},
        {"Product ID": "P1006", "Product Name": "HD Webcam 1080p", "Category": "Electronics", "Price": 79.99, "Quantity Available": 60},
        {"Product ID": "P1007", "Product Name": "Standing Desk Converter", "Category": "Furniture", "Price": 189.00, "Quantity Available": 15},
        {"Product ID": "P1008", "Product Name": "Portable SSD 1TB", "Category": "Storage", "Price": 109.99, "Quantity Available": 90},
        {"Product ID": "P1009", "Product Name": "Smart Fitness Band", "Category": "Wearables", "Price": 49.99, "Quantity Available": 110},
        {"Product ID": "P10010", "Product Name": "Adjustable Monitor Arm", "Category": "Accessories", "Price": 69.50, "Quantity Available": 40}
    ]
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4)
        
    print(f"Successfully generated '{filename}' containing {len(products)} products.")

def display_products_summary():
    print("\n--- Product Inventory Summary ---")
    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)
        print(f"{'ID':<8} | {'Product Name':<30} | {'Category':<14} | {'Price':<10} | {'Stock'}")
        print("-" * 75)
        for p in products:
            print(f"{p['Product ID']:<8} | {p['Product Name']:<30} | {p['Category']:<14} | ${p['Price']:<9.2f} | {p['Quantity Available']}")

if __name__ == "__main__":
    create_products_json()
    display_products_summary()
