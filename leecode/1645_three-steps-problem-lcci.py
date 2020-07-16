def stepCaculate(step_num):
    mode = 1000000007
    ret = []
    ret.append(1)
    for i in range(1, step_num+1):
        ret.append(ret[i-1])
        if i >=2: 
            ret[i] = (ret[i]+ret[i-2])%mode
        if i >=3: 
            ret[i] = (ret[i]+ret[i-3])%mode

    return ret[len(ret)-1]
        

if __name__ == "__main__":
    step_name = 5
    step_num = stepCaculate(step_name)

    print(step_num)

'''
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，
计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3 
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''