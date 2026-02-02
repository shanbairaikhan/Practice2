#1
a=True
b=False
print(a and b)
print(a and True)
print(a or b)
print(b or False)
#2
x=10
y=0
print(x and y)
print(x or y)
print(not y)
#3
age=20
print(age>=18 and age<65)
print(age<18 or age>65)
#4
password="1234"
if password and len(password)>=4:
    print("Valid")
else:
    print("Invalid")
#5
score=85
if score>=90 or (score>=80 and score<90):
    print("Passed")
else:
    print("Failed")