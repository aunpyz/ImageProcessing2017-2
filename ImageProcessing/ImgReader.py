import re
import collections

col = 0
row = 0
lst = list()
# read file in binary
def read(filename):
    with open(filename,'rb') as file:
        header = list()
        ls = list()
        # remove first line
        header.append(file.readline())
        while True:
            line = file.readline()
            if not line:
                # end of file
                break
            elif (chr(line[0]) == '#'):
                # cast to character
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

        while True:
            c = file.read(1)
            if not c:
                # end of file
                break
            ls.append(ord(c))
        
        # output file name
        name = filename.split('.')
        filename = name[0]+'_out.'+name[1]

        write(filename, ls, header)
    file.close()
    return ls

def write(filename, data, header):
    # clear file if exists
    f = open(filename, 'w')
    f.write('')
    f.close()

    # write new file
    with open(filename, 'a', encoding='ISO-8859-1') as file:
        for h in header:
            # decoding
            file.write(str(h, 'utf-8'))
        for d in data:
            file.write(chr(d))
    file.close()

lst = read('scaled_shapes.pgm')
dtc = dict()

for i in lst:
    dtc[i] = dtc.setdefault(i, 0) +1

# 1.1 histogram
od = collections.OrderedDict(sorted(dtc.items()))

count = 0
for key, val in od.items():
    print(str(key)+'\t'+str(val))
    count += val
print(count)

# 1.2 object's moment