from datetime import datetime, date, timedelta
import calendar

class Dog:

	def __init__(self,name,age):
		self.name = name
		self.age = age

	def introduce(self):
		print("Hi my name is {} and I am {} years old".format(self.name,self.age))

class Person:

	def __init__(self,name,age,birthday):
		self.name = name
		self.age = age
		self.birthday = birthday

	def day_birthday(self):
		day_of_week = calendar.day_name[self.birthday.weekday()]
		return day_of_week

# def decide_weekday(number):
# 	if number == 2:
# 		print("wednesday")

today = date.today()


today += timedelta(days=2)
# print("today",today)
# print("type", type(today))
# print("dir", dir(today))

person1 = Person("John", 24, today)

dayWeek = person1.day_birthday()
print(dayWeek)




#  CLOSURE ASIDE
def add(x,y):
	num1 = x*2
	num2 = y*2
	def add_doubles():
		return num1+num2

	return add_doubles


answer = add(10,12)
print("answer", answer())











