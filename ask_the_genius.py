'''
DAILY TRACKER

dato - tidspunkt??
maskine / tid / længde / kcal
vægt / BMI
kost / vand / humør
skridttæller

'''

import time
import sqlite3
import datetime


class Health(object):
	def __init__(self):
		self.date = str(datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S'))
		
		self.month = self.today()[0]
		self.day = self.today()[1]


		self.connection = sqlite3.connect("Database.db")
		self.cursor = self.connection.cursor()
		
		self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.month}(Day INT, Machine TEXT, Time INT, Distance REAL, Kcal INT)")


	def today(self):
		months = {"01": "Januar", "02": "Februar",
				"03": "Marts", "04": "April",
				"05": "May", "06": "Juni",
				"07": "Juli", "08": "August",
				"09": "September", "10": "Oktober",
				"11": "November", "12": "December"}
		date, time = self.date.split()
		month = months[date.split("-")[1]]
		day = self.date.split("-")[0]
		return month, day
	
	
	def log(self):
		day = self.day
		machine = input("Enter Machine: ")
		time = int(input("Enter time in minutes: "))
		distance = float(input("Enter distance in kilometre: "))
		kcal = int(input("Enter kcal: "))
		
		self.cursor.execute(f"INSERT INTO {self.month}(Day, Machine, Time, Distance, Kcal) VALUES(?,?,?,?,?)",(day, machine, time, distance, kcal))
		self.connection.commit()
		print("DATA LOGGED!!")
		self.cursor.close()
		self.connection.close()


if __name__ == "__main__":
	func = Health()
	func.log()
	
