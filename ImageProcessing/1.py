import numpy as np
import math as m
from matplotlib import pyplot as plt
from ImgReader import readfile as r, writeNumeric as w

def ToBinary(lst:list, ref)->list:
    l = list()
    for i in range(len(lst)):
        if lst[i] == ref:
            # check if pixel belongs to object
            l.append(1)
        else:
            l.append(0)
    return l

def centerOfMass(p:int, q:int, blist:list, dimension:list)->float:
    col = dimension[0]
    row = dimension[1]
    sum = [0, 0]
    # center of mass x
    if p == 1:
        for y in range(row):
            for x in range(col):
                sum[0] += x*blist[y*col + x]
                sum[1] += blist[y*col + x]
    # center of mass y
    else:
        for y in range(row):
            for x in range(col):
                sum[0] += y*blist[y*col + x]
                sum[1] += blist[y*col + x]
    return sum[0]/sum[1]

def Moment(bList:list, dimension:list)->float:
    cmx = centerOfMass(1, 0, bList, dimension)
    cmy = centerOfMass(0, 1, bList, dimension)

    col = dimension[0]
    row = dimension[1]

    sum = [0, 0, 0]
    for y in range(row):
        for x in range(col):
            sum[0] += m.pow(x-cmx, 2)*bList[y*col + x]
            sum[1] += m.pow(y-cmy, 2)*bList[y*col + x]
            sum[2] += bList[y*col + x]

    moment = (sum[0] + sum[1])/m.pow(sum[2], 2)
    return moment

filename = "scaled_shapes.pgm"
head, lst, dimension = r(filename)
w(filename, lst, head, dimension)

ref = [0,80,120,160,200]
obj1 = ToBinary(lst, ref[0])
obj2 = ToBinary(lst, ref[1])
obj3 = ToBinary(lst, ref[2])
obj4 = ToBinary(lst, ref[3])
obj5 = ToBinary(lst, ref[4])

moment1 = Moment(obj1, dimension)
moment2 = Moment(obj2, dimension)
moment3 = Moment(obj3, dimension)
moment4 = Moment(obj4, dimension)
moment5 = Moment(obj5, dimension)

print(moment1)
print(moment2)
print(moment3)
print(moment4)
print(moment5)

plt.hist(lst)
plt.show()