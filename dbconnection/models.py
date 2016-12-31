import sqlite3 as lite
import sqlite_init
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
# sys.path.insert(0,parentdir) 

# print parentdir
global returnData
returnData = {}
class CustomerDetails(object):
	"""docstring for CustomerDetails"""
	def __init__(self):
		super(CustomerDetails, self).__init__()
		
	def setData(self,data):
		con = None
		con = lite.connect(parentdir+'/bespoke.db')
		with con:
			cur = con.cursor()
			cur.execute("PRAGMA foreign_keys = ON")

			name2 = str(data['name'])
			phone2 = str(data['mobile'])
			email2 = str(data['email'])
			address2 = str(data['address'])

			try:
				sql = '''SELECT uid from customer_details WHERE name = ? and phone = ? '''
				selectData = (name2,phone2)
				cur.execute(sql,selectData)
				rows = cur.fetchone()
				if type(rows) is list and len(rows) > 0 :
					con.commit()
					returnData['insert_id'] = rows[0]
					returnData['msg'] = "Already Registered Customer"
					returnData['req'] = 'success'
					return returnData

				else:
					sql = '''INSERT INTO customer_details(name,phone,email,address) VALUES(?,?,?,?);'''
					insertData = (name2,phone2,email2,address2)

					cur.execute(sql,insertData)
					cur.execute("SELECT last_insert_rowid()")

					rows = cur.fetchone()
					con.commit()
					
					returnData['req'] = 'success'
					returnData['insert_id'] = rows[0]
					returnData['msg'] = "Successfully Added"
					return returnData

			except lite.Error, e:
				# raise e
				returnData['req'] = 'error'
				returnData['msg'] = "customer Not Added. " + e.args[0]
				return returnData
				
			
class OrderDetails(object):
	"""docstring for OrderDetails"""
	def __init__(self):
		super(OrderDetails, self).__init__()
		# self.arg = arg
	def setData(self,data,uid):
		con = None
		con = lite.connect(parentdir+'/bespoke.db')
		with con:
			cur = con.cursor()
			cur.execute("PRAGMA foreign_keys = ON")

			customer_id = str(uid)
			date_order = str(data['date_order'])
			date_trail = str(data['date_trail'])
			date_delivery = str(data['date_delivery'])
			appxTrail = str(data['Approximate_trail_date'])
			appxDelivery = str(data['Approximate_delivery_date'])


			try:

				sql = '''INSERT INTO order_details(customer_id, order_date, trail_date, delivery_date) VALUES(?,?,?,?);'''
				insertData = (customer_id, date_order, date_trail, date_delivery)

				cur.execute(sql,insertData)
				cur.execute("SELECT last_insert_rowid()")

				rows = cur.fetchone()
				con.commit()
				
				returnData['req'] = 'success'
				returnData['order_id'] = rows[0]
				returnData['msg'] = "Date Successfully Added"
				return returnData

			except lite.Error, e:
				# raise e
				returnData['req'] = 'error'
				returnData['msg'] = "date Not Added. " + e.args[0]
				return returnData




class MeasurementJacket(object):
	"""docstring for MeasurementJacket"""
	def __init__(self):
		super(MeasurementJacket, self).__init__()
		# self.arg = arg
	def setData(self,data,uid):
		con = None
		con = lite.connect(parentdir+'/bespoke.db')
		with con:
			cur = con.cursor()
			cur.execute("PRAGMA foreign_keys = ON")

			order_id = str(uid)
			length = str(data['length'])
			shoulder = str(data['shoulder'])
			sleeve = str(data['sleeve_length'])
			chest = str(data['chest'])
			waist = str(data['waist'])
			hip = str(data['hip'])
			neck = str(data['neck'])
			half_back = str(data['half_back'])
			cross_back = str(data['cross_back'])
			cross_front = str(data['cross_front'])
			bicep = str(data['bicep'])
			arm_hole_round = str(data['arm_hole_round'])

			sql = '''INSERT INTO measurement_jacket(order_id,length,shoulder,sleeve, chest, waist, hip, neck, half_back, cross_back, cross_front, bicep, arm_hole_round ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);'''
			insertData = (order_id,length,shoulder,sleeve,chest,waist,hip,neck,half_back,cross_back, cross_front,bicep,arm_hole_round )

			try:
				cur.execute(sql,insertData)
				con.commit()
				
				returnData['req'] = 'success'
				returnData['order_id'] = order_id
				returnData['msg'] = "Jacket Basic Measurement Successfully Added"
				return returnData

			except lite.Error, e:
				# raise e
				returnData['req'] = 'error'
				returnData['msg'] = "Jacket Basic Measurement Not Added. " + e.args[0]
				return returnData


