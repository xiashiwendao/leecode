
import math
import numpy as np
count = 0
def check(row_num, col_num, row_col):
    '''
    放置的当前列，不能有皇后，放置的当前位置的斜角（45°）不能有皇后
    '''
    for row_index in range(row_num):
        if(row_col[row_index]==col_num or row_num - row_index==abs(col_num - row_col[row_index])):
            return False
    
    return True

def backTracing(n, row_index, columns):
    global count
    if(row_index == n):
        count=count+1
        return
    check_flag = False
    # n皇后问题，行列都是n，这里的n代表列，尝试将皇后放置在该行（row_index)的每一个（列）位置
    for i in range(n):
        if(check(row_index, i, columns)):
            check_flag = True
            columns[row_index]=i
            backTracing(n, row_index+1, columns)
    
    if(check_flag==False):
        columns[row_index]=-1

def totalNQueues(n):
    row_col = np.zeros((n,))
    print(row_col)
    backTracing(n, 0, row_col)

    return count

if __name__ == "__main__":
    print('total solution count: ', totalNQueues(8))
