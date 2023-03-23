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

    def add_to_file(self,filename):
        if self.find_in_file(filename):
            return "Record already exists"
        else:
            record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.course)
            with open(filename, "a+") as to_write:
                to_write.write(record_to_add)
                return "Record added"
    
    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name + "," + last_name
        courses = ",".join(courses)
        return full_name + ":" + courses + "\n"

    def find_in_file(self, filename):
        with open(filename, "r") as to_read:
            for line in to_read:
                if line.strip() == Student.prep_to_write(self.first_name, self.last_name, self.course):
                    return True
        return False


class StudentAthlete(Student):
    def __init__(self, first, last, course = None, sport = None):
        super().__init__(first, last, course)
        self.sport = sport

file_name = "OOP/data.txt"
course_1 = ['python', 'java', 'c++']
course_2 = ['java', 'c', 'rails']
indrajit = Student('Indrajit', 'Pal', course_1)
indrajit.add_course('rails')
# indrajit.add_course('rails') # This will not add rails course as it is already in the list

# john = Student('John', 'Doe', course_2)
# john.remove_course('c') # This will not remove c course as it is not in the list
# john.remove_course('c')

print(indrajit.first_name, indrajit.last_name, indrajit.course)
print(indrajit.add_to_file(file_name))
# print(dir(indrajit))
# print(repr(indrajit))
# print(john.first_name, john.last_name, john.course)

joe = Student("joe", "schmo", ["python", "ruby", "javascript"])
# print(joe.add_to_file(file_name))


#Inheritance
jane = StudentAthlete("Jane", "Doe", ["python", "ruby", "javascript"], "swimming")
print(jane.sport)
print(isinstance(jane, StudentAthlete))