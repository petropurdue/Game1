from random import *

#see genrandpath for potential improvements

def createborder(xlen, ylen):
    '''
    Creates a box with a border of X's
    :param xlen: The x length of the box generated
    :param ylen: The y length of the box generated
    :return: border, a list of lists forming a rectangle.
    '''
    border = []

    vertedge = ['X']*xlen

    border.append(vertedge)
    for i in range(ylen-2):
        y = ['X']
        for i in range(xlen - 2):
            y.append(' ')
        y.append('X')
        border.append(y)
    border.append(vertedge)#for some reason this actually appends a pointer to vertedge. Weird but convenient, I guess

    return border

def printmap(border): #have it not print the x's?
    for i in range(len(border)):
        printlist = border[i]
        for i in printlist:
            print(i,end=" ")
        print()

def newline():
    '''
    Prints a fancy new line because I'm tired of typing all those periods over and over. That's it.
    :return: Nothing
    '''
    print("...........................................")

def gendir(): #pretty sure this is useless
    '''

    :return:
    '''
    recint = random.randint(0,3)
    if recint == 0:
        return 'up'
    if recint == 1:
        return 'right'
    if recint == 2:
        return 'down'
    if recint == 3:
        return 'left'
    return 'failure'

def cangen(map, ycord, xcord):
    '''
    See if a new point can be generated as part of the path without merging with another path.
    Doesn't actually matter if you mix up x and y cords, it will work regardless.
    :param map: the map we're testing validity on
    :param xcord: the x coordinate of the point we're testing on the map
    :param ycord: the y coordinate of the point we're testing on the map
    :return: 1 if a coordinate is a valid path extension, 0 if not
    '''
    #Test to make sure we aren't potentially generating on a border or special point
    if (map[ycord][xcord] == '!') | (map[ycord][xcord] == '?') | (map[ycord][xcord] == 'X'):
        return False

    #Initializations to test how many other paths it is touching
    touches = 0
    if map[ycord][xcord+1] == '???':
        touches+=1
    if map[ycord][xcord-1] == '???':
        touches+=1
    if map[ycord+1][xcord] == '???':
        touches+=1
    if map[ycord-1][xcord] == '???':
        touches+=1

    if touches <=1: #if only touching from one side (where it entered from)
        if map[ycord][xcord] == ' ':
            map[ycord][xcord] = '???'
        return True

    return False        #all else

def genrandpath(map,ycord, xcord):
    '''
    Generates new path nodes. Recursively.
    :param ycord:
    :param xcord:
    :return:
    '''
    #Generate a new random order sequence to create a new path
    a = randint(0,3)
    b = randint(0,3)
    c = randint(0,3)
    d = randint(0,3)
    while b == a:
        b = randint(0, 3)
    while ((c == b) | (c==a)):
        c = randint(0, 3)
    while ((d == c) | (d == b) | (d==a)):
        d = randint(0, 3)
    order = [a,b,c,d]
    #print(order)
    for i in order:
        if i == 0:
            if cangen(map, ycord - 1, xcord):
                genrandpath(map, ycord - 1, xcord)
        if i == 1:
            if cangen(map, ycord + 1, xcord):
                genrandpath(map, ycord + 1, xcord)

        if i == 2:
            if cangen(map, ycord, xcord - 1):
                genrandpath(map, ycord, xcord - 1)
        if i == 3:
            if cangen(map, ycord, xcord + 1):
                genrandpath(map, ycord, xcord + 1)


def detectedge(map, ycord, xcord): #this only detects if a path has an edge.
    '''
    :param map:
    :param ycord:
    :param xcord:
    :return:
    '''
    map[ycord][xcord] = 'o'  # set the current coordinate to o, similiar to setting a traversed node to grey in a tree

    # orientations, pretty much useless for anything other than reference
    right = map[ycord][xcord + 1]
    left = map[ycord][xcord - 1]
    up = map[ycord - 1][xcord]
    down = map[ycord + 1][xcord]
    if up == '0':
        # print("up")
        return travel(map, ycord - 1, xcord)
    if down == '0':
        # print("down")
        return travel(map, ycord + 1, xcord)
    if left == '0':
        # print("L")
        return travel(map, ycord, xcord - 1)
    if right == '0':
        # print("R")
        return travel(map, ycord, xcord + 1)
    return [ycord, xcord]

def genexit(map):
    '''
    Generates an exit point for the map from the created path(s).
    :param map: The map we're finding the end point of
    :return: newmap, the map; updated to have an endpoint
    '''
    xcord = getmaplength(map) - 2 #this will be the rightmost column that is NOT a border.
    ycord = 0
    while map[ycord][xcord] != '???':
        print(map[ycord][xcord])
        ycord = randint(1,getmapheight(map)-1)

    while (map[ycord + 1][xcord] == '???') & (map[ycord -1][xcord] == '???'):
        ycord-=1 #keep movin' on up

    #Test if there are any paths that need to be abandoned
    #Any lower paths
    '''
    if (map[ycord+1][xcord] != 'X') & (map[ycord-1][xcord] != ' '): #Make sure it's not a corner
        map[ycord+1][xcord] = ' '  #cut off the path below
    '''
    #If there is a path to the left, you can cut off the above and below paths.
    ''' This is commented out. This program can be improved by fixing this function.
    if ((map[ycord][xcord - 1] == '???') & delhelper(map,ycord,xcord)): #if, after the previous two lines' work, there are still two paths into this point
        #Test that the point to the left is not an edge

        if map[ycord+1][xcord] != 'X':
            map[ycord+1][xcord] = ' '
        if map[ycord-1][xcord] != 'X':
            map[ycord-1][xcord] = ' '
    '''
    map[ycord][xcord] = '!'
    return map


