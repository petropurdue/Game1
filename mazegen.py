from random import *

def createborder(xlen, ylen):
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
    print("...........................................")

def gendir(): #pretty sure this is useless
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

def cangen(map, xcord, ycord): #see if a new point can be generated as part of the path
    #doesn't actually matter if you mix up x and y cords, it will work regardless.
    xtouch = 0
    ytouch = 0
    if map[ycord][xcord] == [0]:
        return 0
    if map[ycord][xcord+1] == '0':
        xtouch +=1
    if map[ycord][xcord-1] == '0':
        xtouch +=1
    if map[ycord+1][xcord] == '0':
        ytouch+=1
    if map[ycord-1][xcord] == '0':
        ytouch+=1

    if (ytouch <=1): #if only touching from one side (where it entered from)
        return 1
    return 0        #all else

def genmainpath(map):
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



if __name__ == '__main__':
    dim = 10
    border = createborder(20,12)
    printborder(border)
    genmainpath(border)
