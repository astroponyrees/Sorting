import random


def quicksort(data):
    if len(data) <= 1:
        return data
    right = []
    left = []
    length = len(data)
    randish = random.randint(0, length-1)
    pivot = data[randish]
    middle = []
    for i in range(0, length):
        if data[i] < pivot:
            right.append(data[i])
        elif data[i] > pivot:
            left.append(data[i])
        else:
            middle.append(pivot)
            continue
    smaller = quicksort(right)
    larger = quicksort(left)
    return smaller + middle + larger


stuff = [5, 6, 1, 3, 9, 10, 2, 7, 4, 2, 8, 1, 15, 45, 5, 6, 6, 11, 12]
print(quicksort(stuff))
