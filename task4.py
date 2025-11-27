# TASK

# 1) check if no. is positive
num1=eval(input("Enter a number : "))
if num1>=0:
    print(f"{num1} is positive")

# 2) check if no. is divisible by 2
if num1%2==0:
    print(f"{num1} is divisible by 2")

# 3) print message if age is grater than 18
if num1>=18:
    print(f" Your age is grater than 18")

# 4) check string length is grather than 5
n2 = input("Enter a string : ")
if len(n2)>5:
    print("String length is grather than 5")

# 5) check if a no. is negative
if num1<=0:
    print(f"{num1} is negative")

# 6) check is chat is vowel
if n2=="aeiouAEIOU":
    print(f"{n2} chat is vowel")

# 7) print message if no. is multiple of 10
if num1 % 10 == 0:
    print(f"{num1} is multiple of 10")
else:
    print(f"{num1} isn't multiple of 10")

# 8) check if list is not empty
l = [1,2,2]
if l==[]:
    print("list is Empty")
else:
    print("List is not empty")

# 9) print message if no. is greater than 100
if num1>100:
    print(f"{num1} is greater than 100")

# 10) check if a word contains letter "a"
if "a" in n2:
    print(f"{n2} word contain letter a")
else:
    print(f"{n2} word not contain letter a")

# 11) check if given no. is even or odd
if num1%2==0:
    print(f"{num1} is even number")
else:
    print(f"{num1} is odd number")

# 12) check eligiblity for voting
age = eval(input("Enter your age :"))
if age>=18:
    print("Eligible for voting ")
else:
    print("Not Eligible for voting ")

# 13) check if a no. if positive or negative
if num1>0:
    print("Positive")
else:
    print("negative")

# 14) Check password length
password = input("Enter your password : ")
min_length = 8
if len(password) < min_length:
    print(f"Password isn't acceptable. It must be at least {min_length} characters long.")
else:
    print("Password length is acceptable.")

# 15) check if temp is hot or cool
temp = eval(input("Enter the temperature :"))
if temp > 40:
    print("Temperature is hot")
elif temp < 20:
    print("Temperature is cool")

# 16) check if no. is divisible by 3
if num1%3==0:
    print(f"{num1} is divisible by 3")

# 17) check multiple of 3 and 4
if num1%3==0 and num1%4==0:
    print(f"{num1} multiple of 3 and 4")

# 18) give a bonus to employee according to salary
salary = eval(input("Enter Salary of employee: "))
if salary < 10000:
    bonus = 2000
    print(f"Your bonus is: {bonus}")
elif salary>=10000 and  salary<25000:
    bonus = 30000
    print(f"Your bonus is: {bonus}")
else:
    bonus = 1000
    print(f"Your bonus is: {bonus}")

# 19) classify the temperature
if temp > 40:
    print("Temperature is hot")
elif temp < 20:
    print("Temperature is cool")

# 20) determine a category base on age
if age>=18 and age<=40:
    print("Younger")
elif age<18 and age>14:
    print("Teenager")
elif age<14 and age>5:
    print("Child")
elif age<5 and age>0:
    print("Baby")
else:
    print("Older")

# 21) month number tp month name
month_no = eval(input("Enter the number of month : "))
if month_no==1:
    print(f"{month_no} is for January")
elif month_no==2:
    print(f"{month_no} is for February")
elif month_no==3:
    print(f"{month_no} is for March")
elif month_no==4:
    print(f"{month_no} is for April")
elif month_no==5:
    print(f"{month_no} is for May")
elif month_no==6:
    print(f"{month_no} is for June")
elif month_no==7:
    print(f"{month_no} is for July")
elif month_no==8:
    print(f"{month_no} is for August")
elif month_no==9:
    print(f"{month_no} is for September")
elif month_no==10:
    print(f"{month_no} is for October")
elif month_no==11:
    print(f"{month_no} is for November")
elif month_no==12:
    print(f"{month_no} is for December")
else:
    print(f"{month_no} is not valid")

# 22) check type of triangle
x = eval(input("value 1 for triangle : "))
y = eval(input("value 2 for triangle : "))
z = eval(input("value 3 for triangle : "))
if x == y == z:
    print("Equilateral Triangle")
elif x == y or y == z or z == x:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


# 23) traffic light system
light = input("Enter traffic light : ")
if light=="red"or"Red":
    print("Stop vehical")
elif light=="yellow"or"Yellow":
    print("Go Slow")
else:
    print("Go")

# 24) determine the largest of three numbers
num1 = int(input("Enter the value1 : "))
num2 = int(input("Enter the value2 : "))
num3 = int(input("Enter the value3 : "))

if num1>num2 and num1>num3:
    print(f"{num1} is grater than {num2} and {num3}")
elif num2>num1 and num2>num3:
    print(f"{num2} is grater than {num3} and {num1}")
else:
    print(f"{num3} is grater than {num2} and {num1}")
