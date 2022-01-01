import numpy as np
from matplotlib import pyplot as plt
import sys

# =============================================================================
# percolation algorithm based on
#  https://www.geeksforgeeks.org/find-whether-path-two-cells-matrix/
# - brown is the table cloth
# - yellow is some for liquids unpassable embroidery
# - black is (obviously) coffee
# Coffee is trying to percolate from left to right
# =============================================================================

# =============================================================================
# It is absolutely possible to run this with matplotlib-lines activated but
# make sure you have some time ^^
# =============================================================================

# =============================================================================
# Output for n = 100 and T = 100 and p = 0.01,0.02,...0.99
#[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.
#  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.
#  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.
#  0.  0.  0.  0.  0.  0.  0.  0.  2. 27. 50. 63. 56. 65. 56. 64. 60. 75.
# 69. 75. 67. 69. 72. 77. 79. 91. 83. 76. 76. 81. 83. 82. 83. 89. 83. 90.
# 91. 89. 90. 94. 98. 97. 96. 96. 99. 99.]
# These are the amounts how often the tea can percolate all the way through in
# 100 tries.
# So the upper threshold would be 0.98 and the lower threshold would be 0.6.
# =============================================================================

n = 1000
#p = 0.6

#path_count = 0

np.random.seed(0)

flag = False

def percolate(matrix,n):
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


#plt.rcParams["figure.figsize"] = [7.00, 3.50]
#plt.rcParams["figure.autolayout"] = True


result_matrix = np.zeros(100)

i = 0
for p in np.arange(0,1,0.01):
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

