# from PIL import ImageTk, Image
try:
	# Python2
	from Tkinter import Tk,Label,Entry,Button,StringVar,tkMessageBox
	from Tkinter import Text,Checkbutton,IntVar,Toplevel,Message,Scrollbar,RAISED,RIGHT,LEFT,BOTH,END,Y,Listbox,Frame,N,S,W,E
	from ttk import *
except ImportError:
	# Python3
	from tkinter import Tk,Label,Entry,Button,StringVar,messagebox as tkMessageBox
	from tkinter import Text,Checkbutton,IntVar,Toplevel,Message,Scrollbar,RAISED,RIGHT,LEFT,BOTH,END,Y,Listbox,ttk,Frame,N,S,W,E

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import sys
import json
from subprocess import call
from dbconnection.models import * 
tailordir = os.path.join(os.path.join(os.path.expanduser('~'),"Documents"),"Tailor")
billdir = os.path.join(tailordir,"bills")
invoicedir = os.path.join(tailordir,"invoice_template")
imagesdir = os.path.join(tailordir,"images")
dbdir = os.path.join(tailordir,"Database")



particulars = ['total_sherwani','total_trouser','total_3pc','total_kurta','total_safari','total_suit','total_vest_jacket','total_kurta_pyjm','total_tuxedo','total_blazer_jkt','total_overcoat','total_jodhpuri','total_churidar','total_shirt','total_extra_charges']
rate = {}
qty = {}
total = {}
shirt_measure = {}
jacket_measure = {}
trouser_measure = {}




class App(Frame):
	def __init__(self, parent, window, window2):
		Frame.__init__(self, parent)

		self.window = window
		self.window2 = window2
		global search_mob_no

		self.parent = parent

		search_mob_no = StringVar()

		ordn=Label(parent,text="ORDER NO.")
		ordn.place(x=70,y=5)
		ordn1= Entry(parent,width=10)
		ordn1.place(x=65,y=25)

		mob_no_l = Label(parent,text="Mobile")
		mob_no_l.place(x=205,y=5)
		mob_no=Entry(parent,width=12,textvariable=search_mob_no)
		mob_no.place(x=185,y=25)

		Button(parent, text='Search',command= lambda: self.search(ordn1.get(), search_mob_no.get())).place(x=320,y=20)

		msg = Message(self, text="")
		msg.pack(ipady=25)
		
		self.CreateUI()
		# self.LoadTable()

		self.pack(anchor='se')
		parent.grid_rowconfigure(0, weight = 1)
		parent.grid_columnconfigure(0, weight = 1)


	def CreateUI(self):
		tv = ttk.Treeview(self)
		treeScroll = ttk.Scrollbar(self)
		treeScroll.configure(command=tv.yview)
		tv.configure(yscrollcommand=treeScroll.set)

		tv['columns'] = ('order_id','cust_name', 'mobile', 'email','order_date', 'delivery_date')
		tv.heading("#0", text='Count', anchor='w')
		tv.column("#0", anchor="w",width=50)
		tv.heading('cust_name', text='Customer Name')
		tv.column('cust_name', anchor='center', width=180)
		tv.heading('order_id', text='Order Id')
		tv.column('order_id', anchor='center', width=60)
		tv.heading('mobile', text='Contact')
		tv.column('mobile', anchor='center', width=100)
		tv.heading('email', text='Email')
		tv.column('email', anchor='center', width=250)
		tv.heading('order_date', text='Order Date')
		tv.column('order_date', anchor='center', width=100)
		tv.heading('delivery_date', text='Del. Date')
		tv.column('delivery_date', anchor='center', width=100)
		# tv.grid(sticky = (N,S,W,E))
		tv.pack(anchor='se')
		self.treeview = tv
		self.grid_rowconfigure(0, weight = 1)
		self.grid_columnconfigure(0, weight = 1)

	def OnDoubleClick(self, event):
		item = self.treeview.focus()
		order_id = self.treeview.item(item,"values")[0]
		fields = "*"
		condition = "order_id = " + order_id

		self.window.clearVar()
		
		editOrder.set(order_id)

		ord_o = self.order.getData(condition,fields)
		if ord_o != '':
			ord_data = {}
			for order in ord_o['ord_data'] :
				ord_data['customer_id'] = order[0]
				# ord_data['order_id'] = order[1]
				# ord_data['order_date'] = order[2]
				# ord_data['trail_date'] = order[3]
				# ord_data['delivery_date'] =  order[4]

				ord_date.set(order[2])
				trail_date.set(order[3])
				deli_date.set(order[4])
				total_grand.set(order[5])

			Bill = BillDetails()
			bill_data = Bill.getData(condition,fields)
			if bill_data != '':

				for bill in bill_data['bill_data']:
					if bill[1] == 'sherwani':
						rate_sherwani.set(bill[2])
						qty_sherwani.set(bill[3])
						total_sherwani.set(bill[4])
					elif bill[1] == 'trouser':
						rate_trouser.set(bill[2])
						qty_trouser.set(bill[3])
						total_trouser.set(bill[4])
					elif bill[1] == '3pc':
						rate_3pc.set(bill[2])
						qty_3pc.set(bill[3])
						total_3pc.set(bill[4])
					elif bill[1] == 'kurta':
						rate_kurta.set(bill[2])
						qty_kurta.set(bill[3])
						total_kurta.set(bill[4])
					elif bill[1] == 'safari':
						rate_safari.set(bill[2])
						qty_safari.set(bill[3])
						total_safari.set(bill[4])
					elif bill[1] == 'suit':
						rate_suit.set(bill[2])
						qty_suit.set(bill[3])
						total_suit.set(bill[4])
					elif bill[1] == 'vest_jacket':
						rate_vest_jacket.set(bill[2])
						qty_vest_jacket.set(bill[3])
						total_vest_jacket.set(bill[4])
					elif bill[1] == 'kurta_pyjm':
						rate_kurta_pyjm.set(bill[2])
						qty_kurta_pyjm.set(bill[3])
						total_kurta_pyjm.set(bill[4])
					elif bill[1] == 'tuxedo':
						rate_tuxedo.set(bill[2])
						qty_tuxedo.set(bill[3])
						total_tuxedo.set(bill[4])
					elif bill[1] == 'blazer_jkt':
						rate_blazer_jkt.set(bill[2])
						qty_blazer_jkt.set(bill[3])
						total_blazer_jkt.set(bill[4])
					elif bill[1] == 'overcoat':
						rate_overcoat.set(bill[2])
						qty_overcoat.set(bill[3])
						total_overcoat.set(bill[4])
					elif bill[1] == 'jodhpuri':
						rate_jodhpuri.set(bill[2])
						qty_jodhpuri.set(bill[3])
						total_jodhpuri.set(bill[4])
					elif bill[1] == 'churidar':
						rate_churidar.set(bill[2])
						qty_churidar.set(bill[3])
						total_churidar.set(bill[4])
					elif bill[1] == 'shirt':
						rate_shirt.set(bill[2])
						qty_shirt.set(bill[3])
						total_shirt.set(bill[4])
					elif bill[1] == 'extra_charges':
						rate_extra_charges.set(bill[2])
						qty_extra_charges.set(bill[3])
						total_extra_charges.set(bill[4])


			Jacket = MeasurementJacket()
			jack_data = Jacket.getData(condition,fields)

			for jack in jack_data['jack_data']:
				Length1.set(jack[3])
				Shoulder1.set(jack[4])
				Sleeve1.set(jack[5])
				Chest1.set(jack[6])
				Waist1.set(jack[7])
				Hip1.set(jack[8])
				Neck1.set(jack[9])
				Half1.set(jack[10])
				Cross_back1.set(jack[11])
				Cross_front1.set(jack[12])
				Bicep1.set(jack[13])
				Arm1.set(jack[14])

			jacketStyle = MeasurementJacketStyle()
			jack_s_data = jacketStyle.getData(condition,fields)

			for jack_s in jack_s_data['jack_s_data']:

				style1.delete('1.0','end-1c')
				style1.insert('1.0',jack_s[1])

				d = json.loads(jack_s[2].replace("'","\""))
				jacket_lapel_peak.set(d['peak'])
				jacket_lapel_natch.set(d['natch'])
				jacket_lapel_shawl.set(d['Shawl'])

				d = json.loads(jack_s[3].replace("'","\""))				
				jacket_vent_center.set(d['center'])
				jacket_vent_side.set(d['side'])
				jacket_vent_no.set(d['no'])

				d = json.loads(jack_s[4].replace("'","\""))
				jacket_pocket_straight.set(d['straight'])
				jacket_pocket_slant.set(d['slant'])
				jacket_pocket_patch.set(d['patch'])
				jacket_pocket_ticket.set(d['ticket'])

				d = json.loads(jack_s[5].replace("'","\""))
				jacket_fit_regular.set(d['regular'])
				jacket_fit_slim.set(d['slim'])

				d = json.loads(jack_s[6].replace("'","\""))
				jacket_sleeveplacket_functional.set(d['vent'])
				jacket_sleeveplacket_functional.set(d['functional'])



			Shirt = MeasurementShirt()
			shirt_data = Shirt.getData(condition,fields)

			for shirt in shirt_data['shirt_data']:
				Length3.set(shirt[1])
				Shoulder3.set(shirt[2])
				Sleeve3.set(shirt[3])
				Chest3.set(shirt[4])
				Waist3.set(shirt[5])
				Hip3.set(shirt[6])
				Cross_Front3.set(shirt[7])
				Cross_Back3.set(shirt[8])
				Neck3.set(shirt[9])
				Cuff3.set(shirt[10])
				Arm_Round3.set(shirt[11])

			shirtStyle = MeasurementShirtStyle()
			shirt_s_data = shirtStyle.getData(condition,fields)

			for shirt_s in shirt_s_data['shirt_s_data']:
				d = json.loads(shirt_s[1].replace("'","\""))
				shirt_bottom_cut.set(d['cut'])
				shirt_bottom_hook.set(d['hook'])
				shirt_bottom_long.set(d['long'])

				d = json.loads(shirt_s[2].replace("'","\""))
				shirt_pocket_1.set(d['1'])
				shirt_pocket_2.set(d['2'])
				shirt_pocket_no.set(d['no'])
				shirt_pocket_chisel.set(d['chisel'])
				shirt_pocket_withflap.set(d['with_flap'])
				shirt_pocket_v.set(d['v'])

				d = json.loads(shirt_s[3].replace("'","\""))
				shirt_frontpocket_plain.set(d['plain'])
				shirt_frontpocket_box.set(d['box'])
				shirt_frontpocket_plainfuse.set(d['plain_fuse'])
				shirt_frontpocket_concealed.set(d['concealed'])

				d = json.loads(shirt_s[4].replace("'","\""))
				shirt_back_sidepleat.set(d['side_pleat'])
				shirt_back_bocpleat.set(d['boc_pleat'])
				shirt_back_dart.set(d['dart'])
				shirt_back_plain.set(d['plain'])

				Ready_Frontinput.delete('1.0','end-1c')
				Ready_Frontinput.insert('1.0',shirt_s[5])


			Trouser = MeasurementTrouser()
			trou_data = Trouser.getData(condition,fields)
			for trou in trou_data['trou_data']:
				Length2.set(trou[1])
				Inseam2.set(trou[2])
				Crotch2.set(trou[3])
				Waist2.set(trou[4])
				Hip2.set(trou[5])
				Thigh2.set(trou[6])
				Knee2.set(trou[7])
				Bottom2.set(trou[8])
				F_Low2.set(trou[9])

			trouserStyle = MeasurementTrouserStyle()
			trou_s_data = trouserStyle.getData(condition,fields)
			for trou_s in trou_s_data['trou_s_data']:
				d = json.loads(trou_s[1].replace("'","\""))
				trouser_belt_cut.set(d['cut'])
				trouser_belt_vshape.set(d['v_shape'])
				trouser_belt_button.set(d['button'])
				trouser_belt_long.set(d['long'])
				trouser_belt_hook.set(d['hook'])
				trouser_belt_square.set(d['square'])
				trouser_belt_round.set(d['round'])

				d = json.loads(trou_s[2].replace("'","\""))
				trouser_pleat_single.set(d['single'])
				trouser_pleat_double.set(d['double'])
				trouser_pleat_flat.set(d['flat'])

				d = json.loads(trou_s[3].replace("'","\""))
				trouser_pocket_mobile.set(d['mobile'])
				trouser_pocket_l.set(d['l_pocket'])
				trouser_pocket_straight.set(d['straight'])
				trouser_pocket_coin.set(d['coin'])
				trouser_pocket_cross.set(d['cross'])

				d = json.loads(trou_s[4].replace("'","\""))
				trouser_backpocket_1.set(d['1'])
				trouser_backpocket_2.set(d['2'])
				trouser_backpocket_no.set(d['no'])
				trouser_backpocket_loop.set(d['loop'])
				trouser_backpocket_kaaj.set(d['kaaj'])
				trouser_backpocket_flap.set(d['flap'])

				d = json.loads(trou_s[5].replace("'","\""))
				trouser_bottom_plain.set(d['plain'])
				trouser_bottom_slant.set(d['slant'])
				trouser_bottom_turnup.set(d['turnup'])

				# d = json.loads(trou_s[6].replace("'","\""))
				Loopsinput.delete('1.0','end-1c')
				Loopsinput.insert('1.0',trou_s[6])

				d = json.loads(trou_s[7].replace("'","\""))
				trouser_fit_regular.set(d['regular'])
				trouser_fit_slim.set(d['slim'])
				trouser_fit_tapered.set(d['tapered'])

				Sizeinput.delete('1.0','end-1c')
				Sizeinput.insert('1.0',trou_s[8])

				d = json.loads(trou_s[9].replace("'","\""))
				trouser_bottom_full.set(d['full_fb'])
				trouser_bottom_half.set(d['half_fb'])
				trouser_bottom_knee.set(d['knee'])

			# print(jack_data)
			# print(jack_s_data)
			# print(shirt_data)
			# print(shirt_s_data)
			# print(trou_data)
			# print(trou_s_data)

			# xtop = Toplevel()
			# msg = Message(xtop, text= "you clicked on " + ord_data)
			# msg.pack()

			fields = "name, phone, email, address "
			condition = "uid = " + str(ord_data['customer_id'])

			cus_o = self.cust.getData(condition,fields)
			if cus_o != '':
				cus_data = {}
				for customer in cus_o['cus_data']:
					cus_data['name'] = customer[0]
					cus_data['phone'] = customer[1]
					cus_data['email'] = customer[2]
					cus_data['address'] = customer[3]

					cus_name.set(customer[0])
					cus_mobile.set(customer[1])
					cus_email.set(customer[2])
					cus_address.set(customer[3])

			self.window.edit()
			# self.window2.destroy()

			self.parent.destroy()

			# self.window.printbill()


	def search(self, orderId, mobile_no):
		self.cust = CustomerDetails()
		self.order = OrderDetails()

		self.treeview.delete(*self.treeview.get_children())

		if orderId != '':
			fields = "order_id, customer_id, order_date, delivery_date, trail_date"
			condition = "order_id = " + str(orderId)
			data_o = self.order.getData(condition,fields)
			i = 1;
			if data_o != '':
				for ord_data in data_o['ord_data']:
					fields = "name, phone, email"
					condition = "uid = " + str(ord_data[1])
					cus_data = self.cust.getData(condition, fields)
					if cus_data != '':
						data_c = cus_data['cus_data']
						for data in data_c:
							self.treeview.insert('', 'end', text=i, values=(ord_data[0],data[0], data[1], data[2],ord_data[2] ,ord_data[3] ))
							i = i+1
		else:
			fields = "uid, name, phone, email"
			condition = "phone LIKE '%" + str(mobile_no) + "%'"

			cus_data = self.cust.getData(condition, fields)

			if cus_data != '':
				data_c = cus_data['cus_data']


				i=1
				for data in data_c:
					fields = "order_id, customer_id, order_date, delivery_date, trail_date"
					condition = "customer_id = "+ str(data[0])

					data_o = self.order.getData(condition,fields)

					if data_o != '':
						for ord_data in data_o['ord_data']:
							self.treeview.insert('', 'end', text=i, values=(ord_data[0],data[1], data[2], data[3],ord_data[2] ,ord_data[3] ))
							i = i+1
					else:
						self.treeview.insert('', 'end', text=i, values=( "", data[1], data[2], data[3],"" ,"" ))
						i = i+1

		self.treeview.bind("<Double-1>",self.OnDoubleClick)


	def LoadTable(self):
		rate_sherwani.set(100)
		cus_name.set("piyush")


