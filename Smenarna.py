from os.path import basename, splitext
from re import L
import tkinter as tk
import random
from tkinter import  CENTER, E, END, LEFT, TOP,  N, W, UNDERLINE, BOTTOM, HORIZONTAL, Label, Button, Scale,  StringVar, Frame, Entry , Listbox,Radiobutton,LabelFrame

        # Základ

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Smenarna (rubly nevedeme)"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        
        self.lbl = tk.Label(self, text="Směnárna")
        self.lbl.grid(row=0, column=0)
        
        
        # Labelframe
        
        self.labelframe = tk.LabelFrame(self , text="Transakce")
        self.labelframe.grid(row=1,column=0, sticky = W)
        
        # Nakup a prodej
        
        self.variable = tk.IntVar(self)
        
        self.radiobutton1 = Radiobutton(self.labelframe, text="Nákup", variable=self.variable, value=1)
        self.radiobutton1.grid()
        
        self.radiobutton2 = Radiobutton(self.labelframe, text="Prodej", variable=self.variable, value=2)
        self.radiobutton2.grid()
        self.variable.set(1)

        # mena

        self.labelframeMen = tk.LabelFrame(self , text="Měna")
        self.labelframeMen.grid(row=2,column=0,sticky = W)
        
        self.listbox = tk.Listbox(self.labelframeMen)
        self.listbox.grid()
        self.listbox.bind("<ButtonRelease-1>", self.reakce)       
        
        # nacteni ze souboru
        
        f = open('listek.txt', 'r')
        slovnik = {}
        for line in f:
            self.listbox.insert(tk.END,line.split()[0])
            slovnik[line.split()[0]] = (line.split()[1:])

        # Kurz
        
        self.labelframe2 = tk.LabelFrame(self , text="Kurz")
        self.labelframe2.grid(row=3,column=0, sticky = W)
        
        
        self.hodnota = tk.StringVar()
        
        self.cena = tk.IntVar()
        self.cenaLbl= tk.Label(self.labelframe2, textvariable=self.cena) 
        self.cenaLbl.grid()
        
        self.hodnotal= tk.Label(self.labelframe2, textvariable= self.hodnota) 
        self.hodnotal.grid()

        # Vypocet
        
        self.labelframe3 = tk.LabelFrame(self , text="Kolik jich chceš")
        self.labelframe3.grid(row=4,column=0,sticky = W )
        
        self.LabelVypln = tk.Label(self.labelframe3)
        self.LabelVypln.grid()
        
        self.mnozstvi = tk.Entry(self.labelframe3)
        self.mnozstvi.grid()
        
        self.LabelVypln2 = tk.Label(self.labelframe3)
        self.LabelVypln2.grid()
        
        self.btn2 = tk.Button(self.labelframe3, text="Výpočet", command=self.vypocet)
        self.btn2.grid()
        
        # Vysledek 
        
        self.labelframe4 = tk.LabelFrame(self , text="Výsledek")
        self.labelframe4.grid(row=5,column=0)

        self.vysledek = tk.IntVar()
        self.vysledekl= tk.Label(self.labelframe4, textvariable= self.vysledek)
        self.vysledekl.grid()
        
        self.lbl4 = tk.Label(self)
        self.lbl4.grid()
        

        #Quit

        self.bind("<Escape>", self.quit)
        self.btn1 = tk.Button(self, text="Quit", command = self.quit)
        self.btn1.grid(row=13, column=0)

        #funkce

    def vypocet(self,event=None):

        a = int(self.mnozstvi.get())
        b = int(self.cena.get())
        c = float(self.hodnota.get().replace(",","."))
        self.vysledekVar = float(a*c/b)
        self.vysledek.set(self.vysledekVar)

    def reakce(self, event):
        index = self.listbox.curselection()[0]
        f = open("listek.txt")
        self.lines = f.readlines()
        self.cenaVar = self.lines[index].split()[1]
        self.cena.set(self.cenaVar)
        if self.variable.get() == 1: 
            self.hodnotaVar = self.lines[index].split()[3] 
        else:
            self.hodnotaVar = self.lines[index].split()[2] 
        self.hodnota.set(self.hodnotaVar)

    
    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()