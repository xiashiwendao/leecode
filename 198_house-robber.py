from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        result = []
        for i in range(0, len(nums)):
            if i <= 1:
                result.append(nums[i])
            elif i == 2:
                result.append(nums[0]+nums[2])
            else:
                span_one = result[i-2]
                span_two = result[i-3]
                max_value = max(span_one, span_two)
                
                result.append(max_value + nums[i])

        return sorted(result)[-1]

    def rob2(self, nums):
        preMax = 0 # i-2轮的max值
        currMax = 0 # i-1轮的max值
        for i in range(len(nums)):
            tmp = currMax
            # 事前判断，如果我这一家动手的话，获得的是i家和i-2家的累计收入；如果不动手，将会获得
            # i-1家累计的金币，所以需要衡量一下到底哪一个划算，如此，一直到最后一家
            # 这里preMax和currMax难道不是同一个值吗？不是，其实是result[i-2]好result[i-1]的值
            # 只不过这里没有用一个list全部存储，只是存储了i-1值和i-2的值，当然这样也就足够了。
            currMax = max(preMax + nums[i], currMax)
            preMax = tmp

        return currMax

if __name__ == "__main__":
    # lst = [1,2,3,1]
    lst = [2,7,9,3,1]
    s = Solution()
    # amount = s.rob(lst)
    amount = s.rob2(lst)
    print(amount)