class FullScreenApp(object):

	def callback(self,rate,qty,total):
		if rate.get() != '' and qty.get() != '':
			total.set( int(rate.get()) * int(qty.get()))
		else:
			total.set('0')

		total_g = int(total_sherwani.get()) + int(total_trouser.get()) + int(total_3pc.get()) + int(total_kurta.get()) + int(total_suit.get()) + int(total_safari.get()) + int(total_tuxedo.get()) +  int(total_vest_jacket.get()) +  int(total_kurta_pyjm.get()) +  int(total_blazer_jkt.get()) +  int(total_overcoat.get()) +  int(total_jodhpuri.get()) +  int(total_churidar.get()) +  int(total_shirt.get()) +  int(total_extra_charges.get())
		total_grand.set(total_g)

	def search(self):
		top = Toplevel()
		top.title("Search Wizard")
		App(top,self,self.main1)
		button = Button(top, text="Dismiss", command=top.destroy)
		button.pack()

	def __init__(self, mainwin, root, main1, **kwargs):
		global cus_name,cus_email,cus_mobile,cus_address,ord_date,deli_date, trail_date, editOrder
		global total_grand, total_sherwani,total_trouser,total_3pc,total_kurta,total_suit,total_safari,total_tuxedo, total_vest_jacket, total_kurta_pyjm, total_blazer_jkt, total_overcoat, total_jodhpuri, total_churidar, total_shirt, total_extra_charges		
		global rate_sherwani, rate_trouser, rate_3pc, rate_kurta, rate_safari, rate_suit, rate_vest_jacket, rate_kurta_pyjm, rate_tuxedo, rate_blazer_jkt, rate_overcoat, rate_jodhpuri, rate_churidar, rate_shirt, rate_extra_charges
		global qty_sherwani, qty_trouser, qty_3pc, qty_kurta, qty_safari, qty_suit, qty_vest_jacket, qty_kurta_pyjm, qty_tuxedo, qty_blazer_jkt, qty_overcoat, qty_jodhpuri, qty_churidar, qty_shirt, qty_extra_charges

		self.root = root
		self.mainwin = mainwin
		self.main1 = main1

		cus_name = StringVar()
		cus_email = StringVar()
		# cus_mobile = IntVar()
		cus_mobile = StringVar()
		cus_address = StringVar()

		ord_date = StringVar()
		trail_date = StringVar()
		deli_date = StringVar()

		rate_sherwani = StringVar()
		qty_sherwani = StringVar()
		total_sherwani = StringVar()

		rate_trouser = StringVar()
		qty_trouser = StringVar()
		total_trouser = StringVar()

		rate_3pc = StringVar()
		qty_3pc = StringVar()
		total_3pc = StringVar()

		rate_kurta = StringVar()
		qty_kurta = StringVar()
		total_kurta = StringVar()

		rate_safari = StringVar()
		qty_safari = StringVar()
		total_safari = StringVar()

		rate_suit = StringVar()
		qty_suit = StringVar()
		total_suit = StringVar()

		rate_vest_jacket = StringVar()
		qty_vest_jacket = StringVar()
		total_vest_jacket = StringVar()

		rate_kurta_pyjm = StringVar()
		qty_kurta_pyjm = StringVar()
		total_kurta_pyjm = StringVar()

		rate_tuxedo = StringVar()
		qty_tuxedo = StringVar()
		total_tuxedo = StringVar()

		rate_blazer_jkt = StringVar()
		qty_blazer_jkt = StringVar()
		total_blazer_jkt = StringVar()

		rate_overcoat = StringVar()
		qty_overcoat = StringVar()
		total_overcoat = StringVar()

		rate_jodhpuri = StringVar()
		qty_jodhpuri = StringVar()
		total_jodhpuri = StringVar()

		rate_churidar = StringVar()
		qty_churidar = StringVar()
		total_churidar = StringVar()

		rate_shirt = StringVar()
		qty_shirt = StringVar()
		total_shirt = StringVar()

		rate_extra_charges = StringVar()
		qty_extra_charges = StringVar()
		total_extra_charges = StringVar()

		editOrder = StringVar()

		total_sherwani.set(0),total_trouser.set(0),total_3pc.set(0),total_kurta.set(0),total_suit.set(0),total_safari.set(0),total_tuxedo.set(0), total_vest_jacket.set(0), total_kurta_pyjm.set(0), total_blazer_jkt.set(0), total_overcoat.set(0), total_jodhpuri.set(0), total_churidar.set(0), total_shirt.set(0), total_extra_charges.set(0)

		total_grand = StringVar()

		rate_sherwani.trace("w", lambda name, index, mode, rate_sherwani=rate_sherwani: self.callback(rate_sherwani,qty_sherwani,total_sherwani))
		qty_sherwani.trace("w", lambda name, index, mode, qty_sherwani=qty_sherwani: self.callback(rate_sherwani,qty_sherwani,total_sherwani))
		
		rate_trouser.trace("w", lambda name, index, mode, rate_trouser=rate_trouser: self.callback(rate_trouser,qty_trouser,total_trouser))
		qty_trouser.trace("w", lambda name, index, mode, qty_trouser=qty_trouser: self.callback(rate_trouser,qty_trouser,total_trouser))

		rate_3pc.trace("w", lambda name, index, mode, rate_3pc=rate_3pc: self.callback(rate_3pc,qty_3pc,total_3pc))
		qty_3pc.trace("w", lambda name, index, mode, qty_3pc=qty_3pc: self.callback(rate_3pc,qty_3pc,total_3pc))

		rate_kurta.trace("w", lambda name, index, mode, rate_kurta=rate_kurta: self.callback(rate_kurta,qty_kurta,total_kurta))
		qty_kurta.trace("w", lambda name, index, mode, qty_kurta=qty_kurta: self.callback(rate_kurta,qty_kurta,total_kurta))


		rate_safari.trace("w", lambda name, index, mode, rate_safari=rate_safari: self.callback(rate_safari,qty_safari,total_safari))
		qty_safari.trace("w", lambda name, index, mode, qty_safari=qty_safari: self.callback(rate_safari,qty_safari,total_safari))


		rate_suit.trace("w", lambda name, index, mode, rate_suit=rate_suit: self.callback(rate_suit,qty_suit,total_suit))
		qty_suit.trace("w", lambda name, index, mode, qty_suit=qty_suit: self.callback(rate_suit,qty_suit,total_suit))


		rate_vest_jacket.trace("w", lambda name, index, mode, rate_vest_jacket=rate_vest_jacket: self.callback(rate_vest_jacket,qty_vest_jacket,total_vest_jacket))
		qty_vest_jacket.trace("w", lambda name, index, mode, qty_vest_jacket=qty_vest_jacket: self.callback(rate_vest_jacket,qty_vest_jacket,total_vest_jacket))


		rate_kurta_pyjm.trace("w", lambda name, index, mode, rate_kurta_pyjm=rate_kurta_pyjm: self.callback(rate_kurta_pyjm,qty_kurta_pyjm,total_kurta_pyjm))
		qty_kurta_pyjm.trace("w", lambda name, index, mode, qty_kurta_pyjm=qty_kurta_pyjm: self.callback(rate_kurta_pyjm,qty_kurta_pyjm,total_kurta_pyjm))


		rate_tuxedo.trace("w", lambda name, index, mode, rate_tuxedo=rate_tuxedo: self.callback(rate_tuxedo,qty_tuxedo,total_tuxedo))
		qty_tuxedo.trace("w", lambda name, index, mode, qty_tuxedo=qty_tuxedo: self.callback(rate_tuxedo,qty_tuxedo,total_tuxedo))


		rate_blazer_jkt.trace("w", lambda name, index, mode, rate_blazer_jkt=rate_blazer_jkt: self.callback(rate_blazer_jkt,qty_blazer_jkt,total_blazer_jkt))
		qty_blazer_jkt.trace("w", lambda name, index, mode, qty_blazer_jkt=qty_blazer_jkt: self.callback(rate_blazer_jkt,qty_blazer_jkt,total_blazer_jkt))


		rate_overcoat.trace("w", lambda name, index, mode, rate_overcoat=rate_overcoat: self.callback(rate_overcoat,qty_overcoat,total_overcoat))
		qty_overcoat.trace("w", lambda name, index, mode, qty_overcoat=qty_overcoat: self.callback(rate_overcoat,qty_overcoat,total_overcoat))


		rate_jodhpuri.trace("w", lambda name, index, mode, rate_jodhpuri=rate_jodhpuri: self.callback(rate_jodhpuri,qty_jodhpuri,total_jodhpuri))
		qty_jodhpuri.trace("w", lambda name, index, mode, qty_jodhpuri=qty_jodhpuri: self.callback(rate_jodhpuri,qty_jodhpuri,total_jodhpuri))


		rate_churidar.trace("w", lambda name, index, mode, rate_churidar=rate_churidar: self.callback(rate_churidar,qty_churidar,total_churidar))
		qty_churidar.trace("w", lambda name, index, mode, qty_churidar=qty_churidar: self.callback(rate_churidar,qty_churidar,total_churidar))


		rate_shirt.trace("w", lambda name, index, mode, rate_shirt=rate_shirt: self.callback(rate_shirt,qty_shirt,total_shirt))
		qty_shirt.trace("w", lambda name, index, mode, qty_shirt=qty_shirt: self.callback(rate_shirt,qty_shirt,total_shirt))


		rate_extra_charges.trace("w", lambda name, index, mode, rate_extra_charges=rate_extra_charges: self.callback(rate_extra_charges,qty_extra_charges,total_extra_charges))
		qty_extra_charges.trace("w", lambda name, index, mode, qty_extra_charges=qty_extra_charges: self.callback(rate_extra_charges,qty_extra_charges,total_extra_charges))


	def clearWindow(self):
		for widget in self.winfo_children():
			widget.pack_forget()
			widget.grid_forget()
			widget.place_forget()

	def clearVar(self):
		cus_name.set('')
		cus_email.set('')
		cus_address.set('')
		cus_mobile.set('')
		ord_date.set('')
		trail_date.set('')
		deli_date.set('')

		rate_sherwani.set('')
		qty_sherwani.set('')
		total_sherwani.set(0)

		rate_trouser.set('')
		qty_trouser.set('')
		total_trouser.set(0)

		rate_3pc.set('')
		qty_3pc.set('')
		total_3pc.set(0)

		rate_kurta.set('')
		qty_kurta.set('')
		total_kurta.set(0)

		rate_safari.set('')
		qty_safari.set('')
		total_safari.set(0)

		rate_suit.set('')
		qty_suit.set('')
		total_suit.set(0)

		rate_vest_jacket.set('')
		qty_vest_jacket.set('')
		total_vest_jacket.set(0)

		rate_kurta_pyjm.set('')
		qty_kurta_pyjm.set('')
		total_kurta_pyjm.set(0)

		rate_tuxedo.set('')
		qty_tuxedo.set('')
		total_tuxedo.set(0)

		rate_blazer_jkt.set('')
		qty_blazer_jkt.set('')
		total_blazer_jkt.set(0)

		rate_overcoat.set('')
		qty_overcoat.set('')
		total_overcoat.set(0)

		rate_jodhpuri.set('')
		qty_jodhpuri.set('')
		total_jodhpuri.set(0)

		rate_churidar.set('')
		qty_churidar.set('')
		total_churidar.set(0)

		rate_shirt.set('')
		qty_shirt.set('')
		total_shirt.set(0)

		rate_extra_charges.set('')
		qty_extra_charges.set('')
		total_extra_charges.set(0)	

		total_grand.set(0)

		Length1.set('')
		Sleeve1.set('')
		Shoulder1.set('')
		Chest1.set('')
		Waist1.set('')
		Hip1.set('')
		Neck1.set('')
		Half1.set('')
		Cross_front1.set('')
		Cross_back1.set('')
		Bicep1.set('')
		Arm1.set('')

		Length2.set('')
		Inseam2.set('')
		Crotch2.set('')
		Waist2.set('')
		Hip2.set('')
		Thigh2.set('')
		Knee2.set('')
		Bottom2.set('')
		F_Low2.set('')



		Length3.set('')
		Sleeve3.set('')
		Shoulder3.set('')
		Chest3.set('')
		Waist3.set('')
		Hip3.set('')
		Cross_Front3.set('')
		Cross_Back3.set('')
		Neck3.set('')
		Cuff3.set('')
		Arm_Round3.set('')

		style1.delete('1.0','end-1c')
		Ready_Frontinput.delete('1.0','end-1c')
		Loopsinput.delete('1.0','end-1c')
		Sizeinput.delete('1.0','end-1c')

		jacket_lapel_peak.set(0)
		jacket_lapel_natch.set(0)
		jacket_lapel_shawl.set(0)
		jacket_vent_no.set(0)
		jacket_vent_side.set(0)
		jacket_vent_center.set(0)
		jacket_pocket_straight.set(0)
		jacket_pocket_slant.set(0)
		jacket_pocket_patch.set(0)
		jacket_pocket_ticket.set(0)
		jacket_fit_regular.set(0)
		jacket_fit_slim.set(0)
		jacket_sleeveplacket_vent.set(0)
		jacket_sleeveplacket_functional.set(0)

		trouser_belt_cut.set(0)
		trouser_belt_long.set(0)
		trouser_belt_hook.set(0)
		trouser_belt_button.set(0)
		trouser_belt_square.set(0)
		trouser_belt_round.set(0)
		trouser_belt_vshape.set(0)
		trouser_pleat_single.set(0)
		trouser_pleat_double.set(0)
		trouser_pleat_flat.set(0)
		trouser_pocket_cross.set(0)
		trouser_pocket_straight.set(0)
		trouser_pocket_l.set(0)
		trouser_pocket_mobile.set(0)
		trouser_pocket_coin.set(0)
		trouser_backpocket_1.set(0)
		trouser_backpocket_2.set(0)
		trouser_backpocket_no.set(0)
		trouser_backpocket_loop.set(0)
		trouser_backpocket_kaaj.set(0)
		trouser_backpocket_flap.set(0)
		trouser_bottom_plain.set(0)
		trouser_bottom_slant.set(0)
		trouser_bottom_turnup.set(0)
		trouser_bottom_lining.set(0)
		trouser_bottom_knee.set(0)
		trouser_bottom_half.set(0)
		trouser_bottom_full.set(0)
		trouser_fit_regular.set(0)
		trouser_fit_slim.set(0)
		trouser_fit_tapered.set(0)


		shirt_bottom_cut.set(0)
		shirt_bottom_long.set(0)
		shirt_bottom_hook.set(0)
		shirt_pocket_1.set(0)
		shirt_pocket_2.set(0)
		shirt_pocket_no.set(0)
		shirt_pocket_v.set(0)
		shirt_pocket_chisel.set(0)
		shirt_pocket_withflap.set(0)
		shirt_frontpocket_plain.set(0)
		shirt_frontpocket_box.set(0)
		shirt_frontpocket_plainfuse.set(0)
		shirt_frontpocket_concealed.set(0)
		shirt_back_plain.set(0)
		shirt_back_sidepleat.set(0)
		shirt_back_bocpleat.set(0)
		shirt_back_dart.set(0)	


		editOrder.set('')

	def create(self,mainwin):

		for widget in self.mainwin.winfo_children():
			widget.pack_forget()
			widget.grid_forget()
			widget.place_forget()

		siz = -50
		wid = 0
		global e13,e14

		self.clearVar()

		# orderno=Label(mainwin,text="ORDER NO.")
		# orderno.place(x=500,y=320)
		# orderno1= Entry(mainwin,width=wid+10)
		# orderno1.place(x=500,y=340)
		Button(mainwin, text='Search',height=1,command= lambda: self.search()).place(x=500,y=370)

		l1=Label(mainwin,text="Costomer Name")
		l1.place(x=10,y=siz+60)
		e1= Entry(mainwin,width=wid+30,textvariable=cus_name)
		e1.place(x=120,y=siz+60)

		l2=Label(mainwin,text="Address")
		l2.place(x=10,y=siz+90)
		e2 = Entry(mainwin,width=wid+30,textvariable=cus_address)
		e2.place(x=120,y=siz+90)

		l3=Label(mainwin,text="Email Id")
		l3.place(x=10,y=siz+150)
		e3= Entry(mainwin,width=wid+30,textvariable=cus_email)
		e3.place(x=120,y=siz+150)

		l4=Label(mainwin,text="Phone no.")
		l4.place(x=380,y=siz+60)
		e4= Entry(mainwin,width=wid+22,textvariable=cus_mobile)
		e4.place(x=470,y=siz+60)

		l5=Label(mainwin,text="Order date")
		l5.place(x=380,y=siz+90)
		e5= Entry(mainwin,width=wid+22,textvariable=ord_date)
		e5.place(x=470,y=siz+90)

		l6=Label(mainwin,text="Trail date")
		l6.place(x=380,y=siz+120)
		e6= Entry(mainwin,width=wid+22,textvariable=trail_date)
		e6.place(x=470,y=siz+120)

		l7=Label(mainwin,text="Delivery date")
		l7.place(x=380,y=siz+150)
		e7= Entry(mainwin,width=wid+22,textvariable=deli_date)
		e7.place(x=470,y=siz+150)

		l8=Label(mainwin,text="PU")
		l8.place(x=30,y=siz+190)
		l81=Label(mainwin,text="62")
		l81.place(x=30,y=siz+220)
		l82=Label(mainwin,text="63")
		l82.place(x=30,y=siz+250)
		l83=Label(mainwin,text="64")
		l83.place(x=30,y=siz+280)
		l84=Label(mainwin,text="65")
		l84.place(x=30,y=siz+310)
		l85=Label(mainwin,text="67")
		l85.place(x=30,y=siz+340)
		l86=Label(mainwin,text="68")
		l86.place(x=30,y=siz+370)
		l87=Label(mainwin,text="69")
		l87.place(x=30,y=siz+400)
		l88=Label(mainwin,text="71")
		l88.place(x=30,y=siz+430)
		l89=Label(mainwin,text="72")
		l89.place(x=30,y=siz+460)
		l810=Label(mainwin,text="73")
		l810.place(x=30,y=siz+490)
		l811=Label(mainwin,text="74")
		l811.place(x=30,y=siz+520)
		l812=Label(mainwin,text="75")
		l812.place(x=30,y=siz+550)
		l813=Label(mainwin,text="76")
		l813.place(x=30,y=siz+580)
		l814=Label(mainwin,text="83")
		l814.place(x=30,y=siz+610)
		l815=Label(mainwin,text="91")
		l815.place(x=30,y=siz+640)


		l9=Label(mainwin,text="Particular")
		l9.place(x=90,y=siz+190)
		l91=Label(mainwin,text="SHERWANI")
		l91.place(x=90,y=siz+220)
		l92=Label(mainwin,text="TROUSERS")
		l92.place(x=90,y=siz+250)
		l93=Label(mainwin,text="3PC SUIT")
		l93.place(x=90,y=siz+280)
		l94=Label(mainwin,text="KURTA")
		l94.place(x=90,y=siz+310)
		l95=Label(mainwin,text="SAFARI")
		l95.place(x=90,y=siz+340)
		l96=Label(mainwin,text="SUIT")
		l96.place(x=90,y=siz+370)
		l97=Label(mainwin,text="VEST-JACKET")
		l97.place(x=90,y=siz+400)
		l98=Label(mainwin,text="KURTA-PYJM")
		l98.place(x=90,y=siz+430)
		l99=Label(mainwin,text="TUXEDO")
		l99.place(x=90,y=siz+460)
		l910=Label(mainwin,text="BLAZER/JKT")
		l910.place(x=90,y=siz+490)
		l911=Label(mainwin,text="OVERCOAT")
		l911.place(x=90,y=siz+520)
		l912=Label(mainwin,text="JODHPURI SUIT")
		l912.place(x=90,y=siz+550)
		l913=Label(mainwin,text="CHURIDAR")
		l913.place(x=90,y=siz+580)
		l914=Label(mainwin,text="SHIRT")
		l914.place(x=90,y=siz+610)
		l915=Label(mainwin,text="ACCESSORIES")
		l915.place(x=90,y=siz+640)
		l916=Label(mainwin,text="EMBROIDERY")
		l916.place(x=90,y=siz+640)
		l917=Label(mainwin,text="EXTRA CHARGES")
		l917.place(x=90,y=siz+640)

		l10=Label(mainwin,text="Rate")
		l10.place(x=210,y=siz+190)


		e101= Entry(mainwin,width=wid+10,textvariable=rate_sherwani)
		e101.place(x=210,y=siz+220)
		e111= Entry(mainwin,width=wid+10,textvariable=qty_sherwani)
		e111.place(x=290,y=siz+220)

		e102= Entry(mainwin,width=wid+10,textvariable=rate_trouser)
		e102.place(x=210,y=siz+250)
		e112= Entry(mainwin,width=wid+10,textvariable=qty_trouser)
		e112.place(x=290,y=siz+250)

		e103= Entry(mainwin,width=wid+10,textvariable=rate_3pc)
		e103.place(x=210,y=siz+280)
		e113= Entry(mainwin,width=wid+10,textvariable=qty_3pc)
		e113.place(x=290,y=siz+280)

		e104= Entry(mainwin,width=wid+10,textvariable=rate_kurta)
		e104.place(x=210,y=siz+310)
		e114= Entry(mainwin,width=wid+10,textvariable=qty_kurta)
		e114.place(x=290,y=siz+310)

		e105= Entry(mainwin,width=wid+10,textvariable=rate_safari)
		e105.place(x=210,y=siz+340)
		e115= Entry(mainwin,width=wid+10,textvariable=qty_safari)
		e115.place(x=290,y=siz+340)

		e106= Entry(mainwin,width=wid+10,textvariable=rate_suit)
		e106.place(x=210,y=siz+370)
		e116= Entry(mainwin,width=wid+10,textvariable=qty_suit)
		e116.place(x=290,y=siz+370)

		e107= Entry(mainwin,width=wid+10,textvariable=rate_vest_jacket)
		e107.place(x=210,y=siz+400)
		e117= Entry(mainwin,width=wid+10,textvariable=qty_vest_jacket)
		e117.place(x=290,y=siz+400)

		e108= Entry(mainwin,width=wid+10,textvariable=rate_kurta_pyjm)
		e108.place(x=210,y=siz+430)
		e118= Entry(mainwin,width=wid+10,textvariable=qty_kurta_pyjm)
		e118.place(x=290,y=siz+430)

		e109= Entry(mainwin,width=wid+10,textvariable=rate_tuxedo)
		e109.place(x=210,y=siz+460)
		e119= Entry(mainwin,width=wid+10,textvariable=qty_tuxedo)
		e119.place(x=290,y=siz+460)

		e1010= Entry(mainwin,width=wid+10,textvariable=rate_blazer_jkt)
		e1010.place(x=210,y=siz+490)
		e1110= Entry(mainwin,width=wid+10,textvariable=qty_blazer_jkt)
		e1110.place(x=290,y=siz+490)

		e1011= Entry(mainwin,width=wid+10,textvariable=rate_overcoat)
		e1011.place(x=210,y=siz+520)
		e1111= Entry(mainwin,width=wid+10,textvariable=qty_overcoat)
		e1111.place(x=290,y=siz+520)

		e1012= Entry(mainwin,width=wid+10,textvariable=rate_jodhpuri)
		e1012.place(x=210,y=siz+550)
		e1112= Entry(mainwin,width=wid+10,textvariable=qty_jodhpuri)
		e1112.place(x=290,y=siz+550)

		e1013= Entry(mainwin,width=wid+10,textvariable=rate_churidar)
		e1013.place(x=210,y=siz+580)
		e1113= Entry(mainwin,width=wid+10,textvariable=qty_churidar)
		e1113.place(x=290,y=siz+580)

		e1014= Entry(mainwin,width=wid+10,textvariable=rate_shirt)
		e1014.place(x=210,y=siz+610)
		e1114= Entry(mainwin,width=wid+10,textvariable=qty_shirt)
		e1114.place(x=290,y=siz+610)

		e1015= Entry(mainwin,width=wid+10,textvariable=rate_extra_charges)
		e1015.place(x=210,y=siz+640)
		e1115= Entry(mainwin,width=wid+10,textvariable=qty_extra_charges)
		e1115.place(x=290,y=siz+640)

		l11=Label(mainwin,text="Qty")
		l11.place(x=290,y=siz+190)
		l12=Label(mainwin,text="Rs.")

		l12.place(x=370,y=siz+190)
		e121= Entry(mainwin,width=wid+10,textvariable=total_sherwani)
		e121.place(x=370,y=siz+220)
		e122= Entry(mainwin,width=wid+10,textvariable=total_trouser)
		e122.place(x=370,y=siz+250)
		e123= Entry(mainwin,width=wid+10,textvariable=total_3pc)
		e123.place(x=370,y=siz+280)
		e124= Entry(mainwin,width=wid+10,textvariable=total_kurta)
		e124.place(x=370,y=siz+310)
		e125= Entry(mainwin,width=wid+10,textvariable=total_safari)
		e125.place(x=370,y=siz+340)
		e126= Entry(mainwin,width=wid+10,textvariable=total_suit)
		e126.place(x=370,y=siz+370)
		e127= Entry(mainwin,width=wid+10,textvariable=total_vest_jacket)
		e127.place(x=370,y=siz+400)
		e128= Entry(mainwin,width=wid+10,textvariable=total_kurta_pyjm)
		e128.place(x=370,y=siz+430)
		e129= Entry(mainwin,width=wid+10,textvariable=total_tuxedo)
		e129.place(x=370,y=siz+460)
		e1210= Entry(mainwin,width=wid+10,textvariable=total_blazer_jkt)
		e1210.place(x=370,y=siz+490)
		e1211= Entry(mainwin,width=wid+10,textvariable=total_overcoat)
		e1211.place(x=370,y=siz+520)
		e1212= Entry(mainwin,width=wid+10,textvariable=total_jodhpuri)
		e1212.place(x=370,y=siz+550)
		e1213= Entry(mainwin,width=wid+10,textvariable=total_churidar)
		e1213.place(x=370,y=siz+580)
		e1214= Entry(mainwin,width=wid+10,textvariable=total_shirt)
		e1214.place(x=370,y=siz+610)
		e1215= Entry(mainwin,width=wid+10,textvariable=total_extra_charges)
		e1215.place(x=370,y=siz+640)
		e1216= Entry(mainwin,width=wid+10,textvariable=total_grand)
		e1216.place(x=370,y=siz+670)

		l12=Label(mainwin,text="Total.")
		l12.place(x=320,y=siz+670)

		l13=Label(mainwin,text="Approximate Trail Date")
		l13.place(x=50,y=siz+690)
		e13= Entry(mainwin,width=wid+10)
		e13.place(x=220,y=siz+690)

		l14=Label(mainwin,text="Approximate Delivery Date")
		l14.place(x=50,y=siz+720)
		e14= Entry(mainwin,width=wid+10)
		e14.place(x=220,y=siz+720)

		Button(self.mainwin, text='Save',height=2,width=5 ,command= lambda: setCustomerDetails(self.root)).place(x=450,y=650)
		Button(self.mainwin, text='Cancel',height=2,width=9, command=self.root.destroy).place(x=520,y=650)

		# Button(mainwin, text='>>>>',height=2,width=wid+5, command=setCustomerDetails ).place(x=520,y=490)

	def edit(self):
		siz = -50
		wid = 0
		# self.create(self.mainwin)

		orderno=Label(self.mainwin,text="ORDER NO.")
		orderno.place(x=500,y=320)
		orderno1= Entry(self.mainwin,width=wid+10,textvariable=editOrder)
		orderno1.place(x=500,y=340)

		Button(self.mainwin, text='Print',height=2,width=5, command=lambda: self.printbill()).place(x=450,y=650)
		Button(self.mainwin, text='New Order',height=2,width=9, command=lambda: self.create(self.mainwin)).place(x=520,y=650)

	def getBill(self,name,rate, qty, total):
		ret_data = '''<tr>
			            <td class="service">'''+ name + ''' </td>
			            <td class="unit">'''+ rate + '''</td>
			            <td class="qty">'''+ qty + '''</td>
			            <td class="total">'''+ total + '''</td>
			          </tr>'''
		return ret_data

	def printbill(self):
		fi = open(os.path.join(billdir,editOrder.get().strip()+".html"),'w')
		particulars_bill = ''

		if int(total_sherwani.get()) > 0:
			particulars_bill += self.getBill("SHERWANI",rate_sherwani.get(),qty_sherwani.get(),total_sherwani.get())

		if int(total_trouser.get()) > 0:
			particulars_bill += self.getBill("TROUSER",rate_trouser.get(),qty_trouser.get(),total_trouser.get())
		
		if int(total_3pc.get()) > 0:
			particulars_bill += self.getBill("3PC",rate_3pc.get(),qty_3pc.get(),total_3pc.get())
		
		if int(total_kurta.get()) > 0:
			particulars_bill += self.getBill("KURTA",rate_kurta.get(),qty_kurta.get(),total_kurta.get())
		
		if int(total_safari.get()) > 0:
			particulars_bill += self.getBill("SAFARI",rate_safari.get(),qty_safari.get(),total_safari.get())
		
		if int(total_suit.get()) > 0:
			particulars_bill += self.getBill("SUIT",rate_suit.get(),qty_suit.get(),total_suit.get())
		
		if int(total_vest_jacket.get()) > 0:
			particulars_bill += self.getBill("VEST-JACKET",rate_vest_jacket.get(),qty_vest_jacket.get(),total_vest_jacket.get())
		
		if int(total_kurta_pyjm.get()) > 0:
			particulars_bill += self.getBill("KURTA-PYJM",rate_kurta_pyjm.get(),qty_kurta_pyjm.get(),total_kurta_pyjm.get())
		
		if int(total_tuxedo.get()) > 0:
			particulars_bill += self.getBill("TUXEDO",rate_tuxedo.get(),qty_tuxedo.get(),total_tuxedo.get())

		if int(total_blazer_jkt.get()) > 0:
			particulars_bill += self.getBill("BLAZER",rate_blazer_jkt.get(),qty_blazer_jkt.get(),total_blazer_jkt.get())
		
		if int(total_overcoat.get()) > 0:
			particulars_bill += self.getBill("OVERCOAT",rate_overcoat.get(),qty_overcoat.get(),total_overcoat.get())
		
		if int(total_jodhpuri.get()) > 0:
			particulars_bill += self.getBill("JODHPURI",rate_jodhpuri.get(),qty_jodhpuri.get(),total_jodhpuri.get())
		
		if int(total_churidar.get()) > 0:
			particulars_bill += self.getBill("CHURIDAR",rate_churidar.get(),qty_churidar.get(),total_churidar.get())
		
		if int(total_shirt.get()) > 0:
			particulars_bill += self.getBill("SHIRT",rate_shirt.get(),qty_shirt.get(),total_shirt.get())
		
		if int(total_extra_charges.get()) > 0:
			particulars_bill += self.getBill("EXTRA",rate_extra_charges.get(),qty_extra_charges.get(),total_extra_charges.get())


		str = '''<!DOCTYPE html>
				<html lang="en">
			  <head>
			    <meta charset="utf-8">
			    <title>Example 1</title>
			    <link rel="stylesheet" href="'''+ invoicedir +'''/style.css" media="all" />
			    <style type="text/css">
			    </style>
			  </head>
			  <body>
			    <header class="clearfix">
			      <div id="logo">
			        <img src="../images/bt.jpg">
			      </div>
			      <h1>BESPOKE # INVOICE</h1>
			      <div id="company" class="clearfix">
			        <div>BeSpoke Tailoring</div>
			        <div> L.G.F., F-11, Eldeco Magnum Plaza<br /> Eldeco Green, <br/> Gomti Nagar, Lucknow</div>
        			<div>9696401314, 9935106200</div>
			      </div>
			      <div id="project">
			        <div><strong><span>ORDER # ..</span> '''+ editOrder.get() +'''</strong></div><br/>
			        <div><span>CUSTOMER</span> '''+ cus_name.get() +'''</div>
			        <div><span>MOBILE N0</span> '''+ cus_mobile.get() +'''</div>
			        <div><span>EMAIL.......</span> <a href="mailto:'''+ cus_email.get() +'''">'''+ cus_email.get() +'''</a></div>
			        <div><span>DATE.........</span> '''+ ord_date.get() +'''</div>
			        <div><span>DUE DATE ....</span> '''+ deli_date.get() +'''</div>
			        <div><span>ADDRESS .</span> '''+ cus_address.get() +''', INDIA</div>
			      </div>
			    </header>
			    <main>
			      <table>
			        <thead>
			          <tr>
			            <th class="service">SERVICE</th>
			            <th>PRICE</th>
			            <th>QTY</th>
			            <th>TOTAL</th>
			          </tr>
			        </thead>
			        <tbody>
			          '''+ particulars_bill + '''
			          
			          <tr>
			            <td colspan="3" class="grand total">GRAND TOTAL</td>
			            <td class="grand total"> Rs.'''+ total_grand.get() +'''</td>
			          </tr>
			        </tbody>
			      </table>
			    </main>
			    <footer>
			      Invoice was created on a computer and is valid without the signature and seal.
			    </footer>
			  </body>
			</html>'''
		
		fi.write(str)
		fi.close()

		data={}
		data['req'] = 'success'
		data['msg'] = "Bill Generated"
		NotifyMsg(data)


