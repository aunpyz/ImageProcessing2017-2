import re
import numpy as np

# only read pgm file
def readfile(filename:str)->tuple:
    '''read given pgm file'''
    col = 0
    row = 0
    lst = list()
    with open(filename, 'rb') as file:
        header = list()
        ls = list()
        # remove first line
        header.append((file.readline()).decode("utf-8"))
        while True:
            line = (file.readline()).decode("utf-8")
            if not line:
                break
            elif(line[0] == '#'):
                continue
            else:
                header.append(line)
                ss = str(line)
                l = re.findall(r'\d+', ss)
                col = int(l[0])
                row = int(l[1])
                break
        header.append((file.readline()).decode("utf-8"))

        n = col*row
        lst = list()
        for i in range(n):
            try:
                lst.append(ord(file.read(1)))
            except:
                pass

    file.close()
    return header, lst, [col, row]

#convert list
def convert(lst:list)->list():
    '''String Unicode to int'''
    l = list()
    for item in lst:
        l.append(ord(item))
    return l

def writeNumeric(filename:str, data:list, header:list, dimension:list):
    '''write pgm file in numeric format (P2 as a header)'''
    # clear file if exists
    name = filename.split('.')
    filename = name[0]+'_out.'+name[1]

    f = open(filename, 'w')
    f.write('')
    f.close()

    col = dimension[0]
    row = dimension[1]

    s = ''
    # write new file
    with open(filename, 'w', encoding='ISO-8859-1') as file:
        header[0] = 'P2\n'
        for h in header:
            # decoding
            s += h
        for i in range(row):
            for j in range(col):
                try:
                    index = i*col + j
                    s += str(data[index])
                    if j < col -1:
                        s += ' '
                except:
                    # print(i)
                    # print(j)
                    pass
            s += '\n'
        file.write(s)
    file.close()

def write(filename:str, data:list, header:list):
    # clear file if exists
    name = filename.split('.')
    filename = name[0]+'_out.'+name[1]

    f = open(filename, 'w')
    f.write('')
    f.close()

    s = ''
    # write new file
    with open(filename, 'w', encoding='ISO-8859-1') as file:
        for h in header:
            # decoding
            s += h
        for d in data:
            s += str(d)

        file.write(s)
    file.close()