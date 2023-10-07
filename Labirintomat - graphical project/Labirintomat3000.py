from turtle import *
from tkinter import *
from random import *
from tkinter import font
import tkinter as tk
import sys

def draw_pixel(b, a):
    goto(a, b)
    pd()
    goto(a+1,b)
    goto(a+1, b-1)
    goto(a, b-1)
    goto(a,b)
    pu()


def draw_segment(c_x, c_y, segment):
    file = open(str(segment)+".txt", "r")
    pixel_list = file.readlines()
    goto(c_x, c_y)
    for i in range(10):
        for j in range(10):
            if(pixel_list[i][j] == "#"):
                n_x = c_x + i*2
                n_y = c_y + j*2
                draw_pixel(n_x, n_y)

    
def create_matrix(matrix, size_x, size_y):
    for i in range(size_x):
        for j in range(size_y):
            matrix[i][j] = randint(1, 16)


def random_dfs(tx, ty, t):
    l = []
    while(len(l) < 4):
        f = randint(0, 3)
        if f not in l:
            l.append(f)
    for i in l:
        nx = tx + sx[i]
        ny = ty + sy[i]
        if(nx >= 0 and nx < size_x and ny >= 0 and ny < size_y and matrix[nx][ny] == 0):
            matrix[nx][ny] = t
            random_dfs(nx, ny, t+1)


def contact (tx, ty):
    l = [0, 0, 0, 0] #gore, dole, lijevo, desno
    t = matrix[tx][ty]
    if(tx == 0 or matrix[tx-1][ty] not in (t-1, t+1)): l[0] = 1
    if(tx == size_x-1 or matrix[tx+1][ty] not in (t-1, t+1)): l[1] = 1
    if(ty == 0 or matrix[tx][ty-1] not in (t-1, t+1)): l[2] = 1
    if(ty == size_y-1 or matrix[tx][ty+1] not in (t-1, t+1)): l[3]= 1

    if((tx, ty) == (0, 0)): l[0] = 0
    elif((tx, ty) == (size_x-1, size_y-1)): l[1] = 0
    return tuple(l)


def create_labirint():
    for i in range(size_x):
        for j in range(size_y):
            d = contact(i, j)
            if(d == (0, 0, 0, 0)): labirint[i][j] = 16
            elif(d == (0, 0, 0, 1)): labirint[i][j] = 13
            elif(d == (0, 0, 1, 0)): labirint[i][j] = 11
            elif(d == (0, 0, 1, 1)): labirint[i][j] = 4
            elif(d == (0, 1, 0, 0)): labirint[i][j] = 12
            elif(d == (0, 1, 0, 1)): labirint[i][j] = 5
            elif(d == (0, 1, 1, 0)): labirint[i][j] = 3
            elif(d == (0, 1, 1, 1)): labirint[i][j] = 6
            
            elif(d == (1, 0, 0, 0)): labirint[i][j] = 14
            elif(d == (1, 0, 0, 1)): labirint[i][j] = 9
            elif(d == (1, 0, 1, 0)): labirint[i][j] = 10
            elif(d == (1, 0, 1, 1)): labirint[i][j] = 2
            elif(d == (1, 1, 0, 0)): labirint[i][j] = 8
            elif(d == (1, 1, 0, 1)): labirint[i][j] = 1
            elif(d == (1, 1, 1, 0)): labirint[i][j] = 7
            elif(d == (1, 1, 1, 1)): labirint[i][j] = 15


