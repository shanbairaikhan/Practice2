#1
i = 0
total = 0
while i < 10:
    total += i
    i += 1
    if total < 5:
        continue
    print("Total:", total)

#2
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)
#3
i = 0
while i < 2:
    j = 0
    while j < 3:
        j += 1
        if j == 2:
            continue
        print(i, j)
    i += 1
#4
word = "Python"
i = 0
while i < len(word):
    if word[i] in "aeiouAEIOU":
        i += 1
        continue
    print(word[i])
    i += 1

#5
i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1