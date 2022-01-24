def hello():
	print("hello")

x = 1
# print(type(hello)) # Class type -> function

string = "hello"
# print(string.upper()) #Methods...

#------------------------------------#

class Dog:
	def __init__(self, name, age): #everytime any instance of Dog is created this method will run automatically
		self.name = name
		# print(name)
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_age(self, age):
		self.age = age

	# def add_one(self, x):
	# 	return x+1

	# def bark(self):
	# 	print("Barking...")

# huskey = Dog("Meeka", 8)
# huskey.set_age(10)
# print(huskey.name)
# print(huskey.get_age())

# siberian_huskey = Dog("Kakoa", 4)
# print(siberian_huskey.name)
# print(siberian_huskey.get_age())

# print(type(d))
# d.bark()
# print(d.add_one(5))

#---------------------------------------#



class Student:
	def __init__(self, name, age, grade):
		self.name = name
		self.age = age
		self.grade = grade #0 - 100

	def get_grade(self):
		return self.grade #Display grade of student

class Course:
	def __init__(self, name, max_students):
		self.name = name
		self.max_students = max_students
		self.students = []

	def add_student(self, student):
		if(len(self.students) < self.max_students):
			self.students.append(student)
			return True
		return False

	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()

		return value / len(self.students)

s1 = Student("Indrajit", 20, 95)
s2 = Student("Rohan", 20, 75)
s3 = Student("Joe", 20, 65)

# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.add_student(s3))
# print(course.get_average_grade())

#--------------------------------------------------#



# Inheritance

class Pet: #Parent Class
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years Old")

	def speak(self):
		print("I don't know that I say")

class Cat(Pet):
	def __init__(self, name, age, color):
		super().__init__(name, age) #super() is used to call the parent class constructor
		self.color = color

	def speak(self):
		print("Meow")

	def show(self):
		print(f"I am {self.name} and I am {self.age} years Old and my Color is {self.color}")

class Dog(Pet):
	# def __init__(self, name, age):
	# 	self.name = name 
	# 	self.age = age 

	def speak(self): # clild class / derived class
		print("Bark")

class Fish(Pet):
	pass

# p = Pet("Kakoa", 4)
# p.speak()
# c = Cat("Bill", 10, "Brown")
# c.show()
# d =Dog("Tomy", 15)
# d.speak()
# f = Fish("Bubbles", 1)
# f.speak()

#--------------------------------------------------#



# Class Attributes


class Person:
	number_of_people = 0
	GRAVITY = -9.8

	def __init__(self, name):
		self.name = name
		# Person.number_of_people += 1
		Person.add_person()

	@classmethod #classmethods act on the class itself and not have any access to any instance
	def number_of_puipl(cls):
		return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people += 1 

# p1 = Person("Indrajit")
# p2 = Person("Joe")
# # Person.add_person()
# print(Person.number_of_puipl())
#--------------------------------------------------#


# Static Methods

class Math:

	@staticmethod
	def add5(x):
		return x+5

	@staticmethod
	def add10(x):
		return x+10

	@staticmethod
	def pr():
		print("Run")

print(Math.add10(5))
Math.pr()