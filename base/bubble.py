def sort(data_raw):
    size=len(data_raw)
    data=data_raw.copy()
    
    sortFlag = True
    # 两层遍历，外层是逐个元素进行为起点，里层则是从起点到结尾，两两比较，大的排后面
    # 每次排序都可以保证最后面的是最大值，所以每一轮排序到最后的，不需要再进行参与排序；
    # 这意味着每次处理的都是一个子数据集；
    for i in range(size):
        if not sortFlag:
            break

        sortFlag=False
        for j in range(size-i-1):
            if(data[j]>data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
                
                sortFlag=True
    return data

# 这里endIndex就是len(data)-1，正常遍历一组数据应该是len(data)，但是
# 这个函数里面实现的data[i]和data[i+1]的比较，所以
def sort_rec(data, endIndex):
    if(endIndex==0):
        return data

    sort_flag=False
    for i in range(0, endIndex):
        if(data[i]>data[i+1]):
            data[i], data[i+1] = data[i+1], data[i]
            sort_flag=True
    
    if(sort_flag):
        data = sort_rec(data, endIndex-1)
    
    return data

if __name__ == "__main__":
    data=[4,2,5,8,3,2,7]
    # data=[1,2,3,4,5]
    # data=[5,4,3,2,1]
    # data_sorted=sort(data)
    data_sorted=sort_rec(data, len(data)-1)
    print(data_sorted)

    print(list(range(0, 5)))