def delhelper(map, ycord, xcord):
    '''

    :param map:
    :param ycord:
    :param xcord:
    :return:
    '''
    while map[ycord][xcord] == '???':
        if (map[ycord + 1][xcord] == '???') | (map[ycord - 1][xcord] == '???'):
            return False
        xcord -= 1
    return True

    #This is a chunk from cangen(), but it's best not to try and do too much with one function.
    touches = 0
    if map[ycord][xcord+1] == '???':
        touches+=1
    if map[ycord][xcord-1] == '???':
        touches+=1
    if map[ycord+1][xcord] == '???':
        touches+=1
    if map[ycord-1][xcord] == '???':
        touches+=1

    if touches <=1: #if only touching from one side (where it entered from)
        if map[ycord][xcord] == ' ':
            map[ycord][xcord] = '???'
        return True

    return False        #all else




def genrandpathsetup(map):
    '''

    :param map:
    :return:
    '''
    map[randint(1, len(map) - 2)][1] = '?'
    ystart,xstart = getstart(map)
    genrandpath(map,ystart,xstart)
    genexit(map)

def settestpath(map):
    newline()
    temp = map[1]
    map[1][1] = '?'
    map[2][1] = '???'
    map[2][2] = '???'
    map[2][3] = '???'
    map[3][3] = '???'
    map[3][4] = '???'
    map[3][5] = '???'
    map[3][6] = '!'
    map[4][3] = '???'
    map[5][3] = '???'
    map[5][2] = '???'
    map[5][1] = '???'
    map[6][1] = '???'
    map[7][1] = '???'
    map[7][2] = '???'
    #map[7][3] = '!'
    printmap(map)

    print(cangen(map,2,3))

def getmaplength(map):
    '''
    Get the map length
    :param map: the map we're testing the length of
    :return: the length of the map as an integer
    '''
    listi = map[0]
    return len(listi)

def getmapheight(map):
    '''
    returns how tall the map is. Note this INCLUDES the borders
    :param map: the map we're testing the height of
    :return: length, the HEIGHT of the map. ------------------------------------------FIX THIS TO BE HEIGHT, NOT LENGTH
    '''
    height = 0
    for i in range(len(map)):
        #print(i)
        height+=1
    print(height)
    return height

def getstart(map):
    '''
    finds out where to start on the map, as determined by the character '?'
    :param map: The map we're finding the start point on
    :return: the coordinates of where the start point is, as a list.
    '''

    for y in range(getmapheight(map)):
        temp = map[y]
        for x in range(len(temp)):
            if map[y][x] == '?':
                print("Start found at",y,x)
                #print(map[y][x])
                return[y,x]
    print("ERROR: COULD NOT FIND START! GENERATING RANDOM START.")
    return [-666,-666]

def travel(map, ycord, xcord,findlist):
    '''
    #this currently only detects edges, not final values. Below is a hypothetical implementation that would detect when it gets to the true end.
    :param map: The map being explored
    :param ycord: the y coordinate of where is being explored
    :param xcord: the x coordinate of where is being explored
    :param findlist: where the end is found
    :return:
    '''

    if map[ycord][xcord] == '!': #in this case, ! is the ending value
        return [ycord, xcord]

    #print("CURR:",map[ycord][xcord])
    map[ycord][xcord] = 'o' #set the current coordinate to o, similiar to setting a traversed node to grey in a tree

    #orientations, pretty much useless for anything other than reference
    right = map[ycord][xcord+1]
    left = map[ycord][xcord-1]
    up = map[ycord-1][xcord]
    down = map[ycord+1][xcord]
    if ((up == '???') | (up == '!')):
        print("up",[ycord],[xcord])
        findlist = travel(map, ycord - 1, xcord,findlist)
    if ((down == '???') | (down == '!')):
        print("down",[ycord],[xcord])
        findlist = travel(map, ycord + 1, xcord,findlist)
    if ((left == '???') | (left == '!')):
        print("L",[ycord],[xcord])
        findlist = travel(map, ycord, xcord - 1,findlist)
    if ((right == '???') | (right == '!')):
        print("R",[ycord],[xcord])
        findlist = travel(map, ycord, xcord + 1,findlist)
    return findlist

if __name__ == '__main__':
    dim = 10
    border = createborder(20,12)
    #printmap(border)
    #newline()
    #settestpath(border)
    genrandpathsetup(border)
    getmaplength(border)
    printmap(border)
    #print("found edge at",travel(border,yx[0],yx[1],[]))
