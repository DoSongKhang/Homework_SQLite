import csv
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    url_key TEXT,
    url TEXT,
    name TEXT,
    rating_average REAL,
    review_count INTEGER,
    original_price REAL,
    price REAL,
    quantity_sold INTEGER,
    category_id INTEGER
)
"""
)

with open("category_853.csv", mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            """
            INSERT OR REPLACE INTO products (
                id, url_key, url, name, rating_average, review_count, 
                original_price, price, quantity_sold, category_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                int(float(row["id"])) if row["id"] else None,
                row["url_key"],
                row["url"],
                row["name"],
                float(row["rating_average"]) if row["rating_average"] else 0.0,
                (
                    int(float(row["review_count"]))
                    if row["review_count"]
                    else 0
                ),
                float(row["original_price"]) if row["original_price"] else 0.0,
                float(row["price"]) if row["price"] else 0.0,
                (
                    int(float(row["quantity_sold"]))
                    if row["quantity_sold"]
                    else 0
                ),  # SỬA TẠI ĐÂY
                (
                    int(float(row["category_id"]))
                    if row["category_id"]
                    else None
                ),
            ),
        )

conn.commit()
conn.close()

print("Đã nhập dữ liệu thành công!")