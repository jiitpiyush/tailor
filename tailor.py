import sys
from PIL import ImageTk,Image

try:
    # Python2
    from Tkinter import Tk,Frame,RAISED,LEFT,Button,RIGHT
except ImportError:
    # Python3
    from tkinter import Tk,Frame,RAISED,LEFT,Button,RIGHT


from container.piyush import * 


if __name__ == "__main__":

    root = Tk()
    root.wm_title("BeSpoke Tailoring")
    root.resizable(width=False, height=False)
    pad=3

    wid = root.winfo_screenwidth() - pad
    heig = root.winfo_screenheight()-pad
    root.geometry("{0}x{1}+0+0".format(wid , heig))
    # root.bind('<Escape>',r.toggle_geom)



    frame_d = Frame(root,width=30+wid/2, height=heig, relief=RAISED)
    frame_d.pack_propagate(False)
    frame_d.pack(side=RIGHT,padx=(0,2), pady=(0,5))
    main1 = FullScreenApp1(frame_d,root)
    # main1.create(frame_d)

    frame_o = Frame(root,width=-30+wid/2, height=heig, relief=RAISED)
    frame_o.pack(side=LEFT, padx=(2,0), pady=(0,5))
    frame_o.pack_propagate(False)
    main = FullScreenApp(frame_o,root,main1)
    main.create(frame_o)


    # main1.create(frame_d)

    img = ImageTk.PhotoImage(Image.open("images/bt.jpg"))
    panel = Label(root, image = img)
    panel.place(x=500,y=250)

    
    
    # main = 

    root.mainloop()