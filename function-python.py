# square = lambda x: x * x
# print(square(5))

count = 0


def increase():
    global count
    count += 1


increase()
print(count)
