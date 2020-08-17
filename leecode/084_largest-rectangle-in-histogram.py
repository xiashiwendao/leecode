from matplotlib import pyplot as plt
import pandas as pd

# 暴力计算，两边扩充
def max_area_fist(highs):
    max_area = 0
    index = 0
    for high_length in highs:
        left = right = index

        left_end = right_end = False
        count = 1
        
        for compare_index in range(len(highs)):
            left -= 1
            right += 1
            # 左边过了头
            if(left < 0):
                left_end = True
            else:
                left_value = highs[left]
                if high_length < left_value:
                    count+= 1
                else:
                    left_end = True
            # 右边过了头
            if(right >= len(highs)):
                right_end = True
            else:
                right_value = highs[right]
                if high_length < right_value:
                    count+= 1
                else:
                    right_end = True
            
            # 如果左右两边都到了头，或者两边都碰到了比当前high_length要打的，则跳出
            if(left_end and right_end):
                area = count*high_length
                max_area = max(max_area, area)
                break
            
        # 索引+1
        index+=1
    return max_area

def max_area_stack(lst):
    s = []
    prev_item = 0
    max_area = 0
    for i in range(len(lst)):
        item = lst[i]
        if item > prev_item:
            s.append((i, item))
            prev_item = item
            continue
        if len(s) == 0:
            continue
        
        while(len(s) > 1):
            tmp_pair = s.pop()
            index = tmp_pair[0]
            high = tmp_pair[1]
            if high > item:
                width = i - index
            else:
                # 如果是最后一个则代表当前剩下的是最小的，width=全部；否则是i-index+1
                if i == len(lst) -1:
                    width = len(lst)
                else:
                    continue
            area = width * high
            max_area = max(area, max_area)
            print("index: ", index, "; value is: ", high, "; area is: ", area, "; max is: ", max_area)

        s.append((i, item))
        prev_item = item
    
    return max_area

if __name__ == "__main__":
    lst = [2,1,5,6,2,3,11,7,4,3]
    ret = max_area_stack(lst)
    print(ret)

'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
 

示例:

输入: [2,1,5,6,2,3]
输出: 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''