class FullScreenApp1(object):
	def __init__(self, mainwin, root, **kwargs):
		global Length1, Shoulder1, Sleeve1, Chest1,Waist1,Hip1,Neck1,Half1,Cross_back1,Cross_front1,Bicep1,Arm1
		global Arm1,style1,Length2, Inseam2, Crotch2, Waist2, Hip2, Thigh2, Knee2, Bottom2, F_Low2, Loopsinput,Sizeinput
		global Length3, Shoulder3, Sleeve3, Chest3, Waist3,Hip3, Cross_Front3, Cross_Back3, Neck3, Cuff3, Arm_Round3, Ready_Frontinput
		global jacket_lapel_peak,jacket_lapel_natch,jacket_lapel_shawl,jacket_vent_no,jacket_vent_side,jacket_vent_center
		global jacket_pocket_straight,jacket_pocket_slant,jacket_pocket_patch,jacket_pocket_ticket,jacket_fit_regular,jacket_fit_slim,jacket_sleeveplacket_vent,jacket_sleeveplacket_functional
		global trouser_belt_cut,trouser_belt_long, trouser_belt_hook, trouser_belt_button, trouser_belt_square, trouser_belt_round, trouser_belt_vshape,trouser_pleat_single
		global trouser_pleat_double, trouser_pleat_flat, trouser_pocket_cross, trouser_pocket_straight, trouser_pocket_l, trouser_pocket_mobile, trouser_pocket_coin,trouser_backpocket_1
		global trouser_backpocket_2, trouser_backpocket_no, trouser_backpocket_loop, trouser_backpocket_kaaj, trouser_backpocket_flap, trouser_bottom_plain, trouser_bottom_slant, trouser_bottom_turnup
		global trouser_bottom_lining,trouser_bottom_knee, trouser_bottom_half, trouser_bottom_full, trouser_fit_regular, trouser_fit_slim, trouser_fit_tapered
		global shirt_bottom_cut, shirt_bottom_long, shirt_bottom_hook, shirt_pocket_1, shirt_pocket_2, shirt_pocket_no, shirt_pocket_v, shirt_pocket_chisel, shirt_pocket_withflap,shirt_frontpocket_plain
		global shirt_frontpocket_box, shirt_frontpocket_plainfuse, shirt_frontpocket_concealed, shirt_back_plain, shirt_back_sidepleat, shirt_back_bocpleat, shirt_back_dart


		# img = ImageTk.PhotoImage(Image.open("bt.jpg"))
		# panel = Label(mainwin, image = img)
		# panel.place(x=sizx+15,y=5)

		Length1 = StringVar()
		Sleeve1 = StringVar()
		Shoulder1 = StringVar()
		Chest1 = StringVar()
		Waist1 = StringVar()
		Hip1 = StringVar()
		Neck1 = StringVar()
		Half1 = StringVar()
		Cross_front1 = StringVar()
		Cross_back1 = StringVar()
		Bicep1 = StringVar()
		Arm1 = StringVar()

		Length2 = StringVar()
		Inseam2 = StringVar()
		Crotch2 = StringVar()
		Waist2 = StringVar()
		Hip2 = StringVar()
		Thigh2 = StringVar()
		Knee2 = StringVar()
		Bottom2 = StringVar()
		F_Low2 = StringVar()



		Length3 = StringVar()
		Sleeve3 = StringVar()
		Shoulder3 = StringVar()
		Chest3 = StringVar()
		Waist3 = StringVar()
		Hip3 = StringVar()
		Cross_Front3 = StringVar()
		Cross_Back3 = StringVar()
		Neck3 = StringVar()
		Cuff3 = StringVar()
		Arm_Round3 = StringVar()



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


		


	# def create(self,mainwin):

		sizy = -70
		sizx = 00

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
		Length11= Entry(mainwin,width=8,textvariable=Length1)
		Length11.place(x=sizx+10,y=sizy+140)

		Shoulder=Label(mainwin,text="Shoulder")
		Shoulder.place(x=sizx+70,y=sizy+100)
		Shoulder11= Entry(mainwin,width=8,textvariable=Shoulder1)
		Shoulder11.place(x=sizx+70,y=sizy+140)

		Sleeve=Label(mainwin,text="Sleeve")
		Sleeve.place(x=sizx+130,y=sizy+100)
		Length=Label(mainwin,text="Length")
		Length.place(x=sizx+130,y=sizy+115)
		Sleeve11= Entry(mainwin,width=8,textvariable=Sleeve1)
		Sleeve11.place(x=sizx+130,y=sizy+140)

		Chest=Label(mainwin,text="Chest")
		Chest.place(x=sizx+190,y=sizy+100)
		Chest11= Entry(mainwin,width=8,textvariable=Chest1)
		Chest11.place(x=sizx+190,y=sizy+140)

		Waist=Label(mainwin,text="Waist")
		Waist.place(x=sizx+250,y=sizy+100)
		Waist11= Entry(mainwin,width=8,textvariable=Waist1)
		Waist11.place(x=sizx+250,y=sizy+140)

		Hip=Label(mainwin,text="Hip")
		Hip.place(x=sizx+310,y=sizy+100)
		Hip11= Entry(mainwin,width=8,textvariable=Hip1)
		Hip11.place(x=sizx+310,y=sizy+140)

		Neck=Label(mainwin,text="Neck")
		Neck.place(x=sizx+370,y=sizy+100)
		Neck11= Entry(mainwin,width=8,textvariable=Neck1)
		Neck11.place(x=sizx+370,y=sizy+140)

		Half=Label(mainwin,text="Half")
		Half.place(x=sizx+430,y=sizy+100)
		Back=Label(mainwin,text="Back")
		Back.place(x=sizx+430,y=sizy+115)
		Half11= Entry(mainwin,width=8,textvariable=Half1)
		Half11.place(x=sizx+430,y=sizy+140)

		Cross_back=Label(mainwin,text="Cross Bk.")
		Cross_back.place(x=sizx+490,y=sizy+100)
		Cross_back11= Entry(mainwin,width=8,textvariable=Cross_back1)
		Cross_back11.place(x=sizx+490,y=sizy+140)

		Cross_front=Label(mainwin,text="Cross Fr.")
		Cross_front.place(x=sizx+550,y=sizy+100)
		Cross_front11= Entry(mainwin,width=8,textvariable=Cross_front1)
		Cross_front11.place(x=sizx+550,y=sizy+140)

		Bicep=Label(mainwin,text="Bicep")
		Bicep.place(x=sizx+610,y=sizy+100)
		Bicep11= Entry(mainwin,width=8,textvariable=Bicep1)
		Bicep11.place(x=sizx+610,y=sizy+140)

		Arm_hole=Label(mainwin,text="Arm")
		Arm_hole.place(x=sizx+670,y=sizy+85)

		Arm_hole1=Label(mainwin,text="hole")
		Arm_hole1.place(x=sizx+670,y=sizy+100)

		Round=Label(mainwin,text="Round")
		Round.place(x=sizx+670,y=sizy+115)
		Arm11= Entry(mainwin,width=8,textvariable=Arm1)
		Arm11.place(x=sizx+670,y=sizy+140)

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

		Lengthtrouser=Label(mainwin,text="Length")
		Lengthtrouser.place(x=sizx+10,y=sizy+330)
		Length22= Entry(mainwin,width=8,textvariable=Length2)
		Length22.place(x=sizx+10,y=sizy+360)

		Inseam=Label(mainwin,text="Inseam")
		Inseam.place(x=sizx+70,y=sizy+330)
		Inseam22= Entry(mainwin,width=8,textvariable=Inseam2)
		Inseam22.place(x=sizx+70,y=sizy+360)

		Crotch=Label(mainwin,text="Crotch")
		Crotch.place(x=sizx+130,y=sizy+330)
		Crotch22= Entry(mainwin,width=8,textvariable=Crotch2)
		Crotch22.place(x=sizx+130,y=sizy+360)

		Waisttrouser=Label(mainwin,text="Waist")
		Waisttrouser.place(x=sizx+190,y=sizy+330)
		Waist22= Entry(mainwin,width=8,textvariable=Waist2)
		Waist22.place(x=sizx+190,y=sizy+360)

		Hiptrouser=Label(mainwin,text="Hip")
		Hiptrouser.place(x=sizx+250,y=sizy+330)
		Hip22= Entry(mainwin,width=8,textvariable=Hip2)
		Hip22.place(x=sizx+250,y=sizy+360)

		Thigh=Label(mainwin,text="Thigh")
		Thigh.place(x=sizx+310,y=sizy+330)
		Thigh22= Entry(mainwin,width=8,textvariable=Thigh2)
		Thigh22.place(x=sizx+310,y=sizy+360)

		Knee=Label(mainwin,text="Knee")
		Knee.place(x=sizx+370,y=sizy+330)
		Knee22= Entry(mainwin,width=8,textvariable=Knee2)
		Knee22.place(x=sizx+370,y=sizy+360)

		Bottom=Label(mainwin,text="Bottom")
		Bottom.place(x=sizx+430,y=sizy+330)
		Bottom22= Entry(mainwin,width=8,textvariable=Bottom2)
		Bottom22.place(x=sizx+430,y=sizy+360)

		F_Low=Label(mainwin,text="F.Low")
		F_Low.place(x=sizx+490,y=sizy+330)
		F_Low22= Entry(mainwin,width=8,textvariable=F_Low2)
		F_Low22.place(x=sizx+490,y=sizy+360)


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

		Lengths3=Label(mainwin,text="Length")
		Lengths3.place(x=sizx+10,y=sizy+610)
		Length33= Entry(mainwin,width=8,textvariable=Length3)
		Length33.place(x=sizx+10,y=sizy+650)

		Shoulders3=Label(mainwin,text="Shoulder")
		Shoulders3.place(x=sizx+70,y=sizy+610)
		Shoulder33= Entry(mainwin,width=8,textvariable=Shoulder3)
		Shoulder33.place(x=sizx+70,y=sizy+650)

		Sleeves3=Label(mainwin,text="Sleeve")
		Sleeves3.place(x=sizx+130,y=sizy+610)
		Lengthss3=Label(mainwin,text="Length")
		Lengthss3.place(x=sizx+130,y=sizy+630)
		Sleeve33= Entry(mainwin,width=8,textvariable=Sleeve3)
		Sleeve33.place(x=sizx+130,y=sizy+650)

		Chests3=Label(mainwin,text="Chest")
		Chests3.place(x=sizx+190,y=sizy+610)
		Chest33= Entry(mainwin,width=8,textvariable=Chest3)
		Chest33.place(x=sizx+190,y=sizy+650)

		Waists3=Label(mainwin,text="Waist")
		Waists3.place(x=sizx+250,y=sizy+610)
		Waist33= Entry(mainwin,width=8,textvariable=Waist3)
		Waist33.place(x=sizx+250,y=sizy+650)

		Hips3=Label(mainwin,text="Hip")
		Hips3.place(x=sizx+310,y=sizy+610)
		Hip33= Entry(mainwin,width=8,textvariable=Hip3)
		Hip33.place(x=sizx+310,y=sizy+650)

		Cross_Fronts3=Label(mainwin,text="Cross Ft.")
		Cross_Fronts3.place(x=sizx+370,y=sizy+610)
		Cross_Front33= Entry(mainwin,width=8,textvariable=Cross_Front3)
		Cross_Front33.place(x=sizx+370,y=sizy+650)

		Cross_Backs3=Label(mainwin,text="Cross Bk.")
		Cross_Backs3.place(x=sizx+430,y=sizy+610)
		Cross_Back33= Entry(mainwin,width=8,textvariable=Cross_Back3)
		Cross_Back33.place(x=sizx+430,y=sizy+650)

		Necks3=Label(mainwin,text="Neck")
		Necks3.place(x=sizx+490,y=sizy+610)
		Neck33= Entry(mainwin,width=8,textvariable=Neck3)
		Neck33.place(x=sizx+490,y=sizy+650)

		Cuffs3=Label(mainwin,text="Cuff")
		Cuffs3.place(x=sizx+550,y=sizy+610)
		Cuff33= Entry(mainwin,width=8,textvariable=Cuff3)
		Cuff33.place(x=sizx+550,y=sizy+650)

		Arm_Rounds3=Label(mainwin,text="Arm Round")
		Arm_Rounds3.place(x=sizx+610,y=sizy+610)
		Arm_Round33= Entry(mainwin,width=8,textvariable=Arm_Round3)
		Arm_Round33.place(x=sizx+610,y=sizy+650)


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

		FrontPocket=Label(mainwin,text="Front Placket")
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


