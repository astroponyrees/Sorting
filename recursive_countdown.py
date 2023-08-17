import time

def recursive_countdown(duration):
    print(duration)
    if duration == 1:
        time.sleep(1)
        print(0)
        return 0
    else:
        time.sleep(1)
        recursive_countdown(duration-1)

recursive_countdown(10)
