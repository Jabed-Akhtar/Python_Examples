from Student import Student

student1 = Student("Jabed Akhtar", "Mechatronics", 2.5)
student2 = Student("Samir Khan", "Bauingeneer", 1.5)
student3 = Student("Sadam Dilwale", "Civil", 2.9)
student4 = Student("Jamil Akhtar", "Informatics", 2.7)
student5 = Student("Jibril Miya", "Maschinenbau", 3.2)

# saving file with list of students
students_file = open("students.txt","w")
students_file.write(student1.name + " - " + student1.major + " - " + str(student1.gpa))
students_file = open("students.txt","a")
students_file.write("\n" + student2.name + " - " + student2.major + " - " + str(student2.gpa))
students_file = open("students.txt","a")
students_file.write("\n" + student3.name + " - " + student3.major + " - " + str(student3.gpa))
students_file = open("students.txt","a")
students_file.write("\n" + student4.name + " - " + student4.major + " - " + str(student4.gpa))
students_file = open("students.txt","a")
students_file.write("\n" + student5.name + " - " + student5.major + " - " + str(student5.gpa))

# printing
print(student1.name)

