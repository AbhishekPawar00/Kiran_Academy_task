# CFS

# Iterative Statement
# 1) for loop, 2) while loop

# import keyword
# print(keyword.kwlist)

# FOR loop

for i in range(1,6):
    print(i)
    print("*"*i) #ex 1

cars = ["BMW","Audi","Farari"]
for c in cars:
    print(c) # ex 2

# print each char, from a string

s = "Python"

for a in s:
    print(a)

# list of no. print only even no
n = [10,21,4,15,66]

for b in n:
    if b%2==0:
        print(b)

# print index no. in list
colour = ["red",'green',"yellow","blue","white"]
c = 0

for i in (colour):
    print(c, colour[c])
    c+=1

for i in range(len(colour)):
    print(i,colour[i])


# sum of number 1 to 10
sum=0
for i in range(0,11):
    sum+=i
print(sum)

# iterate a tuple
t = (1,2,3)
for i in t:
    print(i)

# iterate a dict.keys
dict = {"a":1,"b":2}
for d in dict:
    print(d)

# iterate dict key and value
for f in dict.items():
    print(f) # eg1

for d,f in dict.items():
    print(d," = ",f) # eg2



# WHILE LOOP

a = 1
while a<=5:
    print(a)
    a+=1

# wap to print even no from 1 to 10
b = 1
while b<=10:
    if b%2==0:
        print(b)
    b+=1

# wap to print reverse numbers form 10 to 1
c = 10
while c>=1:
    
    print(c)
    c-=1

# wap find sum of no from 1 to 10
d = 1
sum = 0
while d<=10:
    sum+=d
    print(f"sum of 1 to {d} is {sum}")
    d+=1

# wap print char of string
str="python"
a=0
while a<len(str):
    print(str[a])
    a+=1

# wap print element from list
list1 = [10,20,30,40]
b = 0
while b<len(list1):
    print(list1[b])
    b+=1

# wap count digit of number
number=12345
c = 0
while c < number:
    c += 1
    number //= 10
print(c)

# wap print table of 7
t = 7
a = 1
while a<=10:
    print(t*a)
    a+=1

# wap print only odd number from 1 to 10
a = 1
while a<=10:
    if a%2!=0:
        print(a)
    a+=1

# wap to asking the user input until they enter 0
u = eval(input("Enter value :"))
while u!=0:
    if u==0:
        print("Thanks")
    else:
        print("Invalid")
    u = eval(input("Enter value :"))

