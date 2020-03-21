import math
def sort(arr):
    print('sort data arr: ', arr)
    if(len(arr)==1):
        print('sort data just single element: ', arr)
        return arr
    
    mid=math.floor(len(arr)/2)
    left = arr[0:mid]
    right = arr[mid:]
    print('data splited by left: %s, right: %s'%(left, right))
    sorted_left = sort(left)
    sorted_right= sort(right)
    merged_data = merge(sorted_left, sorted_right)
    print('merged data: ', merged_data)
    
    return merged_data
    # return merge(sort(left), sort(right))
    

def merge(left, right):
    print('left: ', left, 'right: ', right)
    result=[]
    while(left and right):
        if(left[0]>right[0]):
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    
    while(left):
        result.append(left.pop(0))
    
    while(right):
        result.append(right.pop(0))

    return result

if __name__ == "__main__":
    arr=[4,9,8,3,7,2,6]
    # arr=[7,2,6]
    sorted_arr = sort(arr)
    print(sorted_arr)

