file = open("nonsense.txt", 'w')
file.write("some nonsense about text")
file.close()

file = open("nonsense.txt", 'r')
content = file.read()
print (content)
file.close()

file = open("nonsense.txt", 'a')
file.write(" and a little more nonsense about text")
file.close()

file = open("nonsense.txt", 'r')
content = file.read()
print (content)
file.close()