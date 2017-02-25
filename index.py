try:
    # Python2
    from Tkinter import Tk,Frame,RAISED,LEFT,Button
except ImportError:
    # Python3
    from tkinter import Tk,Frame,RAISED,LEFT,Button

from subprocess import call
from tailor import start



if __name__ == "__main__":

    root = Tk()
    root.wm_title("BeSpoke Tailoring")
    # root.resizable(width=False, height=False)
    pad=3

    wid = 220
    heig = 250
    # Label(text="one").pack()
    root.geometry("{0}x{1}+0+0".format(wid , heig))

    Button(root, text='Open',height=2,width=6 ,command= lambda: start() ).place(x=65,y=84)
    Button(root, text='Cancel',height=2,width=6, command=root.destroy).place(x=65,y=134)


    root.mainloop()