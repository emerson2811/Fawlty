from itertools import count
#imports the "count" function from the "itertools" module
#fails because it cannot find "count", I don't think the right itertools version is installed

for i in count(3):
    print (i)

    if i >= 20:
        break

from itertools import accumulate

