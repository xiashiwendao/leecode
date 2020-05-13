'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import math
def findKth(num1, l1, h1, num2, l2, h2, k):
    m = h1 - l1 + 1
    n = h2 - l2 + 1
    if(m > n):
        return findKth(num2, l2, h2, num1, l1, h1, k)
    if(m == 0):
        return num2[l2 + k -1]
    if(k == 1):
        return min(num1[l1], num2[l2])

    na = min(math.ceil(int(k/2)), m)
    nb = k - na
    va = num1[l1 + na -1]
    vb = num2[l2 + nb -1]
    if(va == vb):
        return va
    elif(va<vb):
        return findKth(num1, l1+na, h1, num2, l2, l2 + nb -1, k-na)
    else:
        return findKth(num1, l1, l1+na-1, num2, l2+nb, h2, k-nb)

def findMedianSortedArray(num1, num2):
    m = len(num1)
    n = len(num2)
    k = int((m+n)/2)

    if (m+n)%2 == 1:
        return findKth(num1, 0, m-1, num2, 0, n-1, k+1)
    else:
        return (findKth(num1, 0, m-1, num2, 0, n-1, k)+ findKth(num1, 0, m-1, num2, 0, n-1, k+1))/2

if __name__ == "__main__":
    # nums1 = [1, 3]
    # nums2 = [2]
    nums1 = [1, 2]
    nums2 = [3, 4]
    ret = findMedianSortedArray(nums1, nums2)
    print('median number: ', ret)
    # print(math.ceil(1/2))
    
    
