def binsearch(nums, target, low, high):
    # 注意这里没有“=”，对于“=”场景在下面会一并处理
    if(low > high):
        return -1
    
    middle = low + int((high-low)/2)
    print('middle:', middle,' low:',low, 'high:', high)
    if(nums[middle] == target):
        return middle

    # 如果有low=hight之后，还是没有找到数据，那其实就是没有，即下面的最后一个分支，
    # 因为middle将会-1，所以会出现low-high的情况，于是返回-1
    if(nums[low]<nums[middle]):
        if(nums[low]<=target and nums[middle]>target):
            return binsearch(nums, target, low, middle-1)
        else:
            return binsearch(nums, target, middle+1, len(nums)-1)
    else:
        if(nums[middle]<target and nums[len(nums)-1]>=target):
            return binsearch(nums, target, middle+1, len(nums)-1)
        else:
            return binsearch(nums, target, low, middle-1)

    

def search(nums, target):
    return binsearch(nums, target, 0, len(nums)-1)

if __name__ == "__main__":
    nums = [4,5,6,7,9,1,2,3]
    print(search(nums, 8))