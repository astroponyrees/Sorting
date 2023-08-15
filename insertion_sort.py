def insertion_sort(data): 
    for i in range(1,len(data)):
        print(data)
        k = i
        j = i-1
        while j >= 0:
            if data[k] < data[j]:
                data[k],data[j] = data[j],data[k]
                k -= 1
            j -= 1
            print(data)
    return data

stuff = [6,3,9,1,2,8,4]
print(more_stuff = insertion_sort(stuff))
