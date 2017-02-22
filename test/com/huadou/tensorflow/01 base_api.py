import tensorflow as tf

import  numpy as np

import  nltk

nltk.download()
# 1.12.0 version
print(np.__version__)

# help(np.arange)

# Examples
# --------
# >> > np.arange(3)
# array([0, 1, 2])
# >> > np.arange(3.0)
# array([0., 1., 2.])
# >> > np.arange(3, 7)
# array([3, 4, 5, 6])
# >> > np.arange(3, 7, 2)
# array([3, 5])


print(np.arange(3))

print(np.arange(0,3))

print(np.arange(0,100,10,dtype=int))

data = np.arange(24).reshape(2,3,4)

print("data:",data)

