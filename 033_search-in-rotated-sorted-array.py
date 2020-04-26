'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
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