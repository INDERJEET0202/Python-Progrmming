# There is a given list of lists of integers that represent a grid. with n rows and m columns. A cell is called dormant cell if it has s strictly greater value than the cells around it.Two cells are neighbours when they sahre a common side.or a common corner. So a cell can have at most 8 neighbours.. find the number of dormant cells in the grid.

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    # Write your code here
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][k]
            flag = 1
            for ii in range(max(0,i-1), min(len(grid), i+2)):
                for kk in range(max(0, k-1), min(len(grid[0]), k+2)):
                    if(ii, kk) != (i,k) and val <= grid[ii][kk]:
                        flag = 0
                        break
                if flag == 0:
                    break
            if flag == 1:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()