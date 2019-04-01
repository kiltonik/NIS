import tkinter as tk
from tkinter import ttk
from Presentation.MainWindow import MainWindow


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root)
    app.pack()
    root.title('Wine Reviews')
    # root.rowconfigure(0, weight=1)
    # root.columnconfigure(0, weight=1)
    # root.geometry('650x450')
    root.resizable(False, False)
    root.mainloop()
