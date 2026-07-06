from collections import namedtuple, defaultdict
import json 

Student = namedtuple('Student', ['Name', 'Class', 'Age', 'SchoolName'])

student_database = defaultdict(list)
# restored_database = defaultdict(list)
# add_students = list()
# s1 = Student('monica', 4,'9','gvm school system')
# s2 = Student('isha', 5,'11','damd public school')
# s3 = Student('jaqualine', 4,'11','md school system')

# all_students.append(s1)
# all_students.append(s2)
# all_students.append(s3)
# for s in all_students:
#     student_dict = s._asdict() 
#     student_database[s.Class].append(student_dict)
# print(student_database)
# print(student_dict) i have to use thiis

with open('JSON_storage_engine.json', 'r') as f:
    data = json.load(f)
             
for class_id in data:
    student_list = data[class_id]
    for student_dict in student_list:
        s = Student(**student_dict)
        student_database[int(class_id)].append(s)
# print(restored_database)
# CRUD create,read,update,del
def add_student(name,Class,age,schname):
    s = Student(name,Class,age,schname)
    student_dict = s._asdict() 
    student_database[s.Class].append(student_dict)
    


with open('JSON_storage_engine.json', 'w') as f:
    json.dump(student_database, f, indent=2)

def find_student(Class,name):
    for s in student_database[Class]:
        if name == s['Name']:
            print(s)
            return
    print("Student not found")


# find_student(5,"isha")
print("----STUDENT STORAGE----")
while True:
    print("1. Add student")
    print("2. Search student")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3)\n"))
    if choice == 1:
        name = input("Enter name: ")
        Class = int(input("Enter class: "))  # Convert to int for your database key!
        age = input("Enter age: ")
        schname = input("Enter school: ")

        add_student(name, Class,age,schname)

        with open('JSON_storage_engine.json','w') as f:
            json.dump(student_database, f, indent=2)
        print("Saved successfully")

    elif choice == 2:
        Class = int(input("Enter class to search in: "))
        name = input("Enter student name to find: ")

        find_student(Class, name)

    elif choice == 3:
        print("GOODBYEE")
        break
