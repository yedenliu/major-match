finalList = []
courseIn = 'STAT 218, STAT 220, STAT 221, STAT 228, STAT 260, STAT 318'
courseList = courseIn.split(',')
for item in courseList:
    if item[0] == ' ':
        item = item[1:]
    if item[-1:] == ',':
        item = item[0:-1]
    finalList.append(item)
print(finalList)