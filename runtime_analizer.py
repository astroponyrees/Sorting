import random
import time
import bubble_sort
import selection_sort
import insertion_sort
import merge_sort
import quick_sort

data_set_size  = int(input("How large is the dataset to be tested? "))
data_set_max_value = int(input("What is the value cap of the data set? "))
runs = int(input("How many trials should be done? "))
data_set = [random.randint(1,data_set_max_value)for _ in range(data_set_size)]

# Bubble Sort Test
start_time = time.perf_counter()
bubble_sort.bubble(data_set)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Bubble Sort: {elapsed_time}")

# Selection Sort Test
start_time = time.perf_counter()
selection_sort.selection(data_set)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Selection Sort: {elapsed_time}")

# Insertion Sort Test
start_time = time.perf_counter()
insertion_sort.insertion_sort(data_set)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Insertion Sort: {elapsed_time}")

# Merge Sort Test
start_time = time.perf_counter()
merge_sort.merge_sort(data_set)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Merge Sort: {elapsed_time}")

# Quick Sort Test
start_time = time.perf_counter()
quick_sort.quicksort(data_set)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Quick Sort: {elapsed_time}")

# Python Native Sort Test
start_time = time.perf_counter()
data_set.sort()
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Python Native Sort: {elapsed_time}")