class MeasurementJacketStyle(object):
	"""docstring for MeasurementJacketStyle"""
	def __init__(self):
		super(MeasurementJacketStyle, self).__init__()
		# self.arg = arg

	def setData(self,data,order_id):
		style = str(data['style'])
		lapel = str(data['lapel'])
		vent = str(data['vent'])
		pocket = str(data['pocket'])
		fit = str(data['fit'])
		sleeve_placket = str(data['sleeve_placket'])

		con = None
		con = lite.connect(parentdir+'/bespoke.db')
		with con:
			cur = con.cursor()
			cur.execute("PRAGMA foreign_keys = ON")

			try:
				sql = '''INSERT INTO measurement_jacket_style(order_id, style, lapel, vent, pocket, fit, sleeve_placket) VALUES(?,?,?,?,?,?,?) '''
				insertData = (order_id, style, lapel, vent, pocket, fit, sleeve_placket)
				cur.execute(sql,insertData)
				con.commit()
				
				returnData['req'] = 'success'
				returnData['order_id'] = order_id
				returnData['msg'] = "Jacket Style Measurement Successfully Added"
				return returnData

			except lite.Error, e:
				# raise e
				returnData['req'] = 'error'
				returnData['msg'] = "Jacket Style Measurement Not Added. " + e.args[0]
				return returnData




