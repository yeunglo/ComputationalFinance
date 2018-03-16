#!python3
#code=utf-8
import numpy as np

a = np.array([2,23,4])  # list 1d
print(a)
# [2 23 4]

#data type: dtype
a = np.array([2,23,4],dtype=np.int)
print(a.dtype)
# int 64
a = np.array([2,23,4],dtype=np.int32)
print(a.dtype)
# int32
a = np.array([2,23,4],dtype=np.float)
print(a.dtype)
# float64
a = np.array([2,23,4],dtype=np.float32)
print(a.dtype)
# float32

# create special type of array
a = np.array([[2,23,4],[2,32,4]])  # 2d 2X3
print(a)
"""
[[ 2 23  4]
 [ 2 32  4]]
"""

# array with all zero
a = np.zeros((3,4)) # all zero, 3X4
"""
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])
"""
# all one and set the data type with dtype:
a = np.ones((3,4),dtype = np.int)   # all one, 3X4, int
"""
array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])
"""

#all empty, actually very close to zero
a = np.empty((3,4)) # empty, 3X4
print(a)
"""
array([[  0.00000000e+000,   4.94065646e-324,   9.88131292e-324,
          1.48219694e-323],
       [  1.97626258e-323,   2.47032823e-323,   2.96439388e-323,
          3.45845952e-323],
       [  3.95252517e-323,   4.44659081e-323,   4.94065646e-323,
          5.43472210e-323]])
"""

# range: continual array
a = np.arange(10,20,2) # range: 10-19, steps: 2
"""
array([10, 12, 14, 16, 18])
"""

# reshape: change shape of data
a = np.arange(12).reshape((3,4))    # 3X4, 0-11
"""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
"""

# linspace: line data
a = np.linspace(1,10,20)    # 1-10, divided into 20 data points and make line
"""
array([  1.        ,   1.47368421,   1.94736842,   2.42105263,
         2.89473684,   3.36842105,   3.84210526,   4.31578947,
         4.78947368,   5.26315789,   5.73684211,   6.21052632,
         6.68421053,   7.15789474,   7.63157895,   8.10526316,
         8.57894737,   9.05263158,   9.52631579,  10.        ])
"""

#reshape line:
a = np.linspace(1,10,20).reshape((5,4)) # reshape
"""
array([[  1.        ,   1.47368421,   1.94736842,   2.42105263],
       [  2.89473684,   3.36842105,   3.84210526,   4.31578947],
       [  4.78947368,   5.26315789,   5.73684211,   6.21052632],
       [  6.68421053,   7.15789474,   7.63157895,   8.10526316],
       [  8.57894737,   9.05263158,   9.52631579,  10.        ]])
"""