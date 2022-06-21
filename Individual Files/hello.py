#this is my first python program
"""
Author is Rahul Dodda
Created May 18th 2022
"""
print('Python is easy!!')

x = int(input("Enter min number:"))
y = int(input("Enter max number:"))
i=x
if i % 2 == 0:
    i = x+1
while i <= y:
    print(i)
    i += 2