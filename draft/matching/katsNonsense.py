finalList = []
courseIn = 'FREN 208,  FREN 209, FREN 213, FREN 214, FREN 216, FREN 217, FREN 221, FREN 223, FREN 224, FREN 228, FREN 234, FREN 235, FREN 237, FREN 241, FREN 278, FREN 302, FREN 303, FREN 306, FREN 307, FREN 308, FREN 312, FREN 313, FREN 315, FREN 317, FREN 319, FREN 330, FREN 333'
courseList = courseIn.split(',')
for item in courseList:
    if item[0] == ' ':
        item = item[1:]
    if item[-1:] == ',':
        item = item[0:-1]
    finalList.append(item)
print(finalList)