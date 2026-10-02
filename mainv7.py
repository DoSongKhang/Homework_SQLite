import sqlite3

# =========================================================
# DATABASE
# =========================================================

DATABASE_NAME = "database.db"


def connect_db():
    return sqlite3.connect(DATABASE_NAME)


# =========================================================
# HÀM TIỆN ÍCH
# =========================================================


def run_query():
    conn = connect_db()
    cursor = conn.cursor()
    return conn, cursor


# =========================================================
# Option 1
# =========================================================


def option_1():
    conn, cursor = run_query()

    # 1. Đổi 'users' thành 'products'
    sql = "SELECT id, name, price, original_price, rating_average, review_count, quantity_sold FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()
    conn.close()

    # 2. In Tiêu đề với độ rộng phù hợp
    header = f"{'ID':<10} | {'TÊN SẢN PHẨM':<35} | {'GIÁ BÁN':<10} | {'GIÁ GỐC':<10} | {'ĐÁNH GIÁ':<8} | {'ĐÃ BÁN':<8}"
    print(header)
    print("-" * len(header))

    # 3. Duyệt và in từng dòng (cắt gọn Tên sản phẩm nếu quá dài)
    for p in products:
        p_id, name, price, orig_price, rating, reviews, sold = p

        # Cắt ngắn tên nếu dài hơn 32 ký tự để không làm vỡ khung
        short_name = name[:32] + "..." if len(str(name)) > 32 else name

        print(
            f"{str(p_id):<10} | {short_name:<35} | {price:<10,.0f} | {orig_price:<10,.0f} | {rating:<8} | {sold:<8}"
        )

    print("-" * len(header))


def option_2():
    conn, cursor = run_query()
    n = float(input("Nhập giá trị đánh giá tối thiểu (n): "))
    m = int(input("Nhập số lượng bán tối thiểu (m): "))
    # 1. Đổi 'users' thành 'products'
    sql = "SELECT name, price, quantity_sold FROM products WHERE rating_average >= ? AND quantity_sold >= ?"
    cursor.execute(sql, (n, m))
    products = cursor.fetchall()
    conn.close()

    # 2. In Tiêu đề với độ rộng phù hợp
    header = f"{'TÊN SẢN PHẨM':<35} | {'GIÁ BÁN':<10}| {'ĐÃ BÁN':<8}"
    print(header)
    print("-" * len(header))

    # 3. Duyệt và in từng dòng (cắt gọn Tên sản phẩm nếu quá dài)
    for p in products:
        name, price, sold = p

        # Cắt ngắn tên nếu dài hơn 32 ký tự để không làm vỡ khung
        short_name = name[:32] + "..." if len(str(name)) > 32 else name

        print(
            f"{short_name:<35} | {price:<10,.0f} | {sold:<8}"
        )

    print("-" * len(header))
    
def option_3():
    conn, cursor = run_query()

    # 1. Đổi 'users' thành 'products'
    n = int(input("Nhập số lượng sản phẩm cần hiển thị (n): "))
    sql = "SELECT name, price, quantity_sold FROM products ORDER BY quantity_sold DESC LIMIT ?"
    cursor.execute(sql, (n,))
    products = cursor.fetchall()
    conn.close()

    # 2. In Tiêu đề với độ rộng phù hợp
    header = f"{'TÊN SẢN PHẨM':<35} | {'GIÁ BÁN':<10}| {'ĐÃ BÁN':<8}"
    print(header)
    print("-" * len(header))

    # 3. Duyệt và in từng dòng (cắt gọn Tên sản phẩm nếu quá dài)
    for p in products:
        name, price, sold = p

        # Cắt ngắn tên nếu dài hơn 32 ký tự để không làm vỡ khung
        short_name = name[:32] + "..." if len(str(name)) > 32 else name

        print(
            f"{short_name:<35} | {price:<10,.0f} | {sold:<8}"
        )

    print("-" * len(header))
    
