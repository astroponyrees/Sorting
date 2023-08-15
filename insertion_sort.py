def insertion_sort(data): 
    count = 0        
    for i in range(1,len(data)): 
        k = i
        j = i-1
        while j >= 0:
            count += 1
            if data[k] < data[j]:
                data[k],data[j] = data[j],data[k]
                k -= 1
            j -= 1
    print(count)
    return data

stuff = [6, 5, 9, 10, 15, 4, 1, 3, 2, 7, 8, 6, 4]
print(insertion_sort(stuff))
additional_stuff = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(insertion_sort(additional_stuff))

