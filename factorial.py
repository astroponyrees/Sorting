def factorial(num):
    print(num)
    if num == 0:
        return 1
    else:
      return num * factorial(num-1)


solution = factorial(5)
print(solution)
