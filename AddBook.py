from tkinter import *
import pymysql
from tkinter import messagebox


def add_book():
    # Cửa sổ phụ
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Kết nối Database (Dùng thông tin đã thống nhất)
    mypass = "matkhau123"
    mydatabase = "library_db"
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Hàm xử lý khi nhấn Submit
    def bookRegister():
        bid = bookInfo1.get()
        title = bookInfo2.get()
        author = bookInfo3.get()
        status = bookInfo4.get()
        status = status.lower()

        insertSql = f"insert into books values ('{bid}','{title}','{author}','{status}')"
        try:
            cur.execute(insertSql)
            con.commit()
            messagebox.showinfo('Success', "Đã thêm sách thành công!")
        except:
            messagebox.showinfo("Error", "Không thể thêm sách (Trùng ID hoặc lỗi DB)")
        root.destroy()

    # --- BẮT ĐẦU VẼ GIAO DIỆN GIỐNG MẪU ---
    # Nền cam
    canvas1 = Canvas(root)
    canvas1.config(bg="#ff6e40")
    canvas1.pack(expand=True, fill=BOTH)

    # Khung tiêu đề "Add Books"
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Khung đen chứa các ô nhập
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Dòng 1: Book ID
    Label(labelFrame, text="Book ID : ", bg='black', fg='white').place(relx=0.05, rely=0.2)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Dòng 2: Title
    Label(labelFrame, text="Title : ", bg='black', fg='white').place(relx=0.05, rely=0.35)
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62)

    # Dòng 3: Author
    Label(labelFrame, text="Author : ", bg='black', fg='white').place(relx=0.05, rely=0.50)
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62)

    # Dòng 4: Status
    Label(labelFrame, text="Status(Avail/issued) : ", bg='black', fg='white').place(relx=0.05, rely=0.65)
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62)

    # Nút bấm Submit và Quit
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()