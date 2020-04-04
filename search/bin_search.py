def bin_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] > target:
            right=mid-1
        elif arr[mid] < target:
            left=mid+1
        else:
            print('find the value %s, index is: %s'%(target, mid))
            return True
    
    return False

def bin_searc_rec(arr, target, left, right):
    print('left is: %s, right is: %s, data is: %s'%(left, right, arr))
    ret = 0
    if(left>right): # 这个地方注意不包括=，只有大于
        print('can\'t find the data:', target)
        return None
    mid = (left+right)//2
    if(arr[mid]>target):
        right=mid-1
    elif arr[mid]<target:
        left=mid+1
    else:
        return mid

    ret= bin_searc_rec(arr, target, left, right)
    print('find the value index is: ', ret)

    return ret



if __name__ == "__main__":
    l= [1,3,4,5,6,7,8]
    # bin_search(l, 8)
    left, right = 0, len(l)-1
    bin_searc_rec(l, 8, left, right)