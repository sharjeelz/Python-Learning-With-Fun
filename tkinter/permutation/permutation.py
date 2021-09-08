from tkinter import *
from images import images_list
import time
from PIL import Image, ImageTk
import pandas
# UI Creation
window = Tk()
window.minsize(width=500, height=400)
window.title("Readability Index Text (اردو)")
window.wm_iconbitmap("heart.ico")
running = True
window.config(bg="white")

canvas = Canvas(width=260, height=260)
canvas.config(bg="white", highlightthickness=0)
tt = iter(images_list)
start = 0
image_for_garbage = {}
data = []

timer = Label(window, bg="white")
timer.pack()

def yes(event):
    end = time.time()
    timer.config(text='clicked  Yes % .3f s' % (end - start))
    window.unbind('1')
    window.unbind('2')
    window.bind('c', clear)
    global running
    running = False
    data_s = {
        "name": "sharjeel",
        "guessed_in_seconds": ' % .3f' % (end - start),
        "guessed": image_for_garbage['name'],
        "type": "Yes"
    }

    data.append(data_s)


label = Label(window, fg="red", bg="white", font=("arial",24,"bold"))
label.pack()


def update_func(count):
    if running:
        if count >= 0:
            window.after(1000, update_func, count - 1)
            label.config(text='% .3f seconds' % count)

def log(data):
    ff = pandas.DataFrame(data)
    ff.to_csv("i.csv")


def no(event):
    end = time.time()
    timer.config(text='clicked  No % .3f s' % (end - start))
    window.unbind('2')
    window.unbind('1')
    window.bind('c', clear)
    global running
    running = False

    data_s = {
        "name": "sharjeel",
        "guessed_in_seconds": ' % .3f' % (end - start),
        "guessed": image_for_garbage['name'],
        "type": "No"
    }

    data.append(data_s)


def clear(event):
    label.config(text="0")
    timer.config(text="0")
    canvas.delete("all")
    window.bind('s', showimage)
    window.bind('1', yes)
    window.bind('2', no)
    global running
    running = True


def showimage(event):

    try:
        t = next(tt)
        path = t['path']
        global start
        start = time.time()
        global image_for_garbage
        canvas.delete("all")
        img = Image.open(path)
        img = img.resize((250, 250))
        new_canvas_image = ImageTk.PhotoImage(img)
        image_for_garbage['img'] = new_canvas_image
        image_for_garbage['name'] = path
        canvas.create_image(130, 130, image=new_canvas_image)
        update_func(5)
    except StopIteration:
        log(data)


window.bind('s', showimage)
window.bind('1', yes)
window.bind('2', no)
window.bind('c', clear)
# user registration


# creating charts/ reports
canvas.pack()
window.mainloop()
