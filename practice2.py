'''
# WAP to that check  whether a number is even or odd
num = int(input("Enter a number : "))
if(num%2==0):
    print("The given number is even ")
else:
    ("The given number is odd")
'''
'''
# Take 2 num from user and print greater one
num1 = int(input("Enter a 1st number : "))
num2 = int(input("Enter a 2nd number : "))
if(num1>num2):
    print("1st number is greatest i.e : ",num1)
else:
    print("2nd number is greatest i.e : ",num2)
'''
'''
# Find the factorial of a number
num = 5
factorial = 1
while(num>1):
    factorial = factorial*num
    num = num-1
print("The factorial of given number is : ",factorial)
'''

#  WAP to print a fibonnic num
num = int(input("Enter a number : "))
reeta = 0
sona = 1
if(num==0):
    print(reeta)
else:
    for i in range(num):
        alpha = reeta+sona
        print(reeta)
        reeta,sona = sona,alpha
    