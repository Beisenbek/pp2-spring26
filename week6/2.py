import re

txt = "The rain 1in Spain"
x = re.search(".*[0-9]+.*", txt)
print(x)