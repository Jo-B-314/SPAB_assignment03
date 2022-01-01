import numpy as np
from matplotlib import pyplot as plt
import sys

# =============================================================================
# percolation algorithm based on
#  https://www.geeksforgeeks.org/find-whether-path-two-cells-matrix/
# - yellow is the table cloth
# - black is some for liquids unpassable embroidery
# - brown is (obviously) coffee
# =============================================================================

n = 1000
p = 0.6

#path_count = 0

np.random.seed(0)

flag = False

def percolate(matrix,n):
    #flag = False
    # starting at random 1 in matrix at the upside border
    i = np.random.randint(n)
    counter = 0
    # Search at left border for percolatable entry
    while matrix[i][0] != 1:
        i = np.random.randint(n)
        counter += 1
        if counter == n:
            #print("no entry point found")
            break
            
    #print("Starting i:", i)
    global flag
    flag = checkPath(matrix,i,0)
    if flag:
        print("Path found")
        global path_count
        path_count += 1
    else:
        print("no path found")
        

def checkPath(matrix,i,j):

    # if space percolatable
    # last possible case is j = n-1
    if matrix[i][j] == 1:
        matrix[i][j] = 2
        # Base Case: we reached the right border
        if j == n-1 and  matrix[i][j] == 2:
            #print("Base Case")
            global flag
            flag = True
            return True
        # Right Case: only possibiliy to end recursion
        if j < n-1 and matrix[i][j+1] == 1:
             checkPath(matrix, i, j+1)
             if flag:
                 return True
        # Up case
        if i > 0 and matrix[i-1][j] == 1:
             checkPath(matrix, i-1, j)
        # Down case
        if i < n-1 and matrix[i+1][j] == 1:
             checkPath(matrix, i+1, j)

    # if space not percolatable
    else:
        return False
          
#   0: closed edge: yellow
#   1: open edge: brown
#   2: percolated coffee
# Try to walk from left to right


#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True


result_matrix = np.zeros(20)

i = 0
for p in np.arange(0,1,0.05):
    path_count = 0
    for run in range(100):
        print("_________________________")
        matrix = np.random.binomial(1, p, size=(n,n))
        #print("Initial Matrix: \n", matrix)
        percolate(matrix,n)
        #print("Percolated Matrix: \n", matrix)
        #im = plt.imshow(matrix, cmap="copper_r")
        #plt.show()
        print("p:", p)

    result_matrix[i] += path_count
    i+=1
    
print(result_matrix)

