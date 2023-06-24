from tkinter import *
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # Create entry widget
        self.entry = Entry(master, width=45, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        
        # Create buttons
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("+", 1, 3)
        self.create_button("C", 1, 4)
        
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3)
        self.create_button("(", 2, 4)
        
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("*", 3, 3)
        self.create_button(")", 3, 4)
        
        self.create_button(".", 4, 0)
        self.create_button("0", 4, 1)
        self.create_button("pi", 4, 2)
        self.create_button("/", 4, 3)
        self.create_button("=", 4, 4)
        
        self.create_button("sin", 5, 0)
        self.create_button("cos", 5, 1)
        self.create_button("tan", 5, 2)
        self.create_button("log", 5, 3)
        self.create_button("sqrt", 5, 4)
        
        self.create_button("MC", 6, 0)
        self.create_button("MR", 6, 1)
        self.create_button("MS", 6, 2)
        self.create_button("M+", 6, 3)
        self.create_button("M-", 6, 4)

    def create_button(self, text, row, column):
        button = Button(self.master, text=text, padx=20, pady=10, command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        if text == "C":
            self.entry.delete(0, END)
        elif text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        elif text == "sqrt":
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        elif text == "pi":
            self.entry.insert(END, math.pi)
        elif text == "sin":
            try:
                result = math.sin(float(self.entry.get()))
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        elif text == "cos":
            try:
                result = math.cos(float(self.entry.get()))
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        elif text == "tan":
            try:
                result = math.tan(float(self.entry.get()))
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        elif text == "log":
            try:
                result = math.log10(float(self.entry.get()))
                self.entry.delete(0, END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        elif text == "MC":
            self.memory = 0
        elif text == "MR":
            self.entry.delete(0, END)
            self.entry.insert(0, self.memory)
        elif text == "MS":
            self.memory = float(self.entry.get())
            self.entry.delete(0, END)
        elif text == "M+":
            self.memory += float(self.entry.get())
            self.entry.delete(0, END)
        elif text == "M-":
            self.memory -= float(self.entry.get())
            self.entry.delete(0, END)
        else:
            self.entry.insert(END, text)

def run(self):
    self.master.mainloop()

if __name__ == "__main__":
    root = Tk()
    my_calculator = Calculator(root)
    root.mainloop()