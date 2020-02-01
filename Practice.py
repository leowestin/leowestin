X = [[5, 4, 3], 
     [3, 6, 7],
     [2, 5, 8]]


Y = [[1, 3, 7],
     [4, 3, 1],
     [6, 9, 6]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result: 
    print(r)