def option_4():
    conn, cursor = run_query()

    # 1. Đổi 'users' thành 'products'
    sql = "SELECT name, price as max_price FROM products WhERE price = (SELECT MAX(price) FROM products)"
    cursor.execute(sql)
    products = cursor.fetchall()
    conn.close()

    # 2. In Tiêu đề với độ rộng phù hợp
    header = f"{'TÊN SẢN PHẨM':<35} | {'GIÁ CAO NHẤT':<15}"
    print(header)
    print("-" * len(header))

    # 3. Duyệt và in từng dòng (cắt gọn Tên sản phẩm nếu quá dài)
    for p in products:
        name, max_price = p

        # Cắt ngắn tên nếu dài hơn 32 ký tự để không làm vỡ khung
        short_name = name[:32] + "..." if len(str(name)) > 32 else name

        print(
            f"{short_name:<35} | {max_price:<15,.0f}"
        )

    print("-" * len(header))

#Tính tổng số tiền tiết kiệm được (giá gốc - giá bán) cho mỗi sản phẩm
def option_5():
    conn, cursor = run_query()

    # 1. Đổi 'users' thành 'products'
    sql = "SELECT name, original_price - price as savings FROM products order by savings desc"
    cursor.execute(sql)
    products = cursor.fetchall()
    conn.close()

    # 2. In Tiêu đề với độ rộng phù hợp
    header = f"{'TÊN SẢN PHẨM':<35} | {'TIẾT KIỆM':<15}"
    print(header)
    print("-" * len(header))

    # 3. Duyệt và in từng dòng (cắt gọn Tên sản phẩm nếu quá dài)
    for p in products:
        name, savings = p

        # Cắt ngắn tên nếu dài hơn 32 ký tự để không làm vỡ khung
        short_name = name[:32] + "..." if len(str(name)) > 32 else name

        print(
            f"{short_name:<35} | {savings:<15,.0f}"
        )

    print("-" * len(header))

def option_6():
    conn, cursor = run_query()
    
    search_term = input("Nhập từ khóa tìm kiếm: ")
    sql = "SELECT id, name, price, rating_average FROM products WHERE name LIKE ?"
    cursor.execute(sql, (f"%{search_term}%",))
    products = cursor.fetchall()
    conn.close()
    header = (
        f"{'ID':<10} | {'TÊN SẢN PHẨM':<35} | {'GIÁ BÁN':<10} | {'ĐÁNH GIÁ':<8} |"
    )
    print(header)
    print("-" * len(header))

    for p in products:
        # Sửa thứ tự gán biến cho khớp với SQL SELECT (price trước, rating sau)
        p_id, name, price, rating = p

        short_name = name[:32] + "..." if len(str(name)) > 32 else name

        print(
            f"{str(p_id):<10} | {short_name:<35} | {price:<10,.0f} | {rating:<8} |"
        )

    print("-" * len(header))

def option_7():
    conn, cursor = run_query()
    
    sql = "SELECT MAX(price) as max_price, MIN(price) as min_price, AVG(price) as avg_price FROM products"
    cursor.execute(sql)
    products = cursor.fetchall()
    conn.close()
    header = (
        f"{'GIÁ CAO NHẤT':<10} | {'GIÁ THẤP NHẤT':<10} | {'GIÁ TRUNG BÌNH':<10} |"
    )
    print(header)
    print("-" * len(header))

    for p in products:
        # Sửa thứ tự gán biến cho khớp với SQL SELECT (price trước, rating sau)
        max_price, min_price, avg_price = p

        print(
            f" {max_price:<13,.0f} | {min_price:<13,.0f} | {avg_price:<12,.0f} |"
        )

    print("-" * len(header))

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Hiển thị sản phẩm có đánh giá >= n và đã bán >= m")
        print("3. Hiển thị n sản phẩm bán chạy nhất")
        print("4. Hiển thị sản phẩm có giá cao nhất")
        print("5. Tính tổng số tiền tiết kiệm được cho mỗi sản phẩm")
        print("6. Tìm kiếm sản phẩm có tên chứa 'Your Typing'")
        print("7. Thống kê giá cao nhất, thấp nhất và trung bình của sản phẩm")
        print("0. Thoát")

        choice = input("Chọn một tùy chọn: ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "5":
            option_5()
        elif choice == "6":
            option_6()
        elif choice == "7":
            option_7()
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")


if __name__ == "__main__":
    main()