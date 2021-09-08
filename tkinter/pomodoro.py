from tkinter import *


screen = Tk()
screen.title("Pomodoro")
screen.config(bg="#ffb319")




# UI Design
my_canvas = Canvas(width=300,height=250)

tomato= PhotoImage(file="tomato.png")
my_canvas.create_image(150,125,image=tomato)
my_canvas.pack()





screen.mainloop()