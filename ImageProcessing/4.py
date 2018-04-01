from ImgReader import readfile as r, writeNumeric as w
from TriangularMatrix import ComputeW as c

def Restore(wxy:list, grayLvl:list, disGrid:list, grid:list, size:int, section:int)->list:
    # wxy = (x, y), row = x, col = y
    lst = list()
    for row in range(size):
        for col in range(size):
            cindex:int
            rindex:int
            for i in range(1, section+1):
                if col <= grid[i][1]:
                    cindex = i-1
                    break
            for i in range(1, section+1):
                if row <= grid[section*(i)+1][0]:
                    rindex = i-1
                    break
            # wxy[rindex*size+cindex]
            wx = wxy[rindex*section+cindex][0]
            wy = wxy[rindex*section+cindex][1]
            x = round(wx[0]*row+wx[1]*col+wx[2]*col*row+wx[3])
            y = round(wy[0]*row+wy[1]*col+wy[2]*col*row+wy[3])
            lst.append(grayLvl[size*x+y])
    return lst
grid = [
    [0, 0], [0, 16], [0, 32], [0, 48], [0, 64], [0, 80], [0, 96], [0, 112], [0, 128], [
        0, 144], [0, 160], [0, 176], [0, 192], [0, 208], [0, 224], [0, 240], [0, 255],
    [15, 0], [15, 16], [15, 32], [15, 48], [15, 64], [15, 80], [15, 96], [15, 112], [15, 128], [
            15, 144], [15, 160], [15, 176], [15, 192], [15, 208], [15, 224], [15, 240], [15, 255],
    [31, 0], [31, 16], [31, 32], [31, 48], [31, 64], [31, 80], [31, 96], [31, 112], [31, 128], [
            31, 144], [31, 160], [31, 176], [31, 192], [31, 208], [31, 224], [31, 240], [31, 255],
    [47, 0], [47, 16], [47, 32], [47, 48], [47, 64], [47, 80], [47, 96], [47, 112], [47, 128], [
            47, 144], [47, 160], [47, 176], [47, 192], [47, 208], [47, 224], [47, 240], [47, 255],
    [63, 0], [63, 16], [63, 32], [63, 48], [63, 64], [63, 80], [63, 96], [63, 112], [63, 128], [
            63, 144], [63, 160], [63, 176], [63, 192], [63, 208], [63, 224], [63, 240], [63, 255],
    [79, 0], [79, 16], [79, 32], [79, 48], [79, 64], [79, 80], [79, 96], [79, 112], [79, 128], [
            79, 144], [79, 160], [79, 176], [79, 192], [79, 208], [79, 224], [79, 240], [79, 255],
    [95, 0], [95, 16], [95, 32], [95, 48], [95, 64], [95, 80], [95, 96], [95, 112], [95, 128], [
            95, 144], [95, 160], [95, 176], [95, 192], [95, 208], [95, 224], [95, 240], [95, 255],
    [111, 0], [111, 16], [111, 32], [111, 48], [111, 64], [111, 80], [111, 96], [111, 112], [111, 128], [
            111, 144], [111, 160], [111, 176], [111, 192], [111, 208], [111, 224], [111, 240], [111, 255],
    [127, 0], [127, 16], [127, 32], [127, 48], [127, 64], [127, 80], [127, 96], [127, 112], [127, 128], [
            127, 144], [127, 160], [127, 176], [127, 192], [127, 208], [127, 224], [127, 240], [127, 255],
    [143, 0], [143, 16], [143, 32], [143, 48], [143, 64], [143, 80], [143, 96], [143, 112], [143, 128], [
            143, 144], [143, 160], [143, 176], [143, 192], [143, 208], [143, 224], [143, 240], [143, 255],
    [159, 0], [159, 16], [159, 32], [159, 48], [159, 64], [159, 80], [159, 96], [159, 112], [159, 128], [
            159, 144], [159, 160], [159, 176], [159, 192], [159, 208], [159, 224], [159, 240], [159, 255],
    [175, 0], [175, 16], [175, 32], [175, 48], [175, 64], [175, 80], [175, 96], [175, 112], [175, 128], [
            175, 144], [175, 160], [175, 176], [175, 192], [175, 208], [175, 224], [175, 240], [175, 255],
    [191, 0], [191, 16], [191, 32], [191, 48], [191, 64], [191, 80], [191, 96], [191, 112], [191, 128], [
            191, 144], [191, 160], [191, 176], [191, 192], [191, 208], [191, 224], [191, 240], [191, 255],
    [207, 0], [207, 16], [207, 32], [207, 48], [207, 64], [207, 80], [207, 96], [207, 112], [207, 128], [
            207, 144], [207, 160], [207, 176], [207, 192], [207, 208], [207, 224], [207, 240], [207, 255],
    [223, 0], [223, 16], [223, 32], [223, 48], [223, 64], [223, 80], [223, 96], [223, 112], [223, 128], [
            223, 144], [223, 160], [223, 176], [223, 192], [223, 208], [223, 224], [223, 240], [223, 255],
    [239, 0], [239, 16], [239, 32], [239, 48], [239, 64], [239, 80], [239, 96], [239, 112], [239, 128], [
            239, 144], [239, 160], [239, 176], [239, 192], [239, 208], [239, 224], [239, 240], [239, 255],
    [255, 0], [255, 16], [255, 32], [255, 48], [255, 64], [255, 80], [255, 96], [255, 112], [255, 128], [
            255, 144], [255, 160], [255, 176], [255, 192], [255, 208], [255, 224], [255, 240], [255, 255]
]
disGrid = [
    [0, 0], [0, 16], [0, 32], [0, 48], [0, 64], [0, 80], [0, 96], [0, 112], [0, 128], [
        0, 144], [0, 160], [0, 176], [0, 192], [0, 208], [0, 224], [0, 240], [0, 255],
    [15, 0], [15, 16], [15, 32], [15, 48], [15, 64], [15, 80], [16, 97], [17, 114], [18, 130], [
        18, 145], [17, 161], [15, 176], [15, 192], [15, 208], [15, 224], [15, 240], [15, 255],
    [31, 0], [31, 16], [31, 32], [31, 48], [32, 66], [34, 85], [36, 103], [38, 121], [41, 136], [
        42, 150], [41, 163], [37, 177], [34, 192], [31, 208], [31, 224], [31, 240], [31, 255],
    [47, 0], [47, 16], [47, 32], [48, 51], [49, 72], [52, 94], [56, 112], [59, 128], [62, 141], [
        64, 154], [64, 166], [62, 178], [56, 192], [50, 208], [47, 224], [47, 240], [47, 255],
    [63, 0], [63, 16], [63, 34], [64, 56], [65, 80], [67, 100], [71, 117], [75, 131], [79, 144], [
        83, 156], [85, 167], [83, 178], [79, 191], [73, 206], [66, 223], [63, 240], [63, 255],
    [79, 0], [79, 16], [79, 38], [77, 62], [78, 84], [80, 103], [84, 119], [89, 133], [94, 144], [
        99, 155], [102, 165], [102, 176], [100, 188], [93, 203], [86, 221], [80, 240], [79, 255],
    [95, 0], [95, 18], [92, 42], [90, 65], [90, 86], [91, 103], [95, 118], [101, 131], [108, 142], [
        113, 151], [117, 161], [118, 172], [116, 185], [112, 200], [104, 218], [97, 238], [95, 255],
    [111, 0], [110, 19], [106, 43], [102, 65], [100, 84], [101, 101], [105, 115], [111, 127], [118, 136], [
        126, 145], [130, 155], [131, 167], [131, 180], [127, 196], [121, 215], [114, 236], [111, 255],
    [127, 0], [125, 19], [119, 42], [114, 63], [111, 81], [111, 96], [114, 109], [119, 120], [127, 129], [
        135, 138], [140, 148], [143, 161], [143, 176], [141, 193], [136, 213], [130, 236], [127, 255],
    [143, 0], [141, 18], [135, 40], [128, 60], [124, 77], [123, 91], [125, 103], [129, 112], [135, 121], [
        144, 131], [149, 142], [153, 156], [155, 172], [153, 191], [149, 212], [145, 237], [143, 255],
    [159, 0], [158, 17], [151, 38], [143, 57], [138, 72], [137, 85], [137, 97], [141, 106], [147, 116], [
        154, 126], [159, 139], [164, 153], [166, 170], [165, 190], [163, 213], [160, 238], [159, 255],
    [175, 0], [175, 16], [170, 35], [161, 54], [155, 69], [152, 81], [152, 92], [154, 102], [159, 112], [
        165, 124], [170, 137], [175, 153], [177, 172], [177, 193], [176, 217], [175, 239], [175, 255],
    [191, 0], [191, 16], [189, 33], [182, 51], [175, 66], [170, 79], [169, 90], [171, 101], [174, 112], [
        179, 125], [183, 139], [187, 156], [189, 175], [191, 198], [191, 221], [191, 240], [191, 255],
    [207, 0], [207, 16], [207, 32], [204, 49], [197, 65], [192, 78], [189, 90], [189, 102], [191, 114], [
        195, 128], [199, 144], [202, 162], [205, 182], [206, 204], [207, 224], [207, 240], [207, 255],
    [223, 0], [223, 16], [223, 32], [223, 48], [220, 64], [216, 79], [213, 93], [211, 106], [212, 119], [
        214, 135], [217, 151], [220, 170], [222, 189], [223, 208], [223, 224], [223, 240], [223, 255],
    [239, 0], [239, 16], [239, 32], [239, 48], [239, 64], [238, 80], [237, 95], [235, 110], [235, 125], [
        236, 142], [237, 158], [238, 175], [239, 192], [239, 208], [239, 224], [239, 240], [239, 255],
    [255, 0], [255, 16], [255, 32], [255, 48], [255, 64], [255, 80], [255, 96], [255, 112], [255, 128], [
        255, 144], [255, 160], [255, 176], [255, 192], [255, 208], [255, 224], [255, 240], [255, 255]
]

filename = "distlenna.pgm"
head, lst, dimension = r(filename)

wxy = list()

for x in c(grid, disGrid, 16):
    wxy.append(x)

#x' = w1x+w2y+w3xy+w4
#y' = w5x+w6y+w7xy+w8
lst = Restore(wxy, lst, disGrid, grid, 256, 16)

w(filename, lst, head, dimension)