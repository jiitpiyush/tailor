
try:
    # Python2
    from Tkinter import Tk,Frame,RAISED,LEFT,Button,RIGHT
except ImportError:
    # Python3
    from tkinter import Tk,Frame,RAISED,LEFT,Button,RIGHT

import sys
from PIL import ImageTk,Image
import hashlib

from container.piyush import * 


def getMd5(data):
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()


def getKey(root):
    # NG4HW-VH26C-733KW-K6F98-J8CK4
    em = email.get()
    pas = passw.get()
    em_hash = getMd5(em)
    pas_hash = getMd5(pas)
    notify = {}

    if em == regEmail and pas == regKey:
        filek = open(os.path.join(tailordir,".activation.key"),"w+")
        filek.write(em_hash+pas_hash)
        filek.close()

        notify['req'] = 'success'
        notify['msg'] = "Successfully Registered"
        NotifyMsg(notify)
        root.destroy()    
    else:
        notify['req'] = 'error'
        notify['msg'] = 'Wrong combination of Mobile and Key'
        NotifyMsg(notify)
    
    return

if __name__ == "__main__":

    root = Tk()
    root.wm_title("BeSpoke Tailoring")
    root.resizable(width=False, height=False)
    pad=3
    global regEmail,regKey
    global email,passw

    regEmail = "9935106200"
    regKey = "NG4HW-VH26C-733KW-K6F98-J8CK4"
    activation = False
    wid = 350
    heig = 250
    sizr = 40
    root.geometry("{0}x{1}+0+0".format(wid , heig))
    
    
    if not os.path.isfile(os.path.join(tailordir,".activation.key")):
        
        l9=Label(root,text="MOBILE:")
        l9.place(x=20,y=sizr+20)
        email= Entry(root,width=30)
        email.place(x=80,y=sizr+20)
        
        l10=Label(root,text="KEY:")
        l10.place(x=20,y=sizr+50)
        passw= Entry(root,width=30)
        passw.place(x=80,y=sizr+50)

        Button(root, text='Submit',height=1, command=lambda:getKey(root)).place(x=250,y=sizr+80)

    elif os.path.isfile(os.path.join(tailordir,".activation.key")):
        em = getMd5(regEmail)
        key = getMd5(regKey)

        data = em+key

        filek = open(os.path.join(tailordir,".activation.key"),"r")
        if filek:
            filedata = filek.readline()
            if filedata == data:
                activation = True
            else:
                notify = {}
                notify['req'] = 'error'
                notify['msg'] = 'Key Modified. Please Register again'
                NotifyMsg(notify)
                
                l9=Label(root,text="MOBILE:")
                l9.place(x=20,y=sizr+20)
                email= Entry(root,width=30)
                email.place(x=80,y=sizr+20)
                
                l10=Label(root,text="KEY:")
                l10.place(x=20,y=sizr+50)
                passw= Entry(root,width=30)
                passw.place(x=80,y=sizr+50)

                Button(root, text='Submit',height=1, command=lambda:getKey(root)).place(x=250,y=sizr+80)


        if activation:
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

            # img = ImageTk.PhotoImage(Image.open("images/bt.jpg"))
            # panel = Label(root, image = img)
            # panel.place(x=500,y=250)

            
            
            # main = 

    root.mainloop()