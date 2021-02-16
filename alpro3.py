# Program to multiply two matrices using list comprehension

# 2x3 matrix
X = [[1,3],
    [4 ,1],
    [2 ,5]]

# 3x2 matrix
Y = [[3,-1,1],
    [0,2,1]]

# result is 3x3
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)
