def swap(nums, index_1, index_2):
    temp = nums[index_1]
    nums[index_1] = nums[index_2]
    nums[index_2] = temp

pivot = 0
def quickSelect(nums, low, high, k):
    pivot = low
    base_value = nums[high]
    for j in range(low, high):
        if nums[j] <= base_value:
            swap(nums, pivot, j)
            pivot += 1
    
    swap(nums, pivot, high)

    count = high-low+1
    if count == k:  
        return nums[pivot]
    if count > k:
        return quickSelect(nums, pivot+1, high, k)
    else:
        return quickSelect(nums, low, pivot-1, k-count)


def findKthLargest(nums, k):
    return quickSelect(nums, 0, len(nums) -1, k)

if __name__ == "__main__":
    nums1 = [2, 5, 3, 1, 6]
    nums2 = [8, 9, 7, 4]
    nums1.extend(nums2)
    k = 7
    ret = findKthLargest(nums1, k)
    print('the %s largets num is: %s' %(k, ret))




