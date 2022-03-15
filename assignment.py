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

# User helper function to define starting coordinates
coordinates = helperfunctions.searchForStart(thislist)
startPointY = coordinates[0]
startPointX = coordinates[1]

print("Start point is: y=" + str(startPointY) + ", x=" + str(startPointX))

while True:
    if direction == 0:
        
        break
    elif direction == 1:
        
        break
    elif direction == 2:
        
        break
    elif direction == 3:
        
        break

print("Total step count is: " + str(steps))