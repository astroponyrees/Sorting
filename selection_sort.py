# Seleciton Sort O(n^2) Complxity
def selection(data):
    count = 0
    for i in range(0, len(data)):
        for j in range(i, len(data)):
            count += 1
            if data[i] > data[j]:
                data[j], data[i] = data[i], data[j]
    print(count)
    return data


stuff = [6, 5, 9, 10, 15, 4, 1, 3, 2, 7, 8, 6, 4]
print(selection(stuff))
new_stuff = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(selection(new_stuff))
