#1
numbers = [1, 2, -1, 4]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        break
    print(numbers[i])
    i += 1
#2
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
#3
i = 1
while i < 10:
    if i % 2 == 0:
        break
    print(i)
    i += 1
#4
x = 10
while x > 0:
    if x == 5:
        break
    print(x)
    x -= 1
#5
i = 0
while True:
    print(i)
    i += 1
    if i >= 3:
        break