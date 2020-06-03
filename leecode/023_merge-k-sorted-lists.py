'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
from heapq import heappop

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        fakeHead = ListNode(0)
        p = fakeHead
        heap =[]
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        
        while len(heap) > 0:
            node = ListNode(heappop(heap))
            p.next = node
            p = p.next

        return fakeHead
if __name__ == "__main__":
    lst1 = ListNode(1)
    lst1.next = ListNode(4)
    lst1.next.next = ListNode(5)

    lst2 = ListNode(1)
    lst2.next = ListNode(3)
    lst2.next.next = ListNode(4)

    lst3 = ListNode(2)
    lst3.next = ListNode(6)

    lst = [lst1, lst2, lst3]

    sol = Solution()
    node = sol.mergeKLists(lst)

    while node.next:
        node = node.next
        print(node.val)