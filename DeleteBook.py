from tkinter import *
from tkinter import messagebox
import pymysql


def delete_book():  # Đảm bảo tên hàm này khớp với file main của bạn
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # --- HÀM XỬ LÝ XÓA (Nằm bên trong để thấy biến bookInfo1) ---
    def deleteSql():
        bid = bookInfo1.get()  # Bây giờ nó đã hiểu bookInfo1 là gì

        mypass = "matkhau123"
        mydatabase = "library_db"

        try:
            con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
            cur = con.cursor()

            # Thực hiện xóa
            curr_delete = f"delete from books where bid = '{bid}'"
            cur.execute(curr_delete)
            con.commit()

            # Xóa luôn ở bảng mượn sách nếu có
            cur.execute(f"delete from books_issued where bid = '{bid}'")
            con.commit()

            messagebox.showinfo('Success', "Đã xóa sách thành công!")
        except Exception as e:
            messagebox.showinfo("Error", f"Lỗi: {e}")

        root.destroy()

    # --- GIAO DIỆN ---
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")  # Màu xanh lá
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.5)

    # ĐỊNH NGHĨA bookInfo1 Ở ĐÂY
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Nút bấm gọi hàm deleteSql ở trên
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=deleteSql)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()