from tkinter import *
root = Tk()
root.geometry("644x900")
root.title("My calcy")
root.configure(background = "black")

def click(event):
    global scvalue 
    text= event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)   
        scvalue.update()     


    elif text == "CLEAR":
        scvalue.set("")
        screen.update()
        
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


#root.wm_iconbitmap("isofile")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar= scvalue,font = "lucida 40 bold",fg="black",bg="white")
screen.pack(fill = X,pady = 10,padx = 10)

f = Frame(root,bg = "black")
b = Button(f,text="9",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="8",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="7",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="6",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)


f.pack()




f = Frame(root,bg = "black")
b = Button(f,text="5",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="4",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="3",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="2",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root,bg = "black")
b = Button(f,text="1",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="0",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text=".",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="=",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)


f.pack()

f = Frame(root,bg = "black")
b = Button(f,text="+",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="-",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="/",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="*",padx=15,pady=15,bg="black",fg="white",font="lucida 35 bold")
b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)


f.pack()


f = Frame(root,bg = "black")
#b = Button(f,text="",padx=15,pady=15,bg ="BLACK",font="lucida 35 bold")
#b.pack(side = LEFT,padx=10,pady=10)
#b.bind("<Button-1>",click)
#b = Button(f,text="(",padx=15,pady=15,font="lucida 35 bold")
#b.pack(side = LEFT,padx=10,pady=10)
#b.bind("<Button-1>",click)
#b = Button(f,text=")",padx=15,pady=15,font="lucida 35 bold")
#b.pack(side = LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)
b = Button(f,text="CLEAR",padx=120,pady=10,bg="black",fg="white",font="lucida 35 bold")
b.pack(padx=10,pady=10,fill=X)
b.bind("<Button-1>",click)


f.pack()







root.mainloop()