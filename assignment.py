#########################################################################################################
#                                                                                                       #
#                                   Junior-developer-assignment                                         #
#                         https://gofore.com/junior-developer-assignment/                               #
#                                                                                                       #
#########################################################################################################
# Count how many steps it takes to reach (E)                                                            #
# Robot starts at character S                                                                           #
# Starting direction is always up                                                                       #
# If the robot is about to hit an obstacle, it should turn right before it and move forward.            #
# If the robot enters into S character after the start, treat S as a dot, so count it as a step.        #
# (E) character is counted as step                                                                      #
#########################################################################################################
#MAP_CODE 1778324

# Define imports here
import helperfunctions                  # Helper functions

#Define global variables here
startPointY = 0                         # start point y-coordinate
startPointX = 0                         # start point x-coordinate
coordX = 0                              # variable for x-coordinate in loops
coordY = 0                              # variable for y-coordinate in loops
coordinates = [0,0]                     # start point coordinates as a list                  
steps = 0                               # step count
direction = 0                           # stepping direction 0 = up, 1 = right, 2 = down, 3 = left

thislist = ["##################################################", # Copy assignment from a web to a list
"#................................................#",
"#.............#..........#.......................#",
"#................#.........................#.....#",
"#................................................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#........................S.......................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#.......................#........................#",
"#...............................#................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#................................................#",
"#......................#.........................#",
"#.........................................#......#",
"#............#...................................#",
"#..............................#.................#",
"#............#E..................................#",
"##################################################"]

# Use helper function to define starting coordinates
coordinates = helperfunctions.searchForStart(thislist)
startPointY = coordinates[0]
startPointX = coordinates[1]

print("Start point is: y=" + str(startPointY) + ", x=" + str(startPointX))

coordY = startPointY
coordX = startPointX

while True:
    # direction 0 is up. Y-1, X
    if direction == 0:
        # check if next character is 'E', if it is, count step by one and break
        if thislist[coordY-1][coordX] == 'E':
            steps += 1
            break
        # check if next character is '.', if it is, count step by one and substract one from coordinate Y (move up)
        elif thislist[coordY-1][coordX] == '.':
            steps += 1
            coordY -= 1
        # check if next character is '#', if it is, change direction, do not count a step yet
        elif thislist[coordY-1][coordX] == '#':
            direction = 1
            continue
    # direction 1 is right. Y, X+1
    elif direction == 1:
        # check if next character is 'E', if it is, count step by one and break
        if thislist[coordY][coordX+1] == 'E':
            steps += 1
            break
        # check if next character is '.', if it is, count step by one and add one to coordinate X (move right)
        elif thislist[coordY][coordX+1] == '.':
            steps += 1
            coordX += 1
        # check if next character is '#', if it is, change direction, do not count a step yet
        elif thislist[coordY][coordX+1] == '#':
            direction = 2
            continue
    # direction 2 is down. Y+1, X
    elif direction == 2:
        # check if next character is 'E', if it is, count step by one and break
        if thislist[coordY+1][coordX] == 'E':
            steps += 1
            break
        # check if next character is '.', if it is, count step by one and add one to coordinate Y (move down)
        elif thislist[coordY+1][coordX] == '.':
            steps += 1
            coordY += 1
        # check if next character is '#', if it is, change direction, do not count a step yet
        elif thislist[coordY+1][coordX] == '#':
            direction = 3
            continue
    # direction 3 is left. Y, X-1
    elif direction == 3:
        # check if next character is 'E', if it is, count step by one and break
        if thislist[coordY][coordX-1] == 'E':
            steps += 1
            break
        # check if next character is '.', if it is, count step by one and substract one from coordinate X (move left)
        elif thislist[coordY][coordX-1] == '.':
            steps += 1
            coordX -= 1
        # check if next character is '#', if it is, change direction, do not count a step yet
        elif thislist[coordY][coordX-1] == '#':
            direction = 0
            continue

print("Total step count is: " + str(steps))