from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

c = 0
for el in cycle("СПИСОК"):
    if c > 10:
        break
    print(el)
    c += 1
