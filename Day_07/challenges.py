# Challenge 1 - Skip multiples of 3

for i in range(1, 21):
    if i % 3 == 0:
        continue

    print(i)


# Challenge 2 - Skip multiples of 3 and stop at 25

for i in range(1, 31):
    if i % 3 == 0:
        continue

    if i == 25:
        break

    print(i)


# Challenge 3 - Pass

for i in range(1, 11):
    if i == 5:
        pass

    print(i)
