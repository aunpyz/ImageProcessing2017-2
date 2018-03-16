import numpy as np
from matplotlib import pyplot as plt
from ImgReader import readfile as r, writeNumeric as w

filename = "scaled_shapes.pgm"
head, lst, dimension = r(filename)
w(filename, lst, head, dimension)

plt.hist(lst)
plt.show()