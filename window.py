import re
from datetime import date
from tkinter import *
import tkinter.ttk as ttk
from ttkbootstrap import widgets
from dateutil import parser
from dateutil.relativedelta import relativedelta


class MainWindow:
    def __init__(self, master):
        # FRAME ROOT
        self.window_root = ttk.Frame(master)
        self.window_root.configure(height=470,
                                   width=420)

        # FRAME LABELS NAMES APP
        self.frameNameApps = ttk.Frame(self.window_root)
        self.frameNameApps.configure(width=200, height=200)

        self.labelNameApp = ttk.Label(self.frameNameApps)
        self.labelNameApp.configure(anchor="center",
                                    cursor="arrow",
                                    font="{Ivi} 15 {bold}",
                                    justify="center",
                                    padding="0 15",
                                    text='CALCULADORA',
                                    width=30)

        self.labelNameApp2 = ttk.Label(self.frameNameApps)
        self.labelNameApp2.configure(anchor="center",
                                     compound="center",
                                     font="{Arial} 25 {bold}",
                                     justify="center",
                                     text='DE IDADE',
                                     width=20)

        # FRAME USERS DATA
        self.frameData = ttk.Frame(self.window_root)
        self.frameData.configure(height=200,
                                 padding='0 30 0 30',
                                 width=200)

        self.labelDateNow = ttk.Label(self.frameData)
        self.labelDateNow.configure(font="{Ubuntu} 12 {}",
                                    justify="left",
                                    text='Data Inicial')
        self.entryDateNow = widgets.DateEntry(self.frameData)
        self.patternNow = self.window_root.register(self.verifyPatternNow)
        self.entryDateNow.entry.configure(validate='focus', validatecommand=self.patternNow)
        self.entryDateNow.entry.bind('<Return>', lambda e: self.entryDateBorn.entry.focus() if self.verifyPatternNow()
                                                                                            else self.entryDateNow.entry.focus())
        self.dateNowVar = self.entryDateNow.entry

        self.labelDateBorn = ttk.Label(self.frameData)
        self.labelDateBorn.configure(font="{Ubuntu} 12 {}",
                                     justify="left",
                                     text='Data de nascimento')
        self.entryDateBorn = widgets.DateEntry(self.frameData)
        self.patternBorn = self.window_root.register(self.verifyPatternBorn)
        self.entryDateBorn.entry.configure(validate='focus', validatecommand=self.patternBorn)
        self.entryDateBorn.entry.bind('<Return>', lambda e: self.calculate() if self.verifyPatternBorn()
                                                                            else self.entryDateBorn.entry.focus())
        self.dateBornVar = self.entryDateBorn.entry

        # FRAME SHOW INFO
        self.frameInfos = ttk.Frame(self.window_root)
        self.frameInfos.configure(height=200, width=200)

        self.LabelYears = ttk.Label(self.frameInfos)
        self.LabelYears.configure(font="{Ivi} 20 {}",
                                  padding="20 40 20 10",
                                  text='27')

        self.labelYears = ttk.Label(self.frameInfos)
        self.labelYears.configure(text='anos')

        self.LabelMonth = ttk.Label(self.frameInfos)
        self.LabelMonth.configure(font="{Ivi} 20 {}",
                                  padding="20 40 20 10",
                                  text='17')

        self.labelMonth = ttk.Label(self.frameInfos)
        self.labelMonth.configure(text='meses')

        self.LabelDays = ttk.Label(self.frameInfos)
        self.LabelDays.configure(font="{Ivi} 20 {}",
                                 padding="20 40 20 10",
                                 text='10')

        self.labelDays = ttk.Label(self.frameInfos)
        self.labelDays.configure(text='dias')

        self.btn_calculate = ttk.Button(self.frameInfos, command=self.calculate)
        self.btn_calculate.configure(text='Calcular Idade',
                                     padding='0 20',
                                     width=20)

        # ACTIVITY WHEN CONFIGURATION GADGETS FINISH
        self.grid_widgets()

        # GIVE FIRST FOCUS
        self.entryDateNow.focus()

    def grid_widgets(self):
        # FRAME ROOT
        self.window_root.grid(column=0, row=0)

        # FRAME LABELS NAMES APP
        self.frameNameApps.grid(row=0, column=0)

        self.labelNameApp.grid(column=0, row=0)
        self.labelNameApp2.grid(column=0, row=1)

        # FRAME USERS DATA
        self.frameData.grid(row=2, column=0)

        self.labelDateNow.grid(column=0, row=2, sticky="w")
        self.entryDateNow.grid(column=1, padx="30 10", pady=10, row=2)

        self.labelDateBorn.grid(column=0, row=3, sticky="w")
        self.entryDateBorn.grid(column=1, padx="30 10", pady=10, row=3)

        # FRAME SHOW INFO
        self.frameInfos.grid(row=4, column=0)

        self.LabelYears.grid(column=0, row=4)
        self.labelYears.grid(column=0, row=5)

        self.LabelMonth.grid(column=1, row=4)
        self.labelMonth.grid(column=1, row=5)

        self.LabelDays.grid(column=2, row=4)
        self.labelDays.grid(column=2, row=5)

        self.btn_calculate.grid(column=0, columnspan=3, pady="50 20", row=6, sticky="s")

    def verifyPatternNow(self):
        # PATTER DATE
        datePattern = re.compile(r'^((\d\d)/(\d\d)/(\d\d\d\d))$')
        if datePattern.match(self.dateNowVar.get()):
            return True
        else:
            return False

    def verifyPatternBorn(self):
        # PATTER DATE
        datePattern = re.compile(r'^((\d\d)/(\d\d)/(\d\d\d\d))$')
        if datePattern.match(self.dateBornVar.get()):
            return True
        else:
            return False
    def calculate(self):
        # Divide as partes da data
        dayBorn, monthBorn, yearBorn = [int(x) for x in self.dateBornVar.get().split('/')]
        dayNow, monthNow, yearNow = [int(x) for x in self.dateNowVar.get().split('/')]

        # Formata a data
        bornDate = date(yearBorn, monthBorn, dayBorn)
        nowDate = date(yearNow, monthNow, dayNow)

        # Calcula a diferença
        year = relativedelta(nowDate, bornDate).years
        month = relativedelta(nowDate, bornDate).months
        days = relativedelta(nowDate, bornDate).days

        # Desenha o resultado
        self.LabelYears['text'] = year
        self.LabelMonth['text'] = month
        self.LabelDays['text'] = days

        # GIVE FOCUS
        self.entryDateNow.entry.focus()