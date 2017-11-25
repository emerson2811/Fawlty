# file = open("demo.txt", 'w')
# #do something with the file
# file.close()
# #closes the file - always close files
#
# file = open ("nonsense.txt", 'r')
# content = file.readline()
# #opens a file, reads the content of the file into the "content" varialble
# print(content)
# file.close()

file = open("nonsense.txt", 'w')
file.write("text written to file")
file.close()

file = open("nonsense.txt", 'r')
content = file.read()
print(content)
file.close()

file = open("nonsense.txt", 'a')
file.write("this is the new line")
file.close()