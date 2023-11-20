import sys
import tkinter as tk
import ttkbootstrap as ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PlotFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.add_plot()




    def add_plot(self):
        figure, ax = plt.subplots()
        # ax = figure.add_subplot()
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) 
        my_plot = FigureCanvasTkAgg(figure, self)
        my_plot.get_tk_widget().grid(column=0, row=0)

        # Close all plot figures
        plt.close('all')
        


class App(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.configure(padx=40, pady=20)
        self.resizable(0, 0)

        self.plot = PlotFrame(self)
        self.plot.grid(column=0, row=0)




# Запуск программы
if __name__ == "__main__":
    app = App(title="Курсы валют", themename='minty', minsize=(500, 500))
    app.mainloop()