import re
import collections

col = 0
row = 0
lst = list()
# read file in binary
def read(filename):
    with open(filename, encoding='ISO-8859-1') as file:
        header = list()
        ls = list()
        # remove first line
        header.append(file.readline())
        while True:
            line = file.readline()
            if not line:
                # end of file
                break
            elif (line[0] == '#'):
                # skip comment line
                continue
            else:
                # until getting picture's dimension
                header.append(line)
                ss = str(line)
                l = re.findall(r'\d+', ss)
                col = int(l[0])
                row = int(l[1])
                break
        header.append(file.readline())

        lines = file.readlines()
        l = list()
        for line in lines:
            for word in line:
                l.append(ord(word))

    #     while True:
    #         c = file.read(1)
    #         if not c:
    #             # end of file
    #             break
    #         data = int(ord(c)) + 10

    #         # clamp to 255
    #         if data > 255:
    #             data = 255
    #         ls.append(data)
        
        # output file name
        name = filename.split('.')
        filename = name[0]+'_out.'+name[1]

        write(filename, l, header)
    file.close()
    # return ls

def write(filename, data, header):
    # clear file if exists
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
            s += ' '
        file.write(s)
    file.close()

# 1 histogram & object moment
# lst = read('scaled_shapes.pgm')
# dtc = dict()

# for i in lst:
#     dtc[i] = dtc.setdefault(i, 0) +1

# 1.1 histogram
# od = collections.OrderedDict(sorted(dtc.items()))

# count = 0
# for key, val in od.items():
#     print(str(key)+'\t'+str(val))
#     count += val
# print(count)

# 1.2 object's moment

# 2 point operations
#read('SEM256_256.pgm')
read('SEM256_256.pgm')