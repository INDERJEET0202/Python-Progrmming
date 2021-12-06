class Student:
    def __init__(self, first, last, course = None):
        self.first_name = first
        self.last_name = last
        if(course == None):
            self.course = []
        else:
            self.course = course

    def add_course(self, course):
        if course not in self.course:
            self.course.append(course)
        else:
            print(f"{self.first_name} is already enrolled in {course} course")

    def remove_course(self, course):
        if course in self.course:
            self.course.remove(course)
        else:
            print(f"{self.first_name} is not enrolled in {course} course")

    def __len__(self):
        return len(self.course)

    def __repr__(self):
        return f"Student ('{self.first_name.capitalize()}', '{self.last_name.capitalize()}', {self.course})"

    def __str__(self):
        return f" First name: {self.first_name.capitalize()}\n Last name: {self.last_name.capitalize()} \n Courses: {', '.join(map(str.capitalize, self.course))}"

course_1 = ['python', 'java', 'c++']
course_2 = ['java', 'c', 'rails']
indrajit = Student('Indrajit', 'Pal', course_1)
indrajit.add_course('rails')
# indrajit.add_course('rails') # This will not add rails course as it is already in the list

john = Student('John', 'Doe', course_2)
john.remove_course('c')
john.remove_course('c')

# print(indrajit.first_name, indrajit.last_name, indrajit.course)
print(indrajit)
# print(dir(indrajit))
print(repr(indrajit))
# print(john.first_name, john.last_name, john.course)