import tkinter as tk
from random import randrange

win = tk.Tk()
canvas = tk.Canvas(win, height = 450, width = 600, bg= "black" )
canvas.pack()

coins = 0 
coinsText = None
ostrov = 0

pic_zem = tk.PhotoImage(file = "ostrov0.png")
pic_voda = tk.PhotoImage(file = "ostrov3.png")
switchable = [tk.PhotoImage(file = "ostrov_kruh0.png"), tk.PhotoImage(file = "ostrov_kruh1.png")]
bridge = [tk.PhotoImage(file = "ostrov1.png"), tk.PhotoImage(file = "ostrov2.png")]

def clickButton(event):
    global ostrov
    if(ostrov == 0):
        canvas.itemconfig("switch", image=switchable[ostrov])
        ostrov = 1
    else:
        canvas.itemconfig("switch", image=switchable[ostrov])
        ostrov = 0

def clickOnWater(event):
    global coins
    id = canvas.find_withtag("current")[0]
    c = canvas.coords(id)

    if(ostrov == 1):
        canvas.create_image(c[0], c[1], anchor="nw", image=bridge[0], tags="horizontalBridge")
        buy(10)
        updateScene()
    else:
        canvas.create_image(c[0], c[1], anchor="nw", image=pic_zem, tags="land")
        buy(50)
        updateScene()

def clickOnBridge(event):
    id, tag = canvas.find_withtag("current")[0], canvas.gettags("current")[0]
    c = canvas.coords(id)
    makeBridge(tag, c)
    
def make_a_scene():
    global zem, coinsText
    m = randrange(4,7)
    n = randrange(3,10)
    for stlp in range(0,n+1):
        for riadok in range(0, m+1):
            if randrange(5) == 2:
                w = 50 * riadok
                h = 50 * stlp
                temp = canvas.create_image(w, h, anchor= "nw", image = pic_zem)

            else:
                w = 50 * riadok
                h = 50*stlp
                temp = canvas.create_image(w, h, anchor= "nw", image = pic_voda, tags="water")

    coinsText = canvas.create_text(475, 50, fill="white", font=("Helvetica", 32), text=coins)
    canvas.create_image(525, 25, anchor="nw", image = switchable[1], tags="switch")

def makeBridge(tag, c):
    if(tag == "verticalBridge"):
        canvas.create_image(c[0], c[1], anchor="nw", image=bridge[0], tags="horizontalBridge")
    else:
        canvas.create_image(c[0], c[1], anchor="nw", image=bridge[1], tags="verticalBridge")

def updateScene():
    global coins, coinsText
    canvas.itemconfig(coinsText, text=coins)

def buy(amount):
    global coins
    coins += amount

canvas.tag_bind("switch","<Button-1>", clickButton)
canvas.tag_bind("water","<Button-1>", clickOnWater)
canvas.tag_bind("verticalBridge","<Button-1>", clickOnBridge)
canvas.tag_bind("horizontalBridge","<Button-1>", clickOnBridge)

make_a_scene()
win.mainloop()

