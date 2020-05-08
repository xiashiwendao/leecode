def findKth(num1, l1, h1, num2, l2, h2, k):
    m = h1 - l1 + 1
    n = h2 - l2 + 1
    if(m > n):
        return findKth(num2, l2, h2, num1, l1, h1, k)
    if(m = 0):
        return num2[l2 + k -1]
    if(k = 1):
        return min(num1[l1], num2[l2])


def findMedianSortedArray(num1, num2):
    m = len(num1)
    n = len(num2)
    k = int((m+n)/2)

    if (m+n)%2 == 1:
        retrun findKth(num1, 0, m-1, num2, 0, n-1, k)
    else:
        return (findKth(num1, 0, m-1, num2, 0, n-1, k)+ findKth(num1, 0, m-1, num2, 0, n-1, k))/2