class MeasurementShirt(object):
	"""docstring for MeasurementShirt"""
	def __init__(self):
		super(MeasurementShirt, self).__init__()
		# self.arg = arg

	def setData(self,data,order_id):
		length = data['length']
		shoulder = data['shoulder']
		sleeve_length = data['sleeve_length']
		chest = data['chest']
		waist = data['waist']
		hip = data['hip']
		cross_front = data['cross_front']
		cross_back = data['cross_back']
		cuff = data['cuff']
		arm_round = data['arm_round']

		con = None
		con = lite.connect(parentdir+'/bespoke.db')
		with con:
			cur = con.cursor()
			cur.execute("PRAGMA foreign_keys = ON")

			try:
				sql = '''INSERT INTO measurement_shirt(order_id, length, shoulder, sleeve, chest, waist, hip, cross_front, cross_back, cuff, arm_round ) VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
				insertData = (order_id, length, shoulder, sleeve_length, chest, waist, hip, cross_front, cross_back, cuff, arm_round )
				cur.execute(sql,insertData)
				con.commit()
				
				returnData['req'] = 'success'
				returnData['order_id'] = order_id
				returnData['msg'] = "Shirt Measurement Successfully Added"
				return returnData

			except lite.Error, e:
				# raise e
				returnData['req'] = 'error'
				returnData['msg'] = "Shirt Measurement Not Added. " + e.args[0]
				return returnData



class MeasurementShirtStyle(object):
	"""docstring for MeasurementShirtStyle"""
	def __init__(self):
		super(MeasurementShirtStyle, self).__init__()
		# self.arg = arg

	def setData(self,data,order_id):
		bottom = str(data['bottom'])
		pocket = str(data['pocket'])
		front_placket = str(data['front_placket'])
		back = str(data['back'])
		ready_front = str(data['ready_front'])

		con = None
		con = lite.connect(parentdir+'/bespoke.db')
		with con:
			cur = con.cursor()
			cur.execute("PRAGMA foreign_keys = ON")

			try:
				sql = '''INSERT INTO measurement_shirt_style(order_id, bottom, pocket, front_placket, back, ready_front ) VALUES(?,?,?,?,?,?) '''
				insertData = (order_id, bottom, pocket, front_placket, back, ready_front )
				cur.execute(sql,insertData)
				con.commit()
				
				returnData['req'] = 'success'
				returnData['order_id'] = order_id
				returnData['msg'] = "Shirt Style Measurement Successfully Added"
				return returnData

			except lite.Error, e:
				# raise e
				returnData['req'] = 'error'
				returnData['msg'] = "Shirt Style Measurement Not Added. " + e.args[0]
				return returnData





class MeasurementTrouser(object):
	"""docstring for MeasurementTrouser"""
	def __init__(self):
		super(MeasurementTrouser, self).__init__()
		# self.arg = arg

	def setData(self,data,order_id):
		length 	= str(data['length'])
		inseam 	= str(data['inseam'])
		crotch 	= str(data['crotch'])
		waist 	= str(data['waist'])
		hip 	= str(data['hip'])
		thigh	= str(data['thigh'])
		knee	= str(data['knee'])
		bottom	= str(data['bottom'])
		f_low	= str(data['f_low'])

		con = None
		con = lite.connect(parentdir+'/bespoke.db')
		with con:
			cur = con.cursor()
			cur.execute("PRAGMA foreign_keys = ON")

			try:
				sql = '''INSERT INTO measurement_trouser(order_id, length, inseam, crotch, waist, hip, thigh, knee, bottom, f_low ) VALUES(?,?,?,?,?,?,?,?,?,?) '''
				insertData = (order_id, length, inseam, crotch, waist, hip, thigh, knee, bottom, f_low )
				cur.execute(sql,insertData)
				con.commit()
				
				returnData['req'] = 'success'
				returnData['order_id'] = order_id
				returnData['msg'] = "Trouser Measurement Successfully Added"
				return returnData

			except lite.Error, e:
				# raise e
				returnData['req'] = 'error'
				returnData['msg'] = "Trouser Measurement Not Added. " + e.args[0]
				return returnData




class MeasurementTrouserStyle(object):
	"""docstring for MeasurementTrouserStyle"""
	def __init__(self):
		super(MeasurementTrouserStyle, self).__init__()
		# self.arg = arg

	def setData(self,data,order_id):
		belt		=	str(data['belt'])
		pleat 		=	str(data['pleat'])
		pocket 		=	str(data['pocket'])
		back_pocket	=	str(data['back_pocket'])
		bottom		=	str(data['bottom'])
		loops		=	str(data['loops'])
		fit			=	str(data['fit'])
		size 		=	str(data['size'])
		lining		=	str(data['lining'])

		con = None
		con = lite.connect(parentdir+'/bespoke.db')
		with con:
			cur = con.cursor()
			cur.execute("PRAGMA foreign_keys = ON")

			try:
				sql = '''INSERT INTO measurement_trouser_style(order_id, belt, pleat, pocket, back_pocket, bottom, loops, fit, size, lining ) VALUES(?,?,?,?,?,?,?,?,?,?) '''
				insertData = (order_id, belt, pleat, pocket, back_pocket, bottom, loops, fit, size, lining )
				cur.execute(sql,insertData)
				con.commit()
				
				returnData['req'] = 'success'
				returnData['order_id'] = order_id
				returnData['msg'] = "Trouser Style Measurement Successfully Added"
				return returnData

			except lite.Error, e:
				# raise e
				returnData['req'] = 'error'
				returnData['msg'] = "Trouser Style Measurement Not Added. " + e.args[0]
				return returnData


