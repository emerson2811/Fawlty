import re

pattern = r"gr.y"
#looks for any string with a gr at the beginning and a y at the end

if re.match(pattern, "gray"):
    print('Match found')