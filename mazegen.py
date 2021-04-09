from random import *

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

def printborder(border):
    for i in range(len(border)):
        print(border[i])

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

def cangen(map, xcord, ycord):
    '''
    See if a new point can be generated as part of the path without merging with another path.
    Doesn't actually matter if you mix up x and y cords, it will work regardless.
    :param map: the map we're testing validity on
    :param xcord: the x coordinate of the point we're testing on the map
    :param ycord: the y coordinate of the point we're testing on the map
    :return: 1 if a coordinate is a valid path extension, 0 if not
    '''
    touches = 0
    if map[ycord][xcord+1] == '0':
        touches+=1
    if map[ycord][xcord-1] == '0':
        touches+=1
    if map[ycord+1][xcord] == '0':
        touches+=1
    if map[ycord-1][xcord] == '0':
        touches+=1

    if touches <=1: #if only touching from one side (where it entered from)
        return 1
    return 0        #all else

def genrandpath(yval, xval):
    '''
    Generates new path nodes. Recursively.
    :param yval:
    :param xval:
    :return:
    '''
    #Generate a new random order to create a new path
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
    print(a,b,c,d)

def genrandpathsetup(map):
    ystart,xstart = getstart(map)
    genrandpath(ystart,xstart)

def settestpath(map):
    newline()
    temp = map[1]
    map[1][1] = '?'
    map[2][1] = '0'
    map[2][2] = '0'
    map[2][3] = '0'
    map[3][3] = '0'
    map[4][3] = '0'
    map[5][3] = '0'
    map[5][2] = '0'
    map[5][1] = '0'
    map[6][1] = '0'
    map[7][1] = '0'
    map[7][2] = '0'
    printborder(map)

    print(cangen(map,2,3))

def getlen(map):
    '''
    returns how tall the map is. Note this INCLUDES the borders
    :param map: the map we're testing the height of
    :return: length, the HEIGHT of the map. ------------------------------------------FIX THIS TO BE HEIGHT, NOT LENGTH
    '''
    length = 0
    for i in range(len(map)):
        #print(i)
        length+=1
    return length

def getstart(map):
    '''
    finds out where to start on the map, as determined by the character '?'
    :param map: The map we're finding the start point on
    :return: the coordinates of where the start point is, as a list.
    '''

    for y in range(getlen(map)):
        temp = map[y]
        for x in range(len(temp)):
            if map[y][x] == '?':
                print("Start found at",y,x)
                #print(map[y][x])
                return[y,x]

def travel(map, ycord, xcord): #this currently only detects edges, not final values. Below is a hypothetical implementation that would detect when it gets to the true end.
    '''
    :param map:
    :param ycord:
    :param xcord:
    :return:
    '''
    '''
    if map[ycord][xcord] == '!' #in this case, ! is the ending value
        return [ycord, xcord]
    '''
    #print("CURR:",map[ycord][xcord])
    map[ycord][xcord] = 'o' #set the current coordinate to o, similiar to setting a traversed node to grey in a tree

    #orientations, pretty much useless for anything other than reference
    right = map[ycord][xcord+1]
    left = map[ycord][xcord-1]
    up = map[ycord-1][xcord]
    down = map[ycord+1][xcord]
    if up == '0':
        #print("up")
        return travel(map, ycord - 1, xcord)
    if down == '0':
        #print("down")
        return travel(map, ycord + 1, xcord)
    if left == '0':
        #print("L")
        return travel(map, ycord, xcord - 1)
    if right == '0':
        #print("R")
        return travel(map, ycord, xcord + 1)
    return [ycord,xcord]

if __name__ == '__main__':
    dim = 10
    border = createborder(20,12)
    printborder(border)
    newline()
    settestpath(border)
    yx = getstart(border)
    genrandpath(1,1)
    print("found edge at",travel(border,yx[0],yx[1]))
