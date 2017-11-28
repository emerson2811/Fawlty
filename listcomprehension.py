list = [x**2 for x in range(5)]
#allows a way to define what will be in the list - this will define squared numbers for a range (including 0)
print(list)

list = [x**2 for x in range(10) if x**2 % 2 == 0]
print(list)

