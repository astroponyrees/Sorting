def bubble(data):
    has_swaped = True
    while has_swaped:
        has_swaped = False
        for i in range(0, len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                has_swaped = True
    return data


# stuff = [6, 5, 9, 10, 15, 4, 1, 3, 2, 7, 8, 6, 4]
# print(bubble(stuff))
# new_stuff = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# print(bubble(new_stuff))

