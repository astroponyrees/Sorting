def merge_sort(data):
    if len(data) == 1:
        return data
    else:
        split = len(data)//2
        sub1 = merge_sort(data[:split])
        sub2 = merge_sort(data[split:])
        merged_n_sorted = merge(sub1,sub2)
        return merged_n_sorted
    
def merge(data1,data2):
    sorted = []
    while len(data1) != 0 and len(data2) != 0:
        if data1[0] > data2[0]:
            sorted.append(data2[0])
            data2.pop(0)
        else:
            sorted.append(data1[0])
            data1.pop(0)
    if len(data1) == 0:
        sorted.extend(data2)
    elif len(data2) == 0:
        sorted.extend(data1)
    return sorted


# hot_mess = [5,2,7,6,9,1,4,3,15,8,10]
# print(merge_sort(hot_mess))

