newlist = [1, 3, 4, 5, 7, 2, 9, 11, 13, 14, 22, 26]

result = list(filter(lambda x:x% 2 == 0, newlist))

print(result)