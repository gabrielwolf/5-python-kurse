# Python 2.7.12

import re

try:
    fhand = open("regex_sum_323510.txt", "r")
except:
    print "Sorry can't open file!"
    quit()

matches = []

for line in fhand:
    pattern = re.findall('([0-9]+)', line)
    if pattern != []:
        for item in pattern:
            # print "Debug item:", item
            matches.append(int(item))

print "Count of numbers:", len(matches)
print "Sum of numbers:", sum(matches)