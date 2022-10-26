from tkinter import *
from window import MainWindow

class MainApp:
    def __init__(self):
        self.master= Tk()
        self.master.title("Calculadora de Idade")
        self.master.configure(bg='#ffffff')

        # Window configuations
        self.width = 420
        self.height = 500

        self.width_sys = int(self.master.winfo_screenwidth() / 2 - self.width / 2)
        self.height_sys = int(self.master.winfo_screenheight() / 2 - self.height / 2)

        self.master.resizable(width=False, height=False)
        self.master.geometry(f'{self.width}x{self.height}+{self.width_sys}+{self.height_sys}')

        # Start Program
        self.mainWIndow = MainWindow(self.master)
        self.master.mainloop()


if __name__ == '__main__':
    MainApp()
