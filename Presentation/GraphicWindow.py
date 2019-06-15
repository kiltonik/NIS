import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from Data.BD import BD
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GraphicWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.init_graphic_window()

    def init_graphic_window(self):
        f = Figure(figsize=(15, 10))
        a = f.add_subplot(1, 1, 1)
        tough = 0.9
        mylist = [1, 2, 2, 3, 3, 3, 5, 5]
        secondlist = [0, 1, 2, 3, 4, 5]
        a.hist(mylist, secondlist, rwidth=tough, label='Number of gyms')
        a.legend()
        a.set_xlabel('Areas')
        a.set_ylabel('Amount')
        a.set_title('Gyms amount by area histogram')
        a.set_xticks(range(13))
        a.set_xticklabels(('Central', 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'Zelenograd', 'Trinity', 'Novomosk'))
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM)