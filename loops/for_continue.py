#1
words = ["hello", "", "world"]
for word in words:
    if word == "":
        continue
    print(word)
#2
for i in range(1, 10):
    if i % 3 == 0:
        continue
    print(i)
#3
for letter in "Python":
    if letter in "aeiou":
        continue
    print(letter)
#4
for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
#5
for i in range(1, 10):
    if i < 5:
        continue
    print(i)
#6
numbers = [1, -3, 2, -4, 5]
for n in numbers:
    if n < 0:
        continue
    print(n)