''' 
# find grade of a student
marks = float(input("Enter your marks : "))
if(marks>=80):
    print("Grade A ")
elif(marks>=60 and marks<80):
    print("Grade B")
elif(marks>=50 and marks<60):
    print("Grade C")
elif(marks>=30 and marks<50):
    print("Grade D ")
else:
    print("Fail")

'''
'''
#Typecasting
a = "6"
b = "4"
c = float(b)
print(type(a))
print(float(b))
print(type(c))
'''
'''
#String
school_name = "Modern public school"
print(school_name[7:13])

'''
'''
school_name = "Modern public school"
for i in school_name :
    print(i)
    '''
'''
#list 
students_name = ["Mannat","Anjali","Amarjot","Satnam","Navjot","Mannat"]
print(students_name)
students_name[5]="Megha" 
students_name.insert(2,"Harsh")
students_name.remove("Mannat")
students_name.pop()
print(students_name)
print(type(students_name))
print(len(students_name))
'''
'''
#tuple
dep = ("cse","cse","bpt","ece","ba",12,13)
print(dep)
print(type(dep))
print(len(dep))
'''
'''
#set
roll_no = {1,2,3,4,5,6,2,"nine",11.2}
print(len(roll_no))
print(type(roll_no))
print(roll_no)
roll_no.add("eight")
roll_no.remove(2)
print(roll_no)
'''
'''
#list with diff email,also have duplicate mail,only print unique mail
id = ["mannat@gmail.com","harsh@gmail.com","priya@gmail.com","deep@gmail.com","mannat@gmail.com"]
print(id)
print((set(id)))
'''
'''
#dictionary
student_data = {"Name":"Mannat","id":"101","sem":"6th"}
print(type(student_data))
print(len(student_data))

student_data["class"]="b.tech"
print(student_data)
del student_data["class"]
print(student_data)
'''

#function
