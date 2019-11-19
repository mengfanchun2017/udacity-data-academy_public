# import
import numpy as np

# set env
red = 8
blue = 3
yellow = 2
full = red + blue + yellow

# get p
pred = red / full
pblue = blue / full
pyellow = yellow / full
print('\n--- p resultes ---')
print(pred, pblue, pyellow)

# entropy
e = - pred*np.log2(pred) - pblue*np.log2(pblue) - pyellow*np.log2(pyellow)
print('\n--- e resultes ---')
print(e)