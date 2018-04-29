#  Beginner Exercises
# ### 1. Create these classes with the following attributes
# #### Dog
# - Two attributes:
#     - name
#     - age
# #### Person
# - Three Attributes:
#     - name
#     - age
#     - birthday (as a datetime object)
# ### 2. For the Dog object, create a method that prints to the terminal the name and age of the dog.
# - i.e.:
# ```
# Dog.introduce() ===> "Hi I am Sparky and I am 5 years old."
# ```
# ### 3. Create a function that will RETURN the Person objects birthday day of the week this year.
# - i.e.:
# ```
# Bob.birthday() ===> "Thursday"
# ```


class Dog():

	def __init__(self,name,age):
		self.name=name
		self.age=age

	def __str__(self):
		return self.name + "" + str(self.age)


class Person():

	def __init__(self,name, age, birthday):
		self.name=name
		self.age=age
		self.birthday=birthday

	def __st__(self):
		return self.name + "" + str(self.birthday)

# d = Dog("Sparky",5)
# print("the dog's name is" + self.name 

p1 = Person('Linda','11', today)


from datetime import datetime, date

today=date.today()

datetime_object = datetime.strptime('Sep 19 2017  1:33PM', '%b %d %Y %I:%M%p')

# print ("Bob's birthday is {:%b %d}".format(datetime_object) + ", which is thursday")

Kesha's Version

from datetime import datetime

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person():
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = datetime.strptime(birthday,'%m %d %Y')
        self.age = int(str(datetime.today())[:4])-int(str(self.birthday)[:4])

dave = Person('dave','12 03 1989')

print(dave.birthday)
print('Dave is {} years old!'.format(dave.age))



