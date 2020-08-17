package leecode;

import java.util.Stack;

public class largest_rectangle_in_histogram {
    // 将输入数组的长度记为 n，初始化最大面积 max 为 0
    int largestRectangleArea(int[] heights) {
        int n = heights.length, max = 0;

        // 定义一个堆栈 stack 用来辅助计算
        Stack<Integer> stack = new Stack<>();

        // 从头开始扫描输入数组
        for (int i = 0; i <= n; i++) {
            while (!stack.isEmpty() && (i == n || heights[i] < heights[stack.peek()])) {
                int height = heights[stack.pop()];
                int width = stack.isEmpty() ? i : i - 1 - stack.peek();

                max = Math.max(max, width * height);
            }

            stack.push(i);
        }
        // 返回面积最大值
        return max;
    }

    public static void main(String[] args) {

    }
}