# Seleciton Sort O(n^2) Complxity
def selection(data):
    for i in range(0, len(data)):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                data[j], data[i] = data[i], data[j]
    return data


stuff = [6, 5, 9, 10, 15, 4, 1, 3, 2, 7, 8, 6, 4]
print(selection(stuff))
