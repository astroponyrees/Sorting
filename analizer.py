import time 
import random

class Analizer:
    def __init__(self,function_name,data_set_size,data_set_range):
        self.function_name = function_name
        self.data_set_size = data_set_size
        self.data_set_range = data_set_range
        self.performance = 0


    def analize(self):
        data_set = [random.randint(1,self.data_set_range) for _ in range(self.data_set_size)]
        if function_name == "native":
            start_time = time.perf_counter()
            data_set.sort()
            end_time = time.perf_counter()
            self.performance = end_time - start_time
        else:
            start_time = time.perf_counter()
            self.function_name(data_set)
            end_time = time.perf_counter()
            self.performance = end_time - start_time

    def __str__():
        return f"{self.function_name} performed in {self.performance} seconds."





