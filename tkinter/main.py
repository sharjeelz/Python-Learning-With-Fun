import tkinter
import tkinter as tk
import math

screen = tk.Tk()

screen.title("Convertor")

screen.config(padx=20, pady=20)
screen.config(bg='dark khaki')



my_label = tk.Label(text="C To F Convertor", font=("Arial", 12, "bold"))
my_label.grid(column=2, row=0)


c_label = tk.Label(text="Centrigrade", font=("Arial", 8))
c_label.grid(column=0, row=2)

c = tkinter.Entry(validate="all")

c.grid(column=2,row=2)

f = tk.Label(text="F", font=("Arial", 18))


f.grid(column=2,row=3)

def convert():
    if(c.get()):
        fei= round(int(c.get())*(9/5)+32)
        f.config(text=f"{fei} F")
    else:
        screen.bell()



convert_button = tkinter.Button(text="Covert",command=convert)
convert_button.grid(column=3,row=2)











screen.mainloop()
