import sqlite3 as lite
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

con = None

con = lite.connect(parentdir+'/bespoke.db')


with con:
	cur = con.cursor()
	cur.execute("PRAGMA foreign_keys = ON")

	def init():
		customer_details = "CREATE TABLE IF NOT EXISTS customer_details('uid' integer PRIMARY KEY AUTOINCREMENT,'name' varchar(100) NOT NULL,'phone' varchar(100) NOT NULL,'email' varchar(250) NOT NULL,'address' text NOT NULL)" 
		cur.execute(customer_details)
		order_details = "CREATE TABLE IF NOT EXISTS 'order_details' ('customer_id' integer NOT NULL,'order_id' integer NOT NULL PRIMARY KEY AUTOINCREMENT,'order_date' TEXT DEFAULT NULL,'trail_date' TEXT DEFAULT NULL,'delivery_date' TEXT DEFAULT NULL, 'grand_total' INTEGER NOT NULL,  FOREIGN KEY ('customer_id') REFERENCES 'customer_details' ('uid'))"
		cur.execute(order_details)
		measurement_jacket = "CREATE TABLE IF NOT EXISTS 'measurement_jacket' ('order_id' integer NOT NULL,'type' varchar(4) DEFAULT NULL,'trail_type' varchar(2) DEFAULT NULL,'length' int(11) DEFAULT NULL,'shoulder' int(11) DEFAULT NULL,'sleeve' int(11) DEFAULT NULL,'chest' int(11) DEFAULT NULL,'waist' int(11) DEFAULT NULL,'hip' int(11) DEFAULT NULL,'neck' int(11) DEFAULT NULL,'half_back' int(11) DEFAULT NULL,'cross_back' int(11) DEFAULT NULL,'cross_front' int(11) DEFAULT NULL,'bicep' int(11) DEFAULT NULL,'arm_hole_round' int(11) DEFAULT NULL,PRIMARY KEY(order_id), FOREIGN KEY ('order_id') REFERENCES 'order_details' ('order_id'))";
		cur.execute(measurement_jacket)
		measurement_jacket_style = "CREATE TABLE IF NOT EXISTS 'measurement_jacket_style' ('order_id' integer NOT NULL,'style' varchar(500) NOT NULL,'lapel' varchar(500) NOT NULL,'vent' varchar(500) NOT NULL,'pocket' varchar(500) NOT NULL,'fit' varchar(500) NOT NULL,'sleeve_placket' varchar(500) NOT NULL, PRIMARY KEY(order_id), FOREIGN KEY ('order_id') REFERENCES 'order_details' ('order_id'))"
		cur.execute(measurement_jacket_style)
		measurement_shirt = "CREATE TABLE IF NOT EXISTS 'measurement_shirt' ('order_id' integer NOT NULL, 'length' int(11) DEFAULT NULL,'shoulder' int(11) DEFAULT NULL,'sleeve' int(11) DEFAULT NULL,'chest' int(11) DEFAULT NULL,'waist' int(11) DEFAULT NULL,'hip' int(11) DEFAULT NULL,'cross_front' int(11) DEFAULT NULL,'cross_back' int(11) DEFAULT NULL,'neck' int(11) DEFAULT NULL,'cuff' int(11) DEFAULT NULL,'arm_round' int(11) DEFAULT NULL, PRIMARY KEY(order_id), FOREIGN KEY ('order_id') REFERENCES 'order_details' ('order_id'))"
		cur.execute(measurement_shirt)
		measurement_shirt_style = "CREATE TABLE IF NOT EXISTS 'measurement_shirt_style' ('order_id' integer NOT NULL ,'bottom' varchar(500) NOT NULL,'pocket' varchar(500) NOT NULL,'front_placket' varchar(500) NOT NULL,'back' varchar(500) NOT NULL,'ready_front' varchar(500) NOT NULL, PRIMARY KEY(order_id), FOREIGN KEY ('order_id') REFERENCES 'order_details' ('order_id'))"
		cur.execute(measurement_shirt_style)
		measurement_trouser = "CREATE TABLE IF NOT EXISTS 'measurement_trouser' ('order_id' integer NOT NULL ,'length' int(11) DEFAULT NULL,'inseam' int(11) DEFAULT NULL,'crotch' int(11) DEFAULT NULL,'waist' int(11) DEFAULT NULL,'hip' int(11) DEFAULT NULL,'thigh' int(11) DEFAULT NULL,'knee' int(11) DEFAULT NULL,'bottom' int(11) DEFAULT NULL,'f_low' int(11) DEFAULT NULL,'type' varchar(10) DEFAULT NULL, PRIMARY KEY(order_id), FOREIGN KEY ('order_id') REFERENCES 'order_details' ('order_id'))"
		cur.execute(measurement_trouser)
		measurement_trouser_style = "CREATE TABLE IF NOT EXISTS 'measurement_trouser_style' ('order_id' integer NOT NULL ,'belt' varchar(500) NOT NULL,'pleat' varchar(500) NOT NULL,'pocket' varchar(500) NOT NULL,'back_pocket' varchar(500) NOT NULL,'bottom' varchar(500) NOT NULL,'loops' varchar(500) NOT NULL,'fit' varchar(500) NOT NULL,'size' varchar(500) NOT NULL,'lining' varchar(500) NOT NULL, PRIMARY KEY(order_id), FOREIGN KEY ('order_id') REFERENCES 'order_details' ('order_id'))"
		cur.execute(measurement_trouser_style)
		bill_details = "CREATE TABLE IF NOT EXISTS 'bill_details' ('order_id' integer NOT NULL, 'name' varchar(100) NOT NULL, 'rate' integer DEFAULT NULL, 'qty' integer DEFAULT NULL, 'sub_total' integer DEFAULT NULL, FOREIGN KEY ('order_id') REFERENCES 'order_details' ('order_id'))"
		cur.execute(bill_details)		
	init()
