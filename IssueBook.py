from tkinter import *
from tkinter import messagebox
import pymysql

def issue_book():
    root = Tk()
    root.title("Issue Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    def issueSql():
        bid = bookInfo1.get().strip()

        if not bid:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập Book ID!")
            return

        mypass = "matkhau123"
        mydatabase = "library_db"

        try:
            con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
            cur = con.cursor()

            # Kiểm tra sách có tồn tại và còn Available không
            cur.execute("SELECT status FROM books WHERE bid = %s", (bid,))
            row = cur.fetchone()

            if not row:
                messagebox.showinfo("Error", "Không tìm thấy sách với Book ID này!")
                return

            if row[0].lower() != "avail":
                messagebox.showinfo("Error", "Sách này hiện không có sẵn để mượn!")
                return

            # Thêm vào bảng books_issued
            cur.execute("INSERT INTO books_issued (bid, issuedto) VALUES (%s, %s)", 
                       (bid, "Student"))   # Bạn có thể thêm Entry để nhập tên sinh viên sau

            # Cập nhật trạng thái sách thành 'issued'
            cur.execute("UPDATE books SET status = 'issued' WHERE bid = %s", (bid,))

            con.commit()
            messagebox.showinfo('Success', f"Đã mượn sách thành công!\nBook ID: {bid}")

        except pymysql.IntegrityError:
            messagebox.showerror("Error", "Sách này đã được mượn trước đó!")
        except Exception as e:
            messagebox.showerror("Error", f"Lỗi: {e}")
        finally:
            if 'con' in locals() and con.is_connected():
                con.close()
            root.destroy()

    # === Giao diện ===
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#e67e22")      # Màu cam nổi bật cho chức năng mượn
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', 
                         font=('Courier', 15, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.4)

    Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=("Arial", 12)).place(relx=0.05, rely=0.4)
    bookInfo1 = Entry(labelFrame, font=("Arial", 12))
    bookInfo1.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Nút Submit và Quit
    SubmitBtn = Button(root, text="ISSUE", bg='#d1ccc0', fg='black', 
                       command=issueSql, font=("Arial", 12, "bold"))
    SubmitBtn.place(relx=0.28, rely=0.85, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', 
                     command=root.destroy, font=("Arial", 12))
    quitBtn.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)

    root.mainloop()