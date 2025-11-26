# 1) Check if a variable is of the type
a = 10
print(type(a))

# 2) Convert a string to an integer
b = "2"
print(int(b))

# 3) Get the length of a list
c = [1,2,3,4]
print("length of list: ", len(c))

# 4) Create a tuple and access the 2nd element
d = (1,2,3,4,5)
print(d[1])

# 5) Convert list to set
print("set: ",set(c))

# 6) Check  if a key exists in dict
e = {1:"a",2:"b",3:"c"}
print("existed key: ",e.keys())

# 7) Convert an integer to a string
print(str(a))

# 8) Merg two dict
f = {4:"d",5:"e"}
print(e | f)

# 9) Find the max num in a list without using max
num = [3,2,13,7,4]
max_num = num[0]
for n in num:
    if n > max_num:
        max_num = n
print("Maximum number:", max_num)


# 10) Covert list of tuple to a dictonary
h = [("a", 1), ("b", 2), ("c", 3)]
print("Dict: ",dict(h))

# 11) Reverse a string
k = "Abhi"
print(k[::-1])

# 12) Remove duplicates from a list while keeping order
p = [1,2,2,3,3,3,4,4,4,4]
z = set(p)
p = list(z)
print(p.sort())

# 13) Convert nested list to a single flat list
# lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
# flat_list=[]
# for i in lis:
#     flat_list.extend(i)
# print('List', lis)
# print('Flat List', flat_list)

# 14) Count frequency of each elemnent in list.
# p = [1,1,2,2,3,3,4,4,4]
# t = {}
# for num in p:
#     t[num] = t.get(num, 0) + 1
# print(t)

# 15) Sort Dict by vale

# m = {'a':2,'b':1,'c':4,'d':3}
# print(dict(sorted(m.items(),key=lambda item: item[1])))

# 16) Check if two list have the same element
i=[2,3,4]
l = 0
common=[]
for x in c:
    if x==i[l]:
        common.append(x)
        l+=1
print("Common in list",common)

# 17) Find common key in two dictionaries.
q = {1:"a",2:"b",3:"c"}
r = {1:"d",2:"e"}
q_key = q.keys()
r_key = r.keys()
print("common keys",q_key & r_key) # 1
for a in q_key:
    if a in r_key:
        print("common key",a) # 2
