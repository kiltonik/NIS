import os
import tkinter as tk
import pandas

class ExportBDWindow(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.grab_set()
        self.init_export_bd_window()

    def init_export_bd_window(self):

        wine_path = tk.Entry(self, width=100)
        wine_path.grid(row=0, padx=3, pady=3)

        province_path = tk.Entry(self, width=100)
        province_path.grid(row=1, padx=3, pady=3)

        country_path = tk.Entry(self, width=100)
        country_path.grid(row=2, padx=3, pady=3)

        button = tk.Button(self, text='Сохранить', command=lambda:{pandas.read_csv(data[2], encoding='utf-8').
                           to_csv(wine_path.get()+'\\Wine info'),
                        pandas.read_csv(data[1], encoding='utf-8').to_csv(province_path.get() + '\\Province info'),
                        pandas.read_csv(data[0], encoding='utf-8').to_csv(country_path.get()+'\\Country info'),
                        self.destroy()})
        button.grid(row=3, padx=3, pady=3)

        f = open(os.path.dirname(os.path.realpath(__file__))[:-12] + 'Params.txt', 'r')
        data = f.read().split('\n')


