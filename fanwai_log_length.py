'''
有一段不知道具体长度的日志文件，里面记录了每次登录的时间戳，已知日志是按顺序从头到尾记录的，
没有记录日志的地方为空，要求当前日志的长度。
'''

import math
import numpy as np
def binextend_log(lines, high):
    # print('binextend_log [high]: ', high)
    lines_size = len(lines)
    high_ext = high*2
    index = min(high_ext, lines_size)
    print('binextend_log [high]: %s, [high_ext]: %s, index: %s'%(high, high_ext, index))
    # 已经发现了边界范围，下面是要缩小范围
    if(lines[index] == 0):
        return binsearch_log(lines, high, index)
    # 还是没有发现，继续扩大查找范围
    else:
        return binextend_log(lines, high_ext)

def binsearch_log(lines, low, high):
    print('binsearch_log, low: %s, hight: %s' %(low, high))
    middle = low + (high-low)//2
    if(lines[middle]==1 and lines[middle+1] ==0):
        return middle

    if(lines[middle]==1):
        return binsearch_log(lines, middle, high)
    else:
        return binsearch_log(lines, low, middle)

if __name__ == "__main__":
    lines = np.zeros((1000,))
    lines_fill = np.ones((100,))
    lines[0:100] = lines_fill
    last_index = binextend_log(lines, 1)
    print('length is: ', last_index+ 1)
