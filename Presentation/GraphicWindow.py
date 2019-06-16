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
    __BD = BD.inst()

    def __init__(self):
        super().__init__()
        self.init_graphic_window()

    def init_graphic_window(self):
        f = Figure(figsize=(15, 10))
        a = f.add_subplot(1, 1, 1)
        tough = 0.9
        mylist = []
        data = self.__BD.provide_wine_data()
        secondlist = np.arange(11,17,1)
        for i in list(data.keys()):
            if data[i]['Price'] != 'nan':
                if float(data[i]['Price']) == 12: mylist.append(0)
                if float(data[i]['Price']) == 13: mylist.append(1)
                if float(data[i]['Price']) == 14: mylist.append(2)
                if float(data[i]['Price']) == 15: mylist.append(3)
                if float(data[i]['Price']) == 16: mylist.append(4)
        a.hist(mylist, np.arange(6), rwidth=tough, label='Number of wines')
        a.legend()
        a.set_xlabel('Country')
        a.set_ylabel('Amount')
        a.set_title('Wines with points <17 amount histogram')
        a.set_xticks(range(4))
        a.set_xticklabels(('Mexico', 'Italy', 'Australia', 'US', 'France'))
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM)