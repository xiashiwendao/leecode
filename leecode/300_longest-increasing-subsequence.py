from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0
    dp = []
    for i in range(len(nums)):
        dp.append(1)
        for j in range(i):
            if nums[i] > nums[j]:
                # 这一步是关键，dp[i]在里层循环的时候可能会被多次更新，i越到后面越大，
                # dp[i]被改写的概率同样越大，这里比较的dp[i]，即当前最大子序列，和d[j]+1谁大
                # 谁大就取谁。因为num[i]>num[j]，所以j位最大子序列一定可以和通过拼接i位字符
                # 组成一个dp[j]+1的子序列，那么剩下的就是和dp[i]到底谁大，谁大取谁。
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lengthOfLIS(nums))
