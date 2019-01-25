import tkinter as tk

def drawWindow(x, color):
    root =  tk.Tk()

    w = tk.Label(root, text=x, fg=color)
    w.pack()

    root.mainloop()

def write_slogan(label, txt, color):
    label.config(text=txt, fg=color)

def oneButtonWindow(title, color, buttonText, windowWidth, windowHeight):
    root = tk.Tk()
    root.title(title)
    root.geometry(str(windowWidth)+"x"+str(windowHeight)+"+0+0")

#    frame = tk.Frame(root, width=windowWidth, height=windowHeight)
    frame  = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, 
                       text=buttonText, 
                       fg=color)
    button.pack(side=tk.LEFT)
    root.mainloop()

def TwoButtonWindow(msg1, clr1, msg2, clr2, title, buttonWid):
    root = tk.Tk()
    root.title(title)

    label= tk.Label(root)
    label.pack()

    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, 
                       text=msg1, 
                       fg=clr1,
                       command=write_slogan(label, msg1, clr1))
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                       text=msg2,
                       fg=clr2,
                       command=write_slogan(label, msg2, clr2))
    slogan.pack(side=tk.LEFT)

    root.mainloop()


