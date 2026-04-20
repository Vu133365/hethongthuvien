from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def view_books():
    root = Tk()
    root.title("View Book List")
    root.minsize(width=400, height=400)
    root.geometry("800x600")

    # Kết nối database
    mypass = "matkhau123"      
    mydatabase = "library_db"

    try:
        con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
        cur = con.cursor()
    except Exception as e:
        messagebox.showerror("Error", f"Không thể kết nối Database!\n{e}")
        root.destroy()
        return

    # === Giao diện ===
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12c2e9")          # Màu nền xanh dương nhạt
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', 
                         font=('Courier', 18, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Frame chứa Treeview
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.6)

    # Treeview để hiển thị bảng
    tree = ttk.Treeview(labelFrame, columns=("bid", "title", "author", "status"), show='headings')

    # Định nghĩa tiêu đề cột
    tree.heading("bid", text="Book ID")
    tree.heading("title", text="Title")
    tree.heading("author", text="Author")
    tree.heading("status", text="Status")

    tree.column("bid", width=100, anchor=CENTER)
    tree.column("title", width=250, anchor=W)
    tree.column("author", width=200, anchor=W)
    tree.column("status", width=100, anchor=CENTER)

    # Scrollbar dọc
    vsb = ttk.Scrollbar(labelFrame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)

    tree.pack(side=LEFT, fill=BOTH, expand=True, padx=(10,0), pady=10)
    vsb.pack(side=RIGHT, fill=Y, pady=10)

    # === Lấy dữ liệu từ MySQL ===
    try:
        cur.execute("SELECT bid, title, author, status FROM books ORDER BY bid")
        rows = cur.fetchall()

        if not rows:
            messagebox.showinfo("Thông báo", "Thư viện hiện chưa có sách nào!")
        else:
            for row in rows:
                # Hiển thị status đẹp hơn: Available / Issued
                status_display = "Available" if row[3].lower() == "avail" else "Issued"
                tree.insert("", END, values=(row[0], row[1], row[2], status_display))

    except Exception as e:
        messagebox.showerror("Error", f"Lỗi khi lấy dữ liệu: {e}")

    # Nút Quit
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', 
                     command=root.destroy, font=("Arial", 12))
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.08)

    root.mainloop()