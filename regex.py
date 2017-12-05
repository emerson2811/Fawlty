import re
#imports regular expression module

pattern = r"eggs"

if re.match(pattern,"greeneggsandham"):
    print('Match found')
else:
    print('No match found')
#searches for exact matches to the string

if re.search(pattern, "baconeggseggsbacon"):
    print('Match found')
else:
    print('No match found')
#matches the pattern anywhere (even in other strings)

print(re.findall(pattern, "baconeggseggsbacon"))
#finds the patter anywhere and prints the pattern
