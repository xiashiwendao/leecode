class LISRecursion{
    // 定义一个静态变量 max，用来保存最终的最长的上升子序列的长度
    static int max;
    public int f(int[] nums, int n) {

        if (n <= 1) {
            return n;
        }
    
        int result=0;
        int maxEndingHere=1; // 以当前数结尾的上升子序列的最长长度
        // 从头遍历数组，递归求出以每个点为结尾的子数组中最长上升序列的长度
        for (int i=1; i < n; i++) {
            result=f(nums, i);

            if (nums[i−1] < nums[n−1] && result + 1 > maxEndingHere) {
                maxEndingHere=result + 1;
            }
        }

        // 判断一下，如果那个数比目前最后一个数要小，那么就能构成一个新的上升子序列 
        if (max < maxEndingHere) {
            max=maxEndingHere;
        }

        // 返回以当前数结尾的上升子序列的最长长度
        return maxEndingHere;
    }
    public int LIS(int[] nums) {
        max=1;
        f(nums, nums.length);
        return max; 
    }
}
