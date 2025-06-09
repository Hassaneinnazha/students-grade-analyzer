
# Write a python program to enter students' names and grades (out of 100) (the number of students should be decided by the user) and the program will do the following:
# 1- Prints students names and grades
# 2- Prints the average grade of the class
# 3- Prints the highest grade earned (Student name and grade)
# 4- Prints the count of students who passed (grade >= 60)

# You have to use loops, lists and functions.
# Your code should have the following functions `display_student_summary`, `get_avg_grade`, `get_heighest_grade`, `count_passed`

def display_student_summary(names,grades):
    i=0
    while i<len(names):
        print(names[i],grades[i])
        i+=1


def get_avg_grade(grades):
    i=0
    total=0
    while i<len(grades):
        total +=grades[i]
        i+=1
        if len(grades) == 0:
         return 0
    return total / len(grades)

def get_heighest_grade(names,grades):
    if len(grades) == 0:  
        return None
    i=0
    high_grade=grades[0]
    high_name=names[0]
    while i<len(grades):
     if grades[i]>high_grade:
         high_grade=grades[i]
         high_name=names[i]
     i+=1
    return high_name,high_grade
     
def count_passed(grades):
    count =0
    i=0
    while i<len(grades):
      if grade>=60:
         count+=1
      else: 
         print("sorry you didn't pass")
      i+=1
    return count
        
grades=[]
names=[]
num=int(input("enter the number of students: "))

i=0
while i<num:
    name=input("Enter student's names: ")
    grade=float(input("Enter student's grades (out of 100): "))
    names.append(name)
    grades.append(grade)
    i+=1
st=display_student_summary(names,grades)
print(st)
average=get_avg_grade(grades)
print("The average of class is: ",average)
hg=get_heighest_grade(names,grades)
print("The highest grades in class is: ",hg)
ct=count_passed(grades)
print("The students who are passed:",ct)
