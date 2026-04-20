from tkinter import *
from PIL import ImageTk, Image
from AddBook import add_book
from DeleteBook import delete_book
from ViewBooks import view_books
from IssueBook import issue_book
from ReturnBook import return_book

# ====== MAIN WINDOW ======
root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# ====== BACKGROUND ======
bg = Image.open("lip.jpg")
bg = bg.resize((800, 600))
bg_img = ImageTk.PhotoImage(bg)

canvas = Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_img, anchor="nw")
# ====== TITLE BOX ======
title_frame_border = Frame(root, bg="#FFBB00", bd=0) # Màu vàng cam
title_frame_border.place(relx=0.5, rely=0.2, anchor="center")

title_frame = Frame(title_frame_border, bg="black", bd=0, highlightthickness=3, highlightbackground="#FFBB00")
title_frame.pack(padx=2, pady=2)

title_label = Label(
    title_frame,
    text="Welcome to\nDataFlair Library",
    bg="black",
    fg="white",
    font=("Arial", 18, "bold"),
    justify="center",
    padx=50,
    pady=10
)
title_label.pack()

# ====== BUTTON FRAME ======
btn_frame = Frame(root, bg="black")
btn_frame.place(relx=0.5, rely=0.6, anchor="center")

# ====== BUTTON STYLE ======
btn_style = {
    "font": ("Arial", 12),
    "bg": "black",
    "fg": "white",
    "width": 25,
    "height": 2,
    "bd": 1
}

# ====== BUTTONS ======
Button(btn_frame, text="Add Book Details", command=add_book, **btn_style).pack(pady=5)
Button(btn_frame, text="Delete Book", command=delete_book, **btn_style).pack(pady=5)
Button(btn_frame, text="View Book List", command=view_books, **btn_style).pack(pady=5)
Button(btn_frame, text="Issue Book to Student", command=issue_book, **btn_style).pack(pady=5)
Button(btn_frame, text="Return Book", command=return_book, **btn_style).pack(pady=5)
root.mainloop()

