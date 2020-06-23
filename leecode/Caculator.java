public class Caculator{
    // 转换，将字符串的字符放入到一个优先队列中
int calculate(String s) {
        Queue<Character> queue = new LinkedList<>();
        for (char c : s.toCharArray()) {
            queue.offer(c);
        }
     
        // 定义两个变量，num 用来表示当前的数字，sum 用来记录最后的和 
        int num = 0, sum = 0;
     
        // 遍历优先队列，从队列中一个一个取出字符 
        while (!queue.isEmpty()) {
            char c = queue.poll();
    
            // 如果当前字符是数字，那么就更新 num 变量，如果遇到了加号，就把当前的 num 加入到 sum 里，num 清零
            if (Character.isDigit(c)) {
                num = 10 * num + c - '0';
            } else {
                sum += num;
                num = 0;
            }
        }
      
        sum += num; // 最后没有加号，再加一次
    
        return sum;
      
    }
}