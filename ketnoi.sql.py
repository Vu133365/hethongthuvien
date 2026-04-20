import mysql.connector

try:
    # 1. Kết nối vào MySQL Server
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="matkhau123"  # Mật khẩu mới bạn đã đặt
    )

    cursor = db.cursor()

    # 2. Tạo Database library_db
    cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
    cursor.execute("USE library_db")
    print("--- Đã truy cập vào database library_db ---")

    # 3. Tạo bảng 'books'
    # bid là khóa chính (PRIMARY KEY)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            bid VARCHAR(20) NOT NULL,
            title VARCHAR(30),
            author VARCHAR(30),
            status VARCHAR(30),
            PRIMARY KEY (bid)
        )
    """)
    print("1. Đã tạo bảng 'books' thành công.")

    # 4. Tạo bảng 'books_issued'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books_issued (
            bid VARCHAR(20) NOT NULL,
            issuedto VARCHAR(30),
            PRIMARY KEY (bid)
        )
    """)
    print("2. Đã tạo bảng 'books_issued' thành công.")

    print("\n--- TẤT CẢ ĐÃ HOÀN TẤT! ---")

except mysql.connector.Error as err:
    print(f"Lỗi rồi: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        db.close()