'''
# File handling
file = open("filehandling.txt","w")
session = file.write(" I am learning python from RFT.")
print(session)
file.close()
'''
'''
# to remove/dlt
import os
os.remove("filehandling.txt")
print(file)
'''
'''
# Exceptional handling
try:
 num = int(input("Enter a number : "))
 result = 40/num
 print("Your result is : ",result)
except ZeroDivisionError:
 print("Enter your number except 0")
except ValueError:
 print("Enter your number except 0")
finally:
 print("code executed")
'''
'''
num = [3,4,5,6,8,9]
try:
 print(num[7])
except Exception as e:
 print("error occured,",e)
finally:
 print("Code executed")
'''