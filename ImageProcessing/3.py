from ImgReader import readfile as r, writeNumeric as w

def ComputeExcessGreen(r:list, g:list, b:list)->list:
    '''2g-r-b'''
    iter = len(r)
    lst = list()
    for i in range(iter):
        eGreen = 2*g[i] - r[i] - b[i]
        if eGreen > 255:
            eGreen = 255
        elif eGreen < 0:
            eGreen = 0
        lst.append(eGreen)
    return lst

def ComputeRedBlueDifference(r:list, b:list)->list:
    '''r-b'''
    iter = len(r)
    lst = list()
    for i in range(iter):
        rbDiff = r[i] - b[i]
        if rbDiff > 255:
            rbDiff = 255
        elif rbDiff < 0:
            rbDiff = 0
        lst.append(rbDiff)
    return lst

def ComputeGrayLevel(r:list, g:list, b:list)->list:
    '''(r+g+b)/3'''
    iter = len(r)
    lst = list()
    for i in range(iter):
        gLvl = (r[i] + g[i] + b[i])/3
        if gLvl > 255:
            gLvl = 255
        elif gLvl < 0:
            gLvl = 0
        lst.append(int(round(gLvl)))
    return lst

filenames = {"red":"SanFranPeak_red.pgm", "blue":"SanFranPeak_green.pgm", "green":"SanFranPeak_blue.pgm"}
rHead, red, rDimension = r(filenames['red'])
gHead, green, gDimension = r(filenames['green'])
bHead, blue, bDimension = r(filenames['blue'])

eGreen = ComputeExcessGreen(red, green, blue)
# excess green uses 2nd parameter as excess color channel
eBlue = ComputeExcessGreen(red, blue, green)
eRed = ComputeExcessGreen(blue, red, green)
rbDiff = ComputeRedBlueDifference(red, blue)
gLvl = ComputeGrayLevel(red, green, blue)
w('SanFranPeak_excess_green.pgm', eGreen, gHead, gDimension)
w('SanFranPeak_excess_blue.pgm', eBlue, gHead, gDimension)
w('SanFranPeak_excess_red.pgm', eRed, gHead, gDimension)
w('SanFranPeak_reb_blue_difference.pgm', rbDiff, rHead, rDimension)
w('SanFranPeak_gray_level.pgm', gLvl, rHead, rDimension)