def okvir():
    goto(-size_y//2*20, size_x//2*20+20)
    pd()
    fd(2)
    pu()
    goto(-size_y//2*20+18, size_x//2*20+20)
    pd()
    fd(20*size_y+2-20)
    pu()
    
    goto(-size_y//2*20, size_x//2*20+20-1)
    pd()
    fd(2)
    pu()
    goto(-size_y//2*20+18, size_x//2*20+20-1)
    pd()
    fd(20*size_y+2-20)
    pu()


    goto(-size_y//2*20, -size_x//2*20+20-3)
    pd()
    fd(20*size_y+2-20)
    pu()
    goto(size_y//2*20-2, -size_x//2*20+20-3)
    pd()
    fd(2)
    pu()
    
    goto(-size_y//2*20, -size_x//2*20+20-2)
    pd()
    fd(20*size_y+2-20)
    pu()
    goto(size_y//2*20-2, -size_x//2*20+20-2)
    pd()
    fd(2)
    pu()

    
    pu()
    rt(90)
    goto(-size_y//2*20-1, size_x//2*20+20)
    pd()
    fd(20*size_x+4)
    pu()
    goto(-size_y//2*20-2, size_x//2*20+20)
    pd()
    fd(20*size_x+4)


    pu()
    goto(size_y//2*20+1, size_x//2*20+20)
    pd()
    fd(20*size_x+4)
    pu()
    goto(size_y//2*20, size_x//2*20+20)
    pd()
    fd(20*size_x+4)
    pu()

def gumbSubmitAkcija1(event):
    a = entryImee.get()
    if a != "":
        getscreen().getcanvas().postscript(file=str(a)+".ps")
        entryImee.config(bg = "white")
        entryImee.delete(0, END)
    else:
        entryImee.config(bg = "#ffafaf")

    
def gumbSubmitAkcija2(event):
    sett.withdraw()
    bye()
    start_screen()

def gumbSubmitAkcija3(event):
    credit.withdraw()
    start_screen()

def gumbSubmitAkcija4(event):
    prozor.withdraw()
    start_screen()
    
def postavke():
    global sett
    sett = Toplevel()
    sett.geometry("200x130+100+100")

    background_image=tk.PhotoImage(file ="b2.png")
    background_label = tk.Label(sett, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    labelImee = Label(sett, text = 'Save as:', fg = "black", bg = "white")

    global entryImee
    entryImee = Entry(sett)
    labelImee.pack()
    entryImee.pack()
    
    gumbSubmit = Button(sett, text = 'Save')
    gumbSubmit.bind('<Button>', gumbSubmitAkcija1)
    gumbSubmit.pack()

    gumbSubmit2 = Button(sett, text = 'Return to Start')
    gumbSubmit2.bind('<Button>', gumbSubmitAkcija2)
    gumbSubmit2.pack()


    prozor.mainloop()
    return
    
def build_grid():
    TurtleScreen._RUNNING = True
    d = open("eventi.txt", "r")
    global size_y
    size_y = int(d.readline().replace("\n",""))
    global size_x
    size_x = int(d.readline().replace("\n",""))
    d.close()
    
    global matrix
    matrix = [[0 for i in range(size_y)] for j in range(size_x)]
    global labirint
    labirint = [[0 for i in range(size_y)] for j in range(size_x)]
    matrix[size_x-1][size_y-1] = 1
    random_dfs(size_x-1, size_y-1, 2)
    create_labirint()

    screensize()
    setup(width = 1.0, height = 1.0)
    screensize(size_y*20+40, size_x*20+40)
    ht()
    pu()
    tracer(0)
    title("Labirintomat3000")
    for i in range (size_x):
        for j in range(size_y):
            draw_segment((size_x//2-i)*20, (j-size_y//2)*20, labirint[i][j])
    okvir()
    tracer(1)
    postavke()
    mainloop()
    return
    
def creditss():
    global credit
    credit = Toplevel()
    credit.geometry('600x640+600+250')
    credit.resizable(False, False)
    credit.title('Labirintomat3000 Credits')
    background_image1= PhotoImage(file ="kredits.png")
    background_label1 = Label(credit, image=background_image1)
    background_label1.pack()
    
    gumbSubmitt = Button(credit, text = 'Return', font="OCRAStd")
    gumbSubmitt.bind('<Button>', gumbSubmitAkcija3)
    gumbSubmitt.pack()
    
    credit.mainloop()

def gumbSubmitAkcija(event):
        d=open("eventi.txt", "w")

        a, b = entryIme.get(), entryPrezime.get()
        if(a == "" or b == ""):
            if(a == ""): entryIme.config(bg = "#ffafaf")
            elif(not a =="" and (9 < int(a) < 81)): entryIme.config(bg = "white")
            if(b == ""): entryPrezime.config(bg = "#ffafaf")
            elif((9 < int(b) < 46) and not b == ""): entryPrezime.config(bg = "white")
        else:
            if(9 < int(a) < 81 and 9 < int(b) < 46):
                entryIme.config(bg = "white")
                entryPrezime.config(bg = "white")
                if(int(a)%2 == 1): a = str(int(a)+1)
                if(int(b)%2 == 1): b = str(int(b)+1)
                d.write(a+"\n" +b)
                d.close()
                entryIme.delete(0, END)
                entryPrezime.delete(0, END)
                prozor.withdraw()
                build_grid()
            else:
                if(not(9 < int(a) < 81)): entryIme.config(bg = "#ffafaf"); entryIme.delete(0, END)
                if(not(9 < int(b) < 46)): entryPrezime.config(bg = "#ffafaf"); entryPrezime.delete(0, END)
                if(9 < int(a) < 81): entryIme.config(bg = "white")
                if(9 < int(b) < 46): entryPrezime.config(bg = "white")

def upit():
    global prozor
    prozor = Toplevel()
    prozor.geometry("600x200+600+400")

    background_image=tk.PhotoImage(file ="b1.png")
    background_label = tk.Label(prozor, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)


    
    teks = Label(prozor, text = "Enter the required length and width of the labirinth", bg = "white")
    labelIme = Label(prozor, text = 'Width (10 - 80):', fg = "black", bg = "white")
    labelPrezime = Label(prozor, text = 'Height (10 - 45)', bg = "white")

    global entryIme, entryPrezime
    entryIme = Entry(prozor)
    entryPrezime = Entry(prozor)
    teks.pack()
    labelIme.pack()
    entryIme.pack()
    labelPrezime.pack()
    entryPrezime.pack()
    
    gumbSubmit = Button(prozor, text = 'Generate')
    gumbSubmit.bind('<Button>', gumbSubmitAkcija)
    gumbSubmit.pack()

    gumbSubmit1 = Button(prozor, text = 'Return to Start')
    gumbSubmit1.bind('<Button>', gumbSubmitAkcija4)
    gumbSubmit1.pack()
    
    prozor.mainloop()
    
    
    return

def gqa(event):
    start.withdraw()
    exit()
def gsa(event):
    start.withdraw()
    upit()
    return
def gca(event):
    start.withdraw()
    creditss()


def start_screen():
    start.update()
    start.deiconify()
    start.geometry('1300x700+300+200')
    start.resizable(False, False)
    start.config(background = "#ECFAFD")
    start.title('Labirintomat3000')
    background_image=tk.PhotoImage(file ="title.png")
    background_label = tk.Label(start, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    gs = Button(start, text = "Start")
    t1 = font.Font(family='OCRAStd', size=20, weight = "bold")
    gs.config(fg="white", bg = "black", font = t1, width = 10, pady = 10)
    gs.place(x=520, y= 220)
    '''
    gt = Button(start, text = "Settings")
    t2 = font.Font(family='OCRAStd', size=20, weight='bold')
    gt.config(fg="white", bg = "black", font = t2, width = 10, pady = 10)
    gt.place(x=520, y= 320)
    '''
    gc = Button(start, text = "Credits")
    t3 = font.Font(family='OCRAStd', size=20, weight='bold')
    gc.config(fg="white", bg = "black", font = t3, width = 10, pady = 10)
    gc.place(x=520, y= 320)

    gq = Button(start, text = "Quit")
    t4 = font.Font(family='OCRAStd', size=20, weight='bold')
    gq.config(fg="white", bg = "black", font = t3, width = 10, pady = 10)
    gq.place(x=520, y= 420)

    gs.bind('<Button>', gsa)
    #gt.bind('<Button>', gta)
    gc.bind('<Button>', gca)
    gq.bind('<Button>', gqa)
    start.mainloop()
    
start = Tk()
#credit = Tk()
def main():
    sys.setrecursionlimit(2600)
    
    global sx
    sx = [0, 1, 0, -1]
    global sy
    sy = [1, 0, -1, 0]
    
    global size_y
    global size_x
    '''
    size_y = int(input("x = ")) #min 4, max 45
    size_x = int(input("y = "))
    '''
    
    start_screen()

    
    
    #build_grid()
    #mainloop()
    
    return

main()
