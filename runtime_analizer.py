import random
import time
from bubble_sort import bubble
from selection_sort import selection
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quicksort

data_set_size  = int(input("How large is the dataset to be tested? "))
data_set_max_value = int(input("What is the value cap of the data set? "))
runs = int(input("How many trials should be done? "))

def performance(function_name, data):
    start_time = time.perf_counter()
    function_name(data)
    end_time = time.perf_counter()
    return end_time - start_time



for i in range(1,runs + 1):
    data_set = [random.randint(1,data_set_max_value)for _ in range(data_set_size)]
    print("______________________________________")
    print(f"Run {i}:")
    # Bubble Sort Test  
    print(f"Bubble Sort: {performance(bubble,data_set)}")

    # Selection Sort Test
    print(f"Selection Sort: {performance(selection,data_set)}")

    # Insertion Sort Test
    print(f"Insertion Sort: {performance(insertion_sort,data_set)}")

    # Merge Sort Test
    print(f"Merge Sort: {performance(merge_sort,data_set)}")

    # Quick Sort Test
    print(f"Quick Sort: {performance(quicksort,data_set)}")

    # Python Native Sort Test
    start_time = time.perf_counter()
    data_set.sort()
    end_time = time.perf_counter()
    print(f"Python Native Sort: {end_time - start_time}")

    print("______________________________________")
