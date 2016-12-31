import sys
from PIL import ImageTk,Image
from Tkinter import Tk,Frame,RAISED,LEFT
from container.piyush import * 
# from container.piyush1 import *
# from container.globals import init
# import Tkinter



if __name__ == "__main__":

    root = Tk()
    root.wm_title("BeSpoke Tailoring")
    root.resizable(width=False, height=False)
    pad=3
    # root._geom='200x200+0+0'

    wid = root.winfo_screenwidth() - pad
    heig = root.winfo_screenheight()-pad
    # Label(text="one").pack()
    root.geometry("{0}x{1}+0+0".format(wid , heig))
    # root.bind('<Escape>',r.toggle_geom)


    frame_o = Frame(root,width=-30+wid/2, height=heig, relief=RAISED)
    frame_o.pack(side=LEFT, padx=(2,0), pady=(0,5))
    frame_o.pack_propagate(False)
    # Label(frame_o,text='CUSTOMER DATA').pack()
    main = FullScreenApp(frame_o,root)


    frame_d = Frame(root,width=30+wid/2, height=heig, relief=RAISED)
    frame_d.pack_propagate(False)
    # Label(frame_d,text='MEASUREMENT FORM').pack()
    frame_d.pack(side=LEFT,padx=(0,2), pady=(0,5))
    main1 = FullScreenApp1(frame_d,root)

    img = ImageTk.PhotoImage(Image.open("images/bt.jpg"))
    panel = Label(root, image = img)
    panel.place(x=500,y=250)

    # Button(root, text='Search',height=1).place(x=680,y=70)
    Button(root, text='Save',height=2,width=5 ,command= lambda: setCustomerDetails(root)).place(x=450,y=650)
    Button(root, text='Cancel',height=2,width=5, command=root.destroy).place(x=520,y=650)

    
    
    # main = 

    root.mainloop()


