from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        '''K代表的是窗口大小'''
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        def clean_deque(i):
            # remove indexes of elements not from sliding window
            # 这里i-k代表的就是如果队首元素是当前元素的窗口大小前元素，则弹出
            # 所有的队首元素都是当前窗口的最大元素
            
            # 在python里面，deq的默认函数就是isempty()
            # popleft是将队首元素弹出，这里i-k是指满足了一个窗口滑动完毕，
            # 在将要滑动到下一个下一个窗口的时候，或者说将要放入新的窗口原酸的时候，将当前窗口的首元素弹出
            if deq and deq[0] == i - k:
                deq.popleft()
                
            # remove from deq indexes of all elements 
            # which are smaller than current element nums[i]
            # 当前窗体遗留元素（k-1个）逐个和将要放入的新元素比较（这里是和数组和队列元素比较）
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        # init deque and output
        deq = deque()
        max_idx = 0
        # 把第一波前K个元素放入到队列中
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]
        
        # 滑动到后面窗口，之后的每个窗口只需要放入一个元素（因为只是向后滑动了一个元素）
        # build output
        for i in range(k, n):
            clean_deque(i)          
            deq.append(i)
            output.append(nums[deq[0]])
        return output