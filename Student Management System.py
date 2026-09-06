from rich.console import Console
from rich.panel import Panel
console=Console()
console.print(
    Panel.fit(
        "Student Management System🎓",
            title="Welcome",
            style="bold cyan"
    )
)
def Name():
    while True:
        name=input("Enter student fullname:")
        if name.replace("","").isalpha():
            return name
        else:
            print("❌Name must be alphabet.!")
def Age(text):
    while True:
        try:
            age=int(input(text))
            if 1<= age <=120:
                return age
            else:
                print("❌Age must be between 1 to 120")
        except ValueError:
            print("❌Age must be number.!")
def ID(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("❌Student's ID isn't true.!")
def Class(text):
    while True:
        Class=input("Enter the name of student's class:")
        if Class.isalnum():
            return Class
        else:
            print("❌The name of class isn't true")
def Score(text):
    while True:
        try:
            score=float(input(text))
            if 0 <= score <= 100:
                return score
            else:
                print("❌Score must be between 0 to 100.!")
        except ValueError:
            print("❌Please write a vaild answer.!")
def Average(Math,English,Science):
    return (Math+ English+ Science)/3
def Grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
def Status(average):
    if average >= 60:
        return "PASS✔"
    else:
        return "FAIL⭕"
def Y_N():
    while True:
        again=input("Do you want to enter information of new student? (yes/no)").strip().lower()
        if again in ["yes","no"]:
            return again
        else:
            print("❌Please Just enter Yes or No.!")
def Save(name,age,id,student_class,Math,English,Science,average,grade,status):
    with open("students.txt","a",encoding="utf-8")as file:
        file.write("/" *40 +"\n")
        file.write(f"Name:{name}\n")
        file.write(f"Age:{age}\n")
        file.write(f"Id:{id}\n")
        file.write(f"Student_Class:{student_class}\n")
        file.write(f"Math:{Math}\n")
        file.write(f"English:{English}\n")
        file.write(f"Science:{Science}\n")
        file.write(f"Average:{average}\n")
        file.write(f"Grade:{grade}\n")
        file.write(f"Status:{status}\n")
        file.write("/" *40 +"\n\n")
def Student(students,name,age,id,student_class,Math,English,Science,average,grade,status,):
    student={
        "Name":name,
        "Age":age,
        "Id":id,
        "Student_class":student_class,
        "Math":Math,
        "English":English,
        "Science":Science,
        "Average":average,
        "Grade":grade,
        "Status":status
    }
    students.append(student)
students=[]
repet="yes"
while repet=="yes":
    name=Name()
    age=Age("Enter student's age:")
    id=ID("Enter student's ID:")
    student_class=Class("Enter student's class:")
    Math=Score("Enter student's Math score:")
    English=Score("Enter student's English score:")
    Science=Score("Enter student's Science score:")
    average=Average(Math,English,Science)
    grade=Grade(average)
    status=Status(average)
    
    Student(students,name,age,id,student_class,Math,English,Science,average,grade,status,)
    Save(name,age,id,student_class,Math,English,Science,average,grade,status)
    repet=Y_N()
    if repet=="no":
        break
print("\n//// ALL STUDENTS ////")
print("Tatal students:",len(students))
Pass=0
Fail=0
for student in students:
    if student["Status"].upper().startswith("PASS"):
        Pass+=1
    else:
        Fail+=1
print("Passed student:",Pass)
print("Failed student:",Fail)
print("\n//// STUDENTS INFOMATION ////")
for student in students:
    print("-"*30)
    print("Name:",student["Name"])
    print("Age:",student["Age"])
    print("ID:",student["Id"])
    print("Class:",student["Student_class"])
    print("Math:",student["Math"])
    print("English:",student["English"])
    print("Science:",student["Science"])
    print("Average:",student["Average"])
    print("Grade:",student["Grade"])
    print("Status:",student["Status"])
print("\n//// STUDENTS STATUS ////")
BestStudents=students[0]
for student in students:
    if student["Average"]> BestStudents["Average"]:
        BestStudents=student
print("Top student:",BestStudents["Name"])
print("Highest average:",BestStudents["Average"])
WorstStudent=students[0]
for student in students:
    if student["Average"]< WorstStudent["Average"]:
        WorstStudent=student
print("Weakest student:",WorstStudent["Name"])
print("Lowest average:",WorstStudent["Average"])
from rich.console import Console
from rich.panel import Panel
console=Console()
console.print(
    Panel.fit(
        "PROGRAM FINSHED✅,\nALL STUDENTS SAVED💾",
              title="STATUS",
              style="bold cyan"
    )
)