def NotifyMsg(data):
	if data['req'] == 'success':
		tkMessageBox.showinfo(data['req'],data['msg'])
	elif data['req'] == 'error' :
		tkMessageBox.showerror(data['req'],data['msg'])
	# else:
	# 	tkMessageBox.showinfo("test",data)

   # tkMessageBox.showinfo(data)
	

def messageWindow():
	win = Toplevel()
	win.title('warning')
	message = "This will delete stuff"
	Label(win, text=message).pack()
	Button(win, text='Delete', command=win.destroy).pack()

def setCustomerDetails(root):
	customer = {}
	order = {}
	notifyData = {}

	customer['name'] = cus_name.get()
	customer['address'] = cus_address.get()
	customer['email'] = cus_email.get()
	customer['mobile'] = cus_mobile.get()

	order['date_order'] = ord_date.get()
	order['date_trail'] = trail_date.get()
	order['date_delivery'] = deli_date.get()
	order['Approximate_trail_date'] = e13.get()
	order['Approximate_delivery_date'] = e14.get()
	order['grand_total'] = total_grand.get()


	rate['sherwani'] = rate_sherwani.get()
	rate['trouser'] = rate_trouser.get()
	rate['3pc'] = rate_3pc.get()
	rate['kurta'] = rate_kurta.get()
	rate['safari'] = rate_safari.get()
	rate['suit'] = rate_suit.get()
	rate['vest_jacket'] = rate_vest_jacket.get()
	rate['kurta_pyjm'] = rate_kurta_pyjm.get()
	rate['tuxedo'] = rate_tuxedo.get()
	rate['blazer_jkt'] = rate_blazer_jkt.get()
	rate['overcoat'] = rate_overcoat.get()
	rate['jodhpuri'] = rate_jodhpuri.get()
	rate['churidar'] = rate_churidar.get()
	rate['shirt'] = rate_shirt.get()
	rate['extra_charges'] = rate_extra_charges.get()

	qty['sherwani'] = qty_sherwani.get()
	qty['trouser'] = qty_trouser.get()
	qty['3pc'] = qty_3pc.get()
	qty['kurta'] = qty_kurta.get()
	qty['safari'] = qty_safari.get()
	qty['suit'] = qty_suit.get()
	qty['vest_jacket'] = qty_vest_jacket.get()
	qty['kurta_pyjm'] = qty_kurta_pyjm.get()
	qty['tuxedo'] = qty_tuxedo.get()
	qty['blazer_jkt'] = qty_blazer_jkt.get()
	qty['overcoat'] = qty_overcoat.get()
	qty['jodhpuri'] = qty_jodhpuri.get()
	qty['churidar'] = qty_churidar.get()
	qty['shirt'] = qty_shirt.get()
	qty['extra_charges'] = qty_extra_charges.get()

	total['sherwani'] = total_sherwani.get()
	total['trouser'] = total_trouser.get()
	total['3pc'] = total_3pc.get()
	total['kurta'] = total_kurta.get()
	total['safari'] = total_safari.get()
	total['suit'] = total_suit.get()
	total['vest_jacket'] = total_vest_jacket.get()
	total['kurta_pyjm'] = total_kurta_pyjm.get()
	total['tuxedo'] = total_tuxedo.get()
	total['blazer_jkt'] = total_blazer_jkt.get()
	total['overcoat'] = total_overcoat.get()
	total['jodhpuri'] = total_jodhpuri.get()
	total['churidar'] = total_churidar.get()
	total['shirt'] = total_shirt.get()
	total['extra_charges'] = total_extra_charges.get()

	jacket_measure['basic'] = {}
	jacket_measure['basic']['length'] = Length1.get()
	jacket_measure['basic']['shoulder'] = Shoulder1.get()
	jacket_measure['basic']['sleeve_length'] = Sleeve1.get()
	jacket_measure['basic']['chest'] = Chest1.get()
	jacket_measure['basic']['waist'] = Waist1.get()
	jacket_measure['basic']['hip'] = Hip1.get()
	jacket_measure['basic']['neck'] = Neck1.get()
	jacket_measure['basic']['half_back'] = Half1.get()
	jacket_measure['basic']['cross_back'] = Cross_back1.get()
	jacket_measure['basic']['cross_front'] = Cross_front1.get()
	jacket_measure['basic']['bicep'] = Bicep1.get()
	jacket_measure['basic']['arm_hole_round'] = Arm1.get()
	jacket_measure['style_details'] = {}
	jacket_measure['style_details']['style'] = style1.get("1.0",'end-1c')
	jacket_measure['style_details']['lapel'] = {}
	jacket_measure['style_details']['lapel']['peak'] = jacket_lapel_peak.get()
	jacket_measure['style_details']['lapel']['natch'] = jacket_lapel_natch.get()
	jacket_measure['style_details']['lapel']['Shawl'] = jacket_lapel_shawl.get()
	jacket_measure['style_details']['vent'] = {}
	jacket_measure['style_details']['vent']['no'] = jacket_vent_no.get()
	jacket_measure['style_details']['vent']['side'] = jacket_vent_side.get()
	jacket_measure['style_details']['vent']['center'] = jacket_vent_center.get()
	jacket_measure['style_details']['pocket'] = {}
	jacket_measure['style_details']['pocket']['straight'] = jacket_pocket_straight.get()
	jacket_measure['style_details']['pocket']['slant'] = jacket_pocket_slant.get()
	jacket_measure['style_details']['pocket']['patch'] = jacket_pocket_patch.get()
	jacket_measure['style_details']['pocket']['ticket'] = jacket_pocket_ticket.get()
	jacket_measure['style_details']['fit'] = {}
	jacket_measure['style_details']['fit']['regular'] = jacket_fit_regular.get()
	jacket_measure['style_details']['fit']['slim'] = jacket_fit_slim.get()
	jacket_measure['style_details']['sleeve_placket'] = {}
	jacket_measure['style_details']['sleeve_placket']['vent'] = jacket_sleeveplacket_vent.get()
	jacket_measure['style_details']['sleeve_placket']['functional'] = jacket_sleeveplacket_functional.get()

	trouser_measure['basic'] = {}
	trouser_measure['basic']['length'] = Length2.get()
	trouser_measure['basic']['inseam'] = Inseam2.get()
	trouser_measure['basic']['crotch'] = Crotch2.get()
	trouser_measure['basic']['waist'] = Waist2.get()
	trouser_measure['basic']['hip'] = Hip2.get()
	trouser_measure['basic']['thigh'] = Thigh2.get()
	trouser_measure['basic']['knee'] = Knee2.get()
	trouser_measure['basic']['bottom'] = Bottom2.get()
	trouser_measure['basic']['f_low'] = F_Low2.get()
	trouser_measure['style_details'] = {}
	trouser_measure['style_details']['belt'] ={}
	trouser_measure['style_details']['belt']['cut'] = trouser_belt_cut.get()
	trouser_measure['style_details']['belt']['long'] = trouser_belt_long.get()
	trouser_measure['style_details']['belt']['hook'] = trouser_belt_hook.get()
	trouser_measure['style_details']['belt']['button'] = trouser_belt_button.get()
	trouser_measure['style_details']['belt']['square'] = trouser_belt_square.get()
	trouser_measure['style_details']['belt']['round'] = trouser_belt_round.get()
	trouser_measure['style_details']['belt']['v_shape'] = trouser_belt_vshape.get()
	trouser_measure['style_details']['pleat'] = {}
	trouser_measure['style_details']['pleat']['single'] = trouser_pleat_single.get()
	trouser_measure['style_details']['pleat']['double'] = trouser_pleat_double.get()
	trouser_measure['style_details']['pleat']['flat'] = trouser_pleat_flat.get()
	trouser_measure['style_details']['pocket'] = {}
	trouser_measure['style_details']['pocket']['cross'] = trouser_pocket_cross.get()
	trouser_measure['style_details']['pocket']['straight'] = trouser_pocket_straight.get()
	trouser_measure['style_details']['pocket']['l_pocket'] = trouser_pocket_l.get()
	trouser_measure['style_details']['pocket']['mobile'] = trouser_pocket_mobile.get()
	trouser_measure['style_details']['pocket']['coin'] = trouser_pocket_coin.get()
	trouser_measure['style_details']['back_pocket'] = {}
	trouser_measure['style_details']['back_pocket']['1'] = trouser_backpocket_1.get()
	trouser_measure['style_details']['back_pocket']['2'] = trouser_backpocket_2.get()
	trouser_measure['style_details']['back_pocket']['no'] = trouser_backpocket_no.get()
	trouser_measure['style_details']['back_pocket']['loop'] = trouser_backpocket_loop.get()
	trouser_measure['style_details']['back_pocket']['kaaj'] = trouser_backpocket_kaaj.get()
	trouser_measure['style_details']['back_pocket']['flap'] = trouser_backpocket_flap.get()
	trouser_measure['style_details']['bottom'] = {}
	trouser_measure['style_details']['bottom']['plain'] = trouser_bottom_plain.get()
	trouser_measure['style_details']['bottom']['slant'] = trouser_bottom_slant.get()
	trouser_measure['style_details']['bottom']['turnup'] = trouser_bottom_turnup.get()
	trouser_measure['style_details']['lining'] = {}
	trouser_measure['style_details']['lining']['knee'] = trouser_bottom_knee.get()
	trouser_measure['style_details']['lining']['half_fb'] = trouser_bottom_half.get()
	trouser_measure['style_details']['lining']['full_fb'] = trouser_bottom_full.get()
	trouser_measure['style_details']['loops'] = Loopsinput.get('1.0','end-1c')
	trouser_measure['style_details']['size'] = Sizeinput.get('1.0','end-1c')
	trouser_measure['style_details']['fit'] = {}
	trouser_measure['style_details']['fit']['regular'] = trouser_fit_regular.get()
	trouser_measure['style_details']['fit']['slim'] = trouser_fit_slim.get()
	trouser_measure['style_details']['fit']['tapered'] = trouser_fit_tapered.get()
	

	shirt_measure['basic'] = {}
	shirt_measure['basic']['length'] = Length3.get()
	shirt_measure['basic']['shoulder'] = Shoulder3.get()
	shirt_measure['basic']['sleeve_length'] = Sleeve3.get()
	shirt_measure['basic']['chest'] = Chest3.get()
	shirt_measure['basic']['waist'] = Waist3.get()
	shirt_measure['basic']['hip'] = Hip3.get()
	shirt_measure['basic']['cross_front'] = Cross_Front3.get()
	shirt_measure['basic']['cross_back'] = Cross_Back3.get()
	shirt_measure['basic']['neck'] = Neck3.get()
	shirt_measure['basic']['cuff'] = Cuff3.get()
	shirt_measure['basic']['arm_round'] = Arm_Round3.get()
	shirt_measure['style_details'] = {}
	shirt_measure['style_details']['bottom'] = {}
	shirt_measure['style_details']['bottom']['cut'] = shirt_bottom_cut.get()
	shirt_measure['style_details']['bottom']['long'] = shirt_bottom_long.get()
	shirt_measure['style_details']['bottom']['hook'] = shirt_bottom_hook.get()
	shirt_measure['style_details']['pocket'] = {}
	shirt_measure['style_details']['pocket']['1'] = shirt_pocket_1.get()
	shirt_measure['style_details']['pocket']['2'] = shirt_pocket_2.get()
	shirt_measure['style_details']['pocket']['no'] = shirt_pocket_no.get()
	shirt_measure['style_details']['pocket']['v'] = shirt_pocket_v.get()
	shirt_measure['style_details']['pocket']['chisel'] = shirt_pocket_chisel.get()
	shirt_measure['style_details']['pocket']['with_flap'] = shirt_pocket_withflap.get()
	shirt_measure['style_details']['front_placket'] = {}
	shirt_measure['style_details']['front_placket']['plain'] = shirt_frontpocket_plain.get()
	shirt_measure['style_details']['front_placket']['box'] = shirt_frontpocket_box.get()
	shirt_measure['style_details']['front_placket']['plain_fuse'] = shirt_frontpocket_plainfuse.get()
	shirt_measure['style_details']['front_placket']['concealed'] = shirt_frontpocket_concealed.get()
	shirt_measure['style_details']['back'] = {}
	shirt_measure['style_details']['back']['side_pleat'] = shirt_back_sidepleat.get()
	shirt_measure['style_details']['back']['boc_pleat'] = shirt_back_bocpleat.get()
	shirt_measure['style_details']['back']['dart'] = shirt_back_dart.get()
	shirt_measure['style_details']['back']['plain'] = shirt_back_plain.get()
	shirt_measure['style_details']['ready_front'] = Ready_Frontinput.get('1.0','end-1c')






	if customer['name'] != '' and customer['address'] != '' and customer['mobile'] != '' :
		if order['date_order'] != '' and order['date_delivery'] != '' :
			notifyData['req'] = 'success'
		else:
			notifyData['req'] = 'error'
			notifyData['msg'] = "Order Date and Delivery Date Can't be Blank"
			NotifyMsg(notifyData)
	
	else:
		notifyData['req'] = 'error'
		notifyData['msg'] = "Name, Address and Mobile Can't be Blank"
		NotifyMsg(notifyData)



	if notifyData['req'] != 'error' and notifyData['req'] == 'success':
		customerObj = CustomerDetails()
		cusData = customerObj.setData(customer)

		if cusData['req'] == 'success' and cusData['req'] != 'error' :
			Lastid = cusData['insert_id']
			# Lastid = 0
			# NotifyMsg(cusData)

			orderObj = OrderDetails()
			ordData = orderObj.setData(order,Lastid)
			NotifyMsg(ordData)

			if ordData['req'] == 'success' and ordData['req'] != 'error':
				LastOrderId = ordData['order_id']

				billObj = BillDetails()
				billData = billObj.setData(rate, qty, total, LastOrderId)
				NotifyMsg(billData)

				jacketObj = MeasurementJacket()
				jktData = jacketObj.setData(jacket_measure['basic'],LastOrderId)
				# NotifyMsg(jktData)
				
				jacketStyleObj = MeasurementJacketStyle()
				jktStlData = jacketStyleObj.setData(jacket_measure['style_details'],LastOrderId)
				# NotifyMsg(jktData)

				shirtObj = MeasurementShirt()
				shirtData = shirtObj.setData(shirt_measure['basic'],LastOrderId)
				# NotifyMsg(shirtData)

				shirtStyleObj = MeasurementShirtStyle()
				shirtStyleData = shirtStyleObj.setData(shirt_measure['style_details'],LastOrderId) 
				# NotifyMsg(shirtStyleData)

				trouserObj = MeasurementTrouser()
				trouserData = trouserObj.setData(trouser_measure['basic'],LastOrderId)
				# NotifyMsg(trouserData)

				trouserStyleObj = MeasurementTrouserStyle()
				trouserStyleData = trouserStyleObj.setData(trouser_measure['style_details'],LastOrderId) 
				# NotifyMsg(trouserStyleData)


			# else:
				# return 
				# NotifyMsg(ordData)
		else:
			NotifyMsg(cusData)
