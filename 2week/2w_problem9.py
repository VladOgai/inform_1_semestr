import re


file = open('input.txt', 'r')
mst = "Hello, world! go? ddd."
print(re.split("!|?|.", mst))
