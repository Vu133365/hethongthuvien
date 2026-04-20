from tkinter import *
from tkinter import messagebox
import pymysql


def return_book():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    def returnSql():
        bid = bookInfo1.get()

        mypass = "matkhau123"
        mydatabase = "library_db"

        try:
            con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
            cur = con.cursor()

            # 1. Kiểm tra xem sách có đang được mượn không
            check_query = f"select * from books_issued where bid = '{bid}'"
            cur.execute(check_query)
            row = cur.fetchone()

            if row:
                # 2. Xóa khỏi bảng mượn
                cur.execute(f"delete from books_issued where bid = '{bid}'")
                # 3. Cập nhật lại trạng thái trong bảng books
                cur.execute(f"update books set status = 'avail' where bid = '{bid}'")
                con.commit()
                messagebox.showinfo('Success', "Sách đã được trả thành công!")
            else:
                messagebox.showinfo("Error", "Mã sách này hiện không có trong danh sách mượn.")
        except Exception as e:
            messagebox.showinfo("Error", f"Lỗi: {e}")

        root.destroy()

    # --- GIAO DIỆN (Màu tím hoặc xanh dương cho khác biệt) ---
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#1565c0")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    Label(labelFrame, text="Book ID : ", bg='black', fg='white').place(relx=0.05, rely=0.5)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    SubmitBtn = Button(root, text="RETURN", bg='#d1ccc0', fg='black', command=returnSql)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()