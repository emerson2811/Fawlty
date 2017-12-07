import re

pattern = r"[A-Z][A-Z][0-9]"
#searches for a patter of letter letter number

if re.search(pattern, "AA1"):
    print("Match found")

pattern = r"eggs(bacon)*"

if re.match(pattern, "bacon"):
    print("Match found")