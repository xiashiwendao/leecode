def move_left(data, index, p_value, r_index):
    for i in range(index, len(data)):
        current_value = data[i]
        l_index=i
        l_value=current_value
        meet_flag = l_index==r_index
        if current_value > p_value:
            print('find the left point value: ', current_value)
            break

def quick_sort(data_raw):
    data=data_raw.copy()
    data_len=len(data)
    p_index=data_len-1
    p_value=data[p_index]
    print('++++ 处理序列:', data_raw, 'pivot value:', p_value)
    l_index=0
    r_index=p_index-1
    meet_flag=False
    print('++++ start move left point...')
    # left point go through
    for i in range(data_len):
        current_value = data[i]
        l_index=i
        l_value=current_value
        meet_flag = l_index==r_index
        if current_value > p_value:
            print('find the left point value: ', current_value)
            break
    
    if not meet_flag:
        print('left point don\'t meet right point, next moving right point...')
        # 每到一个分支都要考虑一下是否需要初始化一下标志位；
        # 每个分支都是一个独立的世界，里面要独立发生一些事情；
        # 所以初始化一定要考虑这个其实就像你床架一个类需要初始化一样
        meet_flag=False # flag init--which is very important!
        for i in range(data_len-2, -1, -1):
            current_value = data[i]
            r_index=i
            r_value=current_value
            meet_flag=l_index==r_index
            if current_value < p_value or meet_flag:
                print('fined the right point value: ', current_value)
                break
        
        # right point don't meet left point
        if not meet_flag:
            print('right point do not meet the left point, swap the left value and right value')
            # not meet, swap the data
            data[l_index] = r_value
            data[r_index] = l_value
        # right point move and meet left poin, 
        # which means rightpoint may in the first postion at last
        else:
            print('right point meet the left point which means, need check right point-first postion')
            # 右节点遍历到了头位置，说明pivot就是最小值，和首元素交换，并设置l_index和r_index
            if r_index==0:
                print('oooo, r point just at the head, so swap the tail and head value')
                temp = data[0]
                last_index = len(data)-1
                data[0] = data[last_index]
                data[last_index]=temp
                l_index = r_index= 0 # 用于后续拆分
    # if meet, which means left point may postion last
    else:
        print('left point meet the right point, need check if left point at the tail position')
        # 如果左节点遍历到了最后的位置，说明pivot就是最大值直接设置l_index和r_index
        last_index = len(data)-1
        if l_index==[last_index]:
            print('oooooo, left point just at the tail position, reset the l_index & r_index')
            l_index=r_index=last_index # 用于后续拆分
    
    # anyway, need to check if reach to left point, if not come on to sort
    print('after sort, data is: ', data)
    print('anyway, need to check if reach to left point, if not come on to sort')

    sub_data_left = data[0:l_index]
    sub_data_right = data[l_index+1:data_len]
    if len(sub_data_left)>1:
        print(':), left part need iteration')
        quick_sort(sub_data_left)
    if len(sub_data_right)>1:
        print(':), right part need iteration')
        quick_sort(sub_data_right)

    return data

if __name__ == "__main__":
    data=[4,3,8,4,6,2,0]
    data_sorted = quick_sort(data)
    print(data_sorted)


    
    

    
