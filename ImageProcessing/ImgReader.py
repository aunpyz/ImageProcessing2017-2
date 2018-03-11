import re
import collections

n = 0
col = 0
row = 0
lst = list()
# read file in binary
with open('scaled_shapes.pgm','rb') as file:
    # remove first line
    line = file.readline()
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
            ss = str(line)
            l = re.findall(r'\d+', ss)
            col = int(l[0])
            row = int(l[1])
            break
    line = file.readline()

    for i in range(row):
        l = list()
        for j in range(col):
            c= file.read(1)
            if not c:
                break
            data = ord(c)
            l.append(data)
            n = n + 1
        lst.append(l)
        l.clear

dtc = dict()
        
print(n)
for i in lst:
    for j in i:
        dtc[j] = dtc.setdefault(j, 0) +1

# 1.1 histogram
# od = collections.OrderedDict(sorted(dtc.items()))

# count = 0
# for key, val in od.items():
#     print(str(key)+'\t'+str(val))
#     count += val
# print(count)

# 1.2 object's moment


# get key
input()