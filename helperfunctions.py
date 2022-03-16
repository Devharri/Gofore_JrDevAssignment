# function for looping through a list and looking for a character 'S'
def searchForStart(list):
    listLength = len(list)
    for y in range(listLength):
        listStringLength = len(list[y])
        for x in range(listStringLength):
            if list[y][x] == "S":
                coordinates = [y,x]
                return coordinates
    return [0,0]