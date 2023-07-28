def bubble(data):
    for j in range(0, len(data)):
        for i in range(0, len(data) - 1):
            if data[i] >= data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data


stuff = [4, 7, 3, 9, 10, 2, 1, 6, 5, 8, 1]
print(bubble(stuff))
