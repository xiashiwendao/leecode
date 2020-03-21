def partition(arr, startIndex, endIndex):
    left = startIndex
    right = endIndex
    pivot = arr[endIndex]
    while(left != right): # error:left<right
        while(left < right and arr[left] < pivot): # question: why left first,how about right?
            left+=1
        while(left < right and arr[right] >= pivot): # 这个等号精妙，直接跳过tail了，少了一步赋值right-1
            right-=1
        # 这个地方是否需要考虑判断left=right？确实需要判断
        if(left<right):
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
    
    arr[endIndex]=arr[left]
    arr[left] = pivot

    return left

def quick_sort(arr, startIndex, endIndex):
    if(startIndex >= endIndex):
        return arr
    
    pivot_index = partition(arr, startIndex, endIndex)

    quick_sort(arr, startIndex, pivot_index-1)
    quick_sort(arr, pivot_index+1, endIndex)

    return arr

if __name__ == "__main__":
    data=[4,3,8,4,6,2,0]
    data_sorted = quick_sort(data,0, len(data)-1)
    print(data_sorted)