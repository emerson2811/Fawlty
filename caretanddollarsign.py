import re

patter = r"^$"
#r is the beginning of a string and $ is the end of a string

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")