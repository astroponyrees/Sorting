def bubble(data):
    has_swaped = True
    while has_swaped:
        has_swaped = False
        for i in range(0, len(data) - 1):
            print(data)
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                has_swaped = True
            print(has_swaped)
    return data


stuff = [4, 7, 3, 9, 10, 2, 1, 6, 5, 8, 1]
print(bubble(stuff))
