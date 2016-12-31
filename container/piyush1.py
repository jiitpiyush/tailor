from Tkinter import Tk,Label,Entry,Text,Checkbutton,IntVar
import os

class FullScreenApp1(object):
	def __init__(self, mainwin, root, **kwargs):
		global Length1, Shoulder1, Sleeve1, Chest1,Waist1,Hip1,Neck1,Half1,Cross_back1,Cross_front1,Bicep1,Arm1
		global Arm1,style1,Length2, Inseam2, Crotch2, Waist2, Hip2, Thigh2, Knee2, Bottom2, F_Low2, Loopsinput,Sizeinput
		global Length3, Shoulder3, Sleeve3, Chest3, Waist3,Hip3, Cross_Front3, Cross_Back3, Neck3,Cuff3, Arm_Round3, Ready_Frontinput
		global jacket_lapel_peak,jacket_lapel_natch,jacket_lapel_shawl,jacket_vent_no,jacket_vent_side,jacket_vent_center
		global jacket_pocket_straight,jacket_pocket_slant,jacket_pocket_patch,jacket_pocket_ticket,jacket_fit_regular,jacket_fit_slim,jacket_sleeveplacket_vent,jacket_sleeveplacket_functional
		global trouser_belt_cut,trouser_belt_long, trouser_belt_hook, trouser_belt_button, trouser_belt_square, trouser_belt_round, trouser_belt_vshape,trouser_pleat_single
		global trouser_pleat_double, trouser_pleat_flat, trouser_pocket_cross, trouser_pocket_straight, trouser_pocket_l, trouser_pocket_mobile, trouser_pocket_coin,trouser_backpocket_1
		global trouser_backpocket_2, trouser_backpocket_no, trouser_backpocket_loop, trouser_backpocket_kaaj, trouser_backpocket_flap, trouser_bottom_plain, trouser_bottom_slant, trouser_bottom_turnup
		global trouser_bottom_lining,trouser_bottom_knee, trouser_bottom_half, trouser_bottom_full, trouser_fit_regular, trouser_fit_slim, trouser_fit_tapered
		global shirt_bottom_cut, shirt_bottom_long, shirt_bottom_hook, shirt_pocket_1, shirt_pocket_2, shirt_pocket_no, shirt_pocket_v, shirt_pocket_chisel, shirt_pocket_withflap,shirt_frontpocket_plain
		global shirt_frontpocket_box, shirt_frontpocket_plainfuse, shirt_frontpocket_concealed, shirt_back_plain, shirt_back_sidepleat, shirt_back_bocpleat, shirt_back_dart


		sizy = -70
		sizx = 00

		# for widget in mainwin.winfo_children():
		# 	widget.pack_forget()
		# 	widget.grid_forget()
		# 	widget.place_forget()
		
		# img = ImageTk.PhotoImage(Image.open("bt.jpg"))
		# panel = Label(mainwin, image = img)
		# panel.place(x=sizx+15,y=5)

		jacket_lapel_peak = IntVar()
		jacket_lapel_natch = IntVar()
		jacket_lapel_shawl = IntVar()
		jacket_vent_no = IntVar()
		jacket_vent_side = IntVar()
		jacket_vent_center = IntVar()
		jacket_pocket_straight = IntVar()
		jacket_pocket_slant = IntVar()
		jacket_pocket_patch = IntVar()
		jacket_pocket_ticket = IntVar()
		jacket_fit_regular = IntVar()
		jacket_fit_slim = IntVar()
		jacket_sleeveplacket_vent = IntVar()
		jacket_sleeveplacket_functional = IntVar()

		trouser_belt_cut=IntVar()
		trouser_belt_long=IntVar()
		trouser_belt_hook=IntVar()
		trouser_belt_button=IntVar()
		trouser_belt_square=IntVar()
		trouser_belt_round=IntVar()
		trouser_belt_vshape=IntVar()
		trouser_pleat_single = IntVar()
		trouser_pleat_double=IntVar()
		trouser_pleat_flat=IntVar()
		trouser_pocket_cross=IntVar()
		trouser_pocket_straight=IntVar()
		trouser_pocket_l=IntVar()
		trouser_pocket_mobile=IntVar()
		trouser_pocket_coin=IntVar()
		trouser_backpocket_1 = IntVar()
		trouser_backpocket_2=IntVar()
		trouser_backpocket_no=IntVar()
		trouser_backpocket_loop=IntVar()
		trouser_backpocket_kaaj=IntVar()
		trouser_backpocket_flap=IntVar()
		trouser_bottom_plain=IntVar()
		trouser_bottom_slant=IntVar()
		trouser_bottom_turnup = IntVar()
		trouser_bottom_lining = IntVar()
		trouser_bottom_knee=IntVar()
		trouser_bottom_half=IntVar()
		trouser_bottom_full=IntVar()
		trouser_fit_regular=IntVar()
		trouser_fit_slim=IntVar()
		trouser_fit_tapered = IntVar()
		shirt_bottom_cut=IntVar()
		shirt_bottom_long=IntVar()
		shirt_bottom_hook=IntVar()
		shirt_pocket_1=IntVar()
		shirt_pocket_2=IntVar()
		shirt_pocket_no=IntVar()
		shirt_pocket_v=IntVar()
		shirt_pocket_chisel=IntVar()
		shirt_pocket_withflap=IntVar()
		shirt_frontpocket_plain = IntVar()
		shirt_frontpocket_box=IntVar()
		shirt_frontpocket_plainfuse=IntVar()
		shirt_frontpocket_concealed=IntVar()
		shirt_back_plain=IntVar()
		shirt_back_sidepleat=IntVar()
		shirt_back_bocpleat=IntVar()
		shirt_back_dart = IntVar()


		



		#############################################JACKET#################################################


		l1=Label(mainwin,text="Jacket Measurments",fg="red")
		l1.place(x=sizx+10,y=sizy+75)


		# ordernojacaket=Label(mainwin,text="ORDER NO.")
		# ordernojacaket.place(x=sizx+500,y=sizy+75)
		# orderno1= Entry(mainwin,width=8)
		# orderno1.place(x=sizx+580,y=sizy+75)


		# name=Label(mainwin,text="Costumer Name")
		# name.place(x=sizx+10,y=sizy+40)
		# name1= Entry(mainwin,width=40)
		# name1.place(x=sizx+120,y=sizy+40)


		# Number=Label(mainwin,text="Phone no.")
		# Number.place(x=sizx+400,y=sizy+40)
		# Number1= Entry(mainwin,width=22)
		# Number1.place(x=sizx+490,y=sizy+40)

		Length=Label(mainwin,text="Length")
		Length.place(x=sizx+10,y=sizy+100)
		Length1= Entry(mainwin,width=8)
		Length1.place(x=sizx+10,y=sizy+140)

		Shoulder=Label(mainwin,text="Shoulder")
		Shoulder.place(x=sizx+70,y=sizy+100)
		Shoulder1= Entry(mainwin,width=8)
		Shoulder1.place(x=sizx+70,y=sizy+140)

		Sleeve=Label(mainwin,text="Sleeve")
		Sleeve.place(x=sizx+130,y=sizy+100)
		Length=Label(mainwin,text="Length")
		Length.place(x=sizx+130,y=sizy+115)
		Sleeve1= Entry(mainwin,width=8)
		Sleeve1.place(x=sizx+130,y=sizy+140)

		Chest=Label(mainwin,text="Chest")
		Chest.place(x=sizx+190,y=sizy+100)
		Chest1= Entry(mainwin,width=8)
		Chest1.place(x=sizx+190,y=sizy+140)

		Waist=Label(mainwin,text="Waist")
		Waist.place(x=sizx+250,y=sizy+100)
		Waist1= Entry(mainwin,width=8)
		Waist1.place(x=sizx+250,y=sizy+140)

		Hip=Label(mainwin,text="Hip")
		Hip.place(x=sizx+310,y=sizy+100)
		Hip1= Entry(mainwin,width=8)
		Hip1.place(x=sizx+310,y=sizy+140)

		Neck=Label(mainwin,text="Neck")
		Neck.place(x=sizx+370,y=sizy+100)
		Neck1= Entry(mainwin,width=8)
		Neck1.place(x=sizx+370,y=sizy+140)

		Half=Label(mainwin,text="Half")
		Half.place(x=sizx+430,y=sizy+100)
		Back=Label(mainwin,text="Back")
		Back.place(x=sizx+430,y=sizy+115)
		Half1= Entry(mainwin,width=8)
		Half1.place(x=sizx+430,y=sizy+140)

		Cross_back=Label(mainwin,text="Cross Bk.")
		Cross_back.place(x=sizx+490,y=sizy+100)
		Cross_back1= Entry(mainwin,width=8)
		Cross_back1.place(x=sizx+490,y=sizy+140)

		Cross_front=Label(mainwin,text="Cross Fr.")
		Cross_front.place(x=sizx+550,y=sizy+100)
		Cross_front1= Entry(mainwin,width=8)
		Cross_front1.place(x=sizx+550,y=sizy+140)

		Bicep=Label(mainwin,text="Bicep")
		Bicep.place(x=sizx+610,y=sizy+100)
		Bicep1= Entry(mainwin,width=8)
		Bicep1.place(x=sizx+610,y=sizy+140)

		Arm_hole=Label(mainwin,text="Arm")
		Arm_hole.place(x=sizx+670,y=sizy+85)

		Arm_hole1=Label(mainwin,text="hole")
		Arm_hole1.place(x=sizx+670,y=sizy+100)

		Round=Label(mainwin,text="Round")
		Round.place(x=sizx+670,y=sizy+115)
		Arm1= Entry(mainwin,width=8)
		Arm1.place(x=sizx+670,y=sizy+140)

		#############################################       JACKET      #################################################

		l2=Label(mainwin,text="Style Details",fg="red")
		l2.place(x=sizx+10,y=sizy+170)

		style=Label(mainwin,text="Style")
		style.place(x=sizx+10,y=sizy+190)
		style1 = Text(mainwin,height=5,width=20)
		style1.place(x=sizx+10,y=sizy+215)

		Lapel=Label(mainwin,text="Lapel")
		Lapel.place(x=sizx+195,y=sizy+190)
		cj1=Checkbutton(mainwin,text="Peak",variable=jacket_lapel_peak)
		cj1.place(x=sizx+190,y=sizy+220)
		cj2=Checkbutton(mainwin,text="Natch",variable=jacket_lapel_natch)
		cj2.place(x=sizx+190,y=sizy+240)
		cj3=Checkbutton(mainwin,text="Shawl",variable=jacket_lapel_shawl)
		cj3.place(x=sizx+190,y=sizy+260)

		Vent=Label(mainwin,text="Vent")
		Vent.place(x=sizx+260,y=sizy+190)
		cj4=Checkbutton(mainwin,text="No Vent",variable=jacket_vent_no)
		cj4.place(x=sizx+260,y=sizy+220)
		cj5=Checkbutton(mainwin,text="Side Vent",variable=jacket_vent_side)
		cj5.place(x=sizx+260,y=sizy+240)
		cj6=Checkbutton(mainwin,text="Center Vent",variable=jacket_vent_center)
		cj6.place(x=sizx+260,y=sizy+260)

		Pocket=Label(mainwin,text="Pocket")
		Pocket.place(x=sizx+360,y=sizy+190)
		cj7=Checkbutton(mainwin,text="Straight",variable=jacket_pocket_straight)
		cj7.place(x=sizx+360,y=sizy+220)
		cj8=Checkbutton(mainwin,text="Slant",variable=jacket_pocket_slant)
		cj8.place(x=sizx+360,y=sizy+240)
		cj9=Checkbutton(mainwin,text="Patch",variable=jacket_pocket_patch)
		cj9.place(x=sizx+360,y=sizy+260)
		cj10=Checkbutton(mainwin,text="Ticket",variable=jacket_pocket_ticket)
		cj10.place(x=sizx+360,y=sizy+280)


		Fit=Label(mainwin,text="Fit")
		Fit.place(x=sizx+440,y=sizy+190)
		cj11=Checkbutton(mainwin,text="Regular Fit",variable=jacket_fit_regular)
		cj11.place(x=sizx+440,y=sizy+220)
		cj12=Checkbutton(mainwin,text="Slim Fit",variable=jacket_fit_slim)
		cj12.place(x=sizx+440,y=sizy+240)

		Sleeve_placket=Label(mainwin,text="Sleeve_placket")
		Sleeve_placket.place(x=sizx+530,y=sizy+190)
		cj13=Checkbutton(mainwin,text="Vent",variable=jacket_sleeveplacket_vent)
		cj13.place(x=sizx+530,y=sizy+220)
		cj14=Checkbutton(mainwin,text="Functional",variable=jacket_sleeveplacket_functional)
		cj14.place(x=sizx+530,y=sizy+240)


		#################################        TROUSER  ####################################

		l3=Label(mainwin,text="Trouser Measurments",fg="red")
		l3.place(x=sizx+10,y=sizy+305)

		# ordernotrouser=Label(mainwin,text="ORDER NO.")
		# ordernotrouser.place(x=sizx+550,y=sizy+300)
		# orderno2= Entry(mainwin,width=8)
		# orderno2.place(x=sizx+620,y=sizy+300)

		Lengthtrouser=Label(mainwin,text="Length")
		Lengthtrouser.place(x=sizx+10,y=sizy+330)
		Length2= Entry(mainwin,width=8)
		Length2.place(x=sizx+10,y=sizy+360)

		Inseam=Label(mainwin,text="Inseam")
		Inseam.place(x=sizx+70,y=sizy+330)
		Inseam2= Entry(mainwin,width=8)
		Inseam2.place(x=sizx+70,y=sizy+360)

		Crotch=Label(mainwin,text="Crotch")
		Crotch.place(x=sizx+130,y=sizy+330)
		Crotch2= Entry(mainwin,width=8)
		Crotch2.place(x=sizx+130,y=sizy+360)

		Waisttrouser=Label(mainwin,text="Waist")
		Waisttrouser.place(x=sizx+190,y=sizy+330)
		Waist2= Entry(mainwin,width=8)
		Waist2.place(x=sizx+190,y=sizy+360)

		Hiptrouser=Label(mainwin,text="Hip")
		Hiptrouser.place(x=sizx+250,y=sizy+330)
		Hip2= Entry(mainwin,width=8)
		Hip2.place(x=sizx+250,y=sizy+360)

		Thigh=Label(mainwin,text="Thigh")
		Thigh.place(x=sizx+310,y=sizy+330)
		Thigh2= Entry(mainwin,width=8)
		Thigh2.place(x=sizx+310,y=sizy+360)

		Knee=Label(mainwin,text="Knee")
		Knee.place(x=sizx+370,y=sizy+330)
		Knee2= Entry(mainwin,width=8)
		Knee2.place(x=sizx+370,y=sizy+360)

		Bottom=Label(mainwin,text="Bottom")
		Bottom.place(x=sizx+430,y=sizy+330)
		Bottom2= Entry(mainwin,width=8)
		Bottom2.place(x=sizx+430,y=sizy+360)

		F_Low=Label(mainwin,text="F.Low")
		F_Low.place(x=sizx+490,y=sizy+330)
		F_Low2= Entry(mainwin,width=8)
		F_Low2.place(x=sizx+490,y=sizy+360)


		#################################        TROUSER  ####################################

		l4=Label(mainwin,text="Style Details",fg="red")
		l4.place(x=sizx+10,y=sizy+390)

		Belt=Label(mainwin,text="Belt")
		Belt.place(x=sizx+10,y=sizy+415)
		ct1=Checkbutton(mainwin,text="Cut",variable=trouser_belt_cut)
		ct1.place(x=sizx+10,y=sizy+440)
		ct2=Checkbutton(mainwin,text="Long",variable=trouser_belt_long)
		ct2.place(x=sizx+10,y=sizy+460)
		ct3=Checkbutton(mainwin,text="Hook",variable=trouser_belt_hook)
		ct3.place(x=sizx+10,y=sizy+480)
		ct4=Checkbutton(mainwin,text="Button",variable=trouser_belt_button)
		ct4.place(x=sizx+10,y=sizy+500)
		ct5=Checkbutton(mainwin,text="Square",variable=trouser_belt_square)
		ct5.place(x=sizx+10,y=sizy+520)
		ct6=Checkbutton(mainwin,text="Round",variable=trouser_belt_round)
		ct6.place(x=sizx+10,y=sizy+540)
		ct7=Checkbutton(mainwin,text="V-Shape",variable=trouser_belt_vshape)
		ct7.place(x=sizx+10,y=sizy+560)

		Pleat=Label(mainwin,text="Pleat")
		Pleat.place(x=sizx+90,y=sizy+415)
		ct8=Checkbutton(mainwin,text="Single",variable=trouser_pleat_single)
		ct8.place(x=sizx+90,y=sizy+440)
		ct9=Checkbutton(mainwin,text="Double",variable=trouser_pleat_double)
		ct9.place(x=sizx+90,y=sizy+460)
		ct10=Checkbutton(mainwin,text="Flat",variable=trouser_pleat_flat)
		ct10.place(x=sizx+90,y=sizy+480)

		Pockettrouser=Label(mainwin,text="Pocket")
		Pockettrouser.place(x=sizx+170,y=sizy+415)
		ct11=Checkbutton(mainwin,text="Cross",variable=trouser_pocket_cross)
		ct11.place(x=sizx+170,y=sizy+440)
		ct12=Checkbutton(mainwin,text="Straight",variable=trouser_pocket_straight)
		ct12.place(x=sizx+170,y=sizy+460)
		ct13=Checkbutton(mainwin,text="L Pocket",variable=trouser_pocket_l)
		ct13.place(x=sizx+170,y=sizy+480)
		ct14=Checkbutton(mainwin,text="Mobile",variable=trouser_pocket_mobile)
		ct14.place(x=sizx+170,y=sizy+500)
		ct15=Checkbutton(mainwin,text="Coin",variable=trouser_pocket_coin)
		ct15.place(x=sizx+170,y=sizy+520)

		Back_Pocket=Label(mainwin,text="Back Pocket")
		Back_Pocket.place(x=sizx+250,y=sizy+415)
		ct16=Checkbutton(mainwin,text="1 Pocket",variable=trouser_backpocket_1)
		ct16.place(x=sizx+250,y=sizy+440)
		ct17=Checkbutton(mainwin,text="2 Pocket",variable=trouser_backpocket_2)
		ct17.place(x=sizx+250,y=sizy+460)
		ct18=Checkbutton(mainwin,text="No",variable=trouser_backpocket_no)
		ct18.place(x=sizx+250,y=sizy+480)
		ct19=Checkbutton(mainwin,text="Loop Bts",variable=trouser_backpocket_loop)
		ct19.place(x=sizx+250,y=sizy+500)
		ct20=Checkbutton(mainwin,text="Kaaj Bts",variable=trouser_backpocket_kaaj)
		ct20.place(x=sizx+250,y=sizy+520)
		ct21=Checkbutton(mainwin,text="Flap",variable=trouser_backpocket_flap)
		ct21.place(x=sizx+250,y=sizy+540)

		Bottom=Label(mainwin,text="Bottom")
		Bottom.place(x=sizx+350,y=sizy+415)
		ct22=Checkbutton(mainwin,text="Plain",variable=trouser_bottom_plain)
		ct22.place(x=sizx+350,y=sizy+440)
		ct23=Checkbutton(mainwin,text="Slant",variable=trouser_bottom_slant)
		ct23.place(x=sizx+350,y=sizy+460)
		ct24=Checkbutton(mainwin,text="Turnup",variable=trouser_bottom_turnup)
		ct24.place(x=sizx+350,y=sizy+480)
		
		Lining=Label(mainwin,text="Lining")
		Lining.place(x=sizx+350,y=sizy+510)
		ct25=Checkbutton(mainwin,text="Knee",variable=trouser_bottom_knee)
		ct25.place(x=sizx+350,y=sizy+530)
		ct26=Checkbutton(mainwin,text="Half F/B",variable=trouser_bottom_half)
		ct26.place(x=sizx+350,y=sizy+550)
		ct27=Checkbutton(mainwin,text="Full F/B",variable=trouser_bottom_full)
		ct27.place(x=sizx+350,y=sizy+570)

		Loops=Label(mainwin,text="Loops")
		Loops.place(x=sizx+440,y=sizy+415)
		Loopsinput = Text(mainwin,height=2,width=5)
		Loopsinput.place(x=sizx+440,y=sizy+440)
		
		Size=Label(mainwin,text="Size")
		Size.place(x=sizx+440,y=sizy+480)
		Sizeinput = Text(mainwin,height=2,width=5)
		Sizeinput.place(x=sizx+440,y=sizy+510)

		Fit=Label(mainwin,text="Fit")
		Fit.place(x=sizx+510,y=sizy+415)
		ct28=Checkbutton(mainwin,text="Regular",variable=trouser_fit_regular)
		ct28.place(x=sizx+510,y=sizy+440)
		ct29=Checkbutton(mainwin,text="Slim",variable=trouser_fit_slim)
		ct29.place(x=sizx+510,y=sizy+460)
		ct30=Checkbutton(mainwin,text="Tapered",variable=trouser_fit_tapered)
		ct30.place(x=sizx+510,y=sizy+480)

		############################ SHirt  #################################


		l5=Label(mainwin,text="Shirt Measurments",fg="red")
		l5.place(x=sizx+10,y=sizy+590)


		# ordernoshirt=Label(mainwin,text="ORDER NO.")
		# ordernoshirt.place(x=sizx+550,y=sizy+580)
		# orderno3= Entry(mainwin,width=8)
		# orderno3.place(x=sizx+620,y=sizy+580)


		Lengths3=Label(mainwin,text="Length")
		Lengths3.place(x=sizx+10,y=sizy+610)
		Length3= Entry(mainwin,width=8)
		Length3.place(x=sizx+10,y=sizy+650)

		Shoulders3=Label(mainwin,text="Shoulder")
		Shoulders3.place(x=sizx+70,y=sizy+610)
		Shoulder3= Entry(mainwin,width=8)
		Shoulder3.place(x=sizx+70,y=sizy+650)

		Sleeves3=Label(mainwin,text="Sleeve")
		Sleeves3.place(x=sizx+130,y=sizy+610)
		Lengthss3=Label(mainwin,text="Length")
		Lengthss3.place(x=sizx+130,y=sizy+630)
		Sleeve3= Entry(mainwin,width=8)
		Sleeve3.place(x=sizx+130,y=sizy+650)

		Chests3=Label(mainwin,text="Chest")
		Chests3.place(x=sizx+190,y=sizy+610)
		Chest3= Entry(mainwin,width=8)
		Chest3.place(x=sizx+190,y=sizy+650)

		Waists3=Label(mainwin,text="Waist")
		Waists3.place(x=sizx+250,y=sizy+610)
		Waist3= Entry(mainwin,width=8)
		Waist3.place(x=sizx+250,y=sizy+650)

		Hips3=Label(mainwin,text="Hip")
		Hips3.place(x=sizx+310,y=sizy+610)
		Hip3= Entry(mainwin,width=8)
		Hip3.place(x=sizx+310,y=sizy+650)

		Cross_Fronts3=Label(mainwin,text="Cross Ft.")
		Cross_Fronts3.place(x=sizx+370,y=sizy+610)
		Cross_Front3= Entry(mainwin,width=8)
		Cross_Front3.place(x=sizx+370,y=sizy+650)

		Cross_Backs3=Label(mainwin,text="Cross Bk.")
		Cross_Backs3.place(x=sizx+430,y=sizy+610)
		Cross_Back3= Entry(mainwin,width=8)
		Cross_Back3.place(x=sizx+430,y=sizy+650)

		Necks3=Label(mainwin,text="Neck")
		Necks3.place(x=sizx+490,y=sizy+610)
		Neck3= Entry(mainwin,width=8)
		Neck3.place(x=sizx+490,y=sizy+650)

		Cuffs3=Label(mainwin,text="Cuff")
		Cuffs3.place(x=sizx+550,y=sizy+610)
		Cuff3= Entry(mainwin,width=8)
		Cuff3.place(x=sizx+550,y=sizy+650)

		Arm_Rounds3=Label(mainwin,text="Arm Round")
		Arm_Rounds3.place(x=sizx+610,y=sizy+610)
		Arm_Round3= Entry(mainwin,width=8)
		Arm_Round3.place(x=sizx+610,y=sizy+650)


		#############################################     Shirt      #################################################


		l6=Label(mainwin,text="Style Details",fg="red")
		l6.place(x=sizx+10,y=sizy+390)

		Bottom=Label(mainwin,text="Bottom")
		Bottom.place(x=sizx+10,y=sizy+680)
		ct31=Checkbutton(mainwin,text="Cut",variable=shirt_bottom_cut)
		ct31.place(x=sizx+10,y=sizy+700)
		ct32=Checkbutton(mainwin,text="Long",variable=shirt_bottom_long)
		ct32.place(x=sizx+10,y=sizy+720)
		ct33=Checkbutton(mainwin,text="Hook",variable=shirt_bottom_hook)
		ct33.place(x=sizx+10,y=sizy+740)


		Pocket=Label(mainwin,text="Pocket")
		Pocket.place(x=sizx+130,y=sizy+680)
		ct34=Checkbutton(mainwin,text="1",variable=shirt_pocket_1)
		ct34.place(x=sizx+90,y=sizy+700)
		ct35=Checkbutton(mainwin,text="2",variable=shirt_pocket_2)
		ct35.place(x=sizx+90,y=sizy+720)
		ct36=Checkbutton(mainwin,text="No",variable=shirt_pocket_no)
		ct36.place(x=sizx+90,y=sizy+740)
		ct37=Checkbutton(mainwin,text="V",variable=shirt_pocket_v)
		ct37.place(x=sizx+140,y=sizy+700)
		ct38=Checkbutton(mainwin,text="Chisel",variable=shirt_pocket_chisel)
		ct38.place(x=sizx+140,y=sizy+720)
		# ct39=Checkbutton(mainwin,text="Round")
		# ct39.place(x=sizx+140,y=sizy+740)
		ct39=Checkbutton(mainwin,text="With Flap",variable=shirt_pocket_withflap)
		ct39.place(x=sizx+140,y=sizy+740)

		FrontPocket=Label(mainwin,text="Front Pocket")
		FrontPocket.place(x=sizx+230,y=sizy+680)
		ct40=Checkbutton(mainwin,text="Plain",variable=shirt_frontpocket_plain)
		ct40.place(x=sizx+230,y=sizy+700)
		ct41=Checkbutton(mainwin,text="Box",variable=shirt_frontpocket_box)
		ct41.place(x=sizx+230,y=sizy+720)
		ct42=Checkbutton(mainwin,text="Plain Fuse",variable=shirt_frontpocket_plainfuse)
		ct42.place(x=sizx+230,y=sizy+740)
		ct43=Checkbutton(mainwin,text="Concealed",variable=shirt_frontpocket_concealed)
		ct43.place(x=sizx+230,y=sizy+760)

		Back=Label(mainwin,text="Back")
		Back.place(x=sizx+340,y=sizy+680)
		ct44=Checkbutton(mainwin,text="Plain",variable=shirt_back_plain)
		ct44.place(x=sizx+340,y=sizy+700)
		ct45=Checkbutton(mainwin,text="Side Pleat",variable=shirt_back_sidepleat)
		ct45.place(x=sizx+340,y=sizy+720)
		ct46=Checkbutton(mainwin,text="Boc Pleat",variable=shirt_back_bocpleat)
		ct46.place(x=sizx+340,y=sizy+740)
		ct47=Checkbutton(mainwin,text="Dart",variable=shirt_back_dart)
		ct47.place(x=sizx+340,y=sizy+760)

		Ready_Front=Label(mainwin,text="Ready Front")
		Ready_Front.place(x=sizx+440,y=sizy+680)
		Ready_Frontinput = Text(mainwin,height=4,width=8)
		Ready_Frontinput.place(x=sizx+440,y=sizy+700)

		# Button(mainwin, text='<<<<',height=2,width=5, command=lambda: FullScreenApp(mainwin)).place(x=680,y=490)


# mainwin.mainloop()