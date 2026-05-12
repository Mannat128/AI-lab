'''
# WAP to ask the user to enter names of thier 3 fav movies 7 store them in a list
mov1 = input("Enter your 1st fav movie : ")
mov2 = input("Enter your 2nd fav movie : ")
mov3 = input("Enter your 3rd fav movie : ")
mov4 = [mov1,mov2,mov3]
print( mov4)
'''
'''
# WAP to check if a list contains a palindrome of element
num = input("ENTER A WORD ")
rev = "".join(reversed(num))
print(num)
print(rev)
if(num==rev):
    print("palindrome")
else:
    print("not palindrome")
'''
'''
# WAP to count the number of students with grade in following tuple (C,D,A,A,B,B,A)
grade = ("C","D","A","A","B","B","A")
print("Number of students got grade A : ",grade.count("A"))
print("Number of students got grade B : ",grade.count("B"))
print("Number of students got grade C : ",grade.count("C"))
print("Number of students got grade D : ",grade.count("D"))
'''
'''
# WAP to strore the above value in list & sort them from A to D
grade = ("C","D","A","A","B","B","A")
print(grade)
print(type(grade),len(grade))
grade = list(grade)
print(grade)
print(type(grade),len(grade))
grade.sort()
print(grade)

'''
#print the sum of numbers from 1 to 100