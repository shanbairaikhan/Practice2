#1
for i in range(10):
    if i == 5:
        break
    print(i)
#2
numbers = [1, 3, -2, 4]
for n in numbers:
    if n < 0:
        break
    print(n)
#3
for i in range(1, 20):
    if i % 7 == 0:
        break
    print(i)
#4
for letter in "Python":
    if letter == "h":
        break
    print(letter)
#5
words = ["hello", "", "world"]
for word in words:
    if word == "":
        break
    print(word)
#6
for guess in [3, 5, 7]:
    if guess == 5:
        break
    print("Try:", guess)
