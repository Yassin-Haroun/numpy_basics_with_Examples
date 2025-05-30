#import numpy as np
#Numpy Basics:
#********************************************************************************
#np.zeros((rows,culomns)) --> matrix from zeros rows , culomns
#--------------------------------------------------------------------------------
#np.zeros((num)) --> matrix from zeros numers
#--------------------------------------------------------------------------------
#np.ones((rows,culomns)) --> matrix from ones rows , culomns
#--------------------------------------------------------------------------------
#np.ones((num)) --> matrix from ones numers
#--------------------------------------------------------------------------------
#np.array(list) --> convert to matrix
#--------------------------------------------------------------------------------
#np.arange(from,to) --> matrix from ... to...
#--------------------------------------------------------------------------------
#np.random.randint(from,to,num) --> random integer
#--------------------------------------------------------------------------------
#np.random.randint(1,20,(5,5)) --> random integer rows culomns
#--------------------------------------------------------------------------------
#np.random.rand(from,to,num) --> random from zero to one
#--------------------------------------------------------------------------------
#x.reshape(2,5) --> convert to matrix (rows , culomns)
#--------------------------------------------------------------------------------
#rows * culomns = num
#--------------------------------------------------------------------------------
#np.random.shuffle(x) --> random change
#--------------------------------------------------------------------------------
#reshaped.max() --> max num
#--------------------------------------------------------------------------------
#reshaped.min() --> min num
#--------------------------------------------------------------------------------
#reshaped.mean() --> mean
#--------------------------------------------------------------------------------
#reshaped.shape() --> shape
#--------------------------------------------------------------------------------
"""
Example:

array = np.arange(1,19)
reshaped = array.reshape(3,6)
np.random.shuffle(reshaped)
print(reshaped)

maxmum = reshaped.max()
minmum = reshaped.min()
mean = reshaped.mean()
shape = reshaped.shape
rows = reshaped.shape[0]
culomns = reshaped.shape[1]

print("\n")
print("The maxmum is : " + str(maxmum))
print("\n")
print("The minmum is : " + str(maxmum))
print("\n")
print("The mean is : " + str(mean))
print("\n")
print("The shape is : " + str(shape))
print("\n")
print("The rows is : " + str(rows))
print("\n")
print("The culomns is : " + str(culomns))
print("\n")
"""
#--------------------------------------------------------------------------------

#np.ceil(2.3) --> round to up
#np.floor(2.3) --> round to low
#np.round(2.3) --> low or up

"""
Example:
np1 = np.floor(2.6)
print(np1)

>>>2.0

np1 = np.ceil(2.6)
print(np1)

>>>3.0

np1 = np.round(2.6)
print(np1)

>>>3.0

"""
#--------------------------------------------------------------------------------
#np.add() --> add
#--------------------------------------------------------------------------------
#np.multiply --> multiply
#--------------------------------------------------------------------------------
#np.divide() -- > divide
#--------------------------------------------------------------------------------

"""
Examlpe:
matrix1 = np.arange(0,15)
rematrix1 = matrix1.reshape(3,5)
print("matrix1\n")
print(rematrix1)
print("\n")
print("*"*50)
print("\n")
print("matrix2\n")
matrix2 = np.arange(15,30)
rematrix2 = matrix2.reshape(3,5)
print(rematrix2)
print("\n")
print("*"*50)
print("\n")

multiply = np.multiply(rematrix1,rematrix2)
print("\n")
print("multiply Matrix1 & Matrix2\n")
print(multiply)
print("\n")
print("*"*50)
add = np.add(rematrix1,rematrix2)
print("\n")
print("add Matrix1 & Matrix2\n")
print(add)
print("\n")
print("*"*50)
divide = np.divide(rematrix1,rematrix2)
print("\n")
print("divide Matrix1 & Matrix2\n")
print(divide)
print("\n")
print("*"*50)

"""
#--------------------------------------------------------------------------------
#********************************************************************************


