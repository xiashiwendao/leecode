'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
'''
def max_substring_self(strs):
    hash_pos = dict()
    i = 0 # 慢指针
    j = 0 # 快指针
    max_len = 0
    for pos, char in enumerate(strs):
        # 当前字符已经存在
        if(char in hash_pos):
            char_pos = hash_pos[char]
            max_len = max(max_len, j - i)
            # 重复字符以及前面的字符都要去掉
            for tmp_pos in range(i, char_pos+1):
                tmp_char = strs[tmp_pos]
                hash_pos.pop(tmp_char)

            i = char_pos+1
        # 当前字符不存在
        else:
            # 之前这一步忽略了，一定要记住作为容器，提到了读取就要想到填充，
            # 提到写入就要想到写入，逻辑上面要体现这种闭环，或者说完备性
            hash_pos[char]=j

        j+=1

    max_len = max(max_len, j - i)
    return max_len

def max_substring_2(strs):
    i = 0
    substr=set()
    max_len = 0
    # 前方高能，这里通过遍历是否存在指定字符，而从i的位置开始删除元素，简直不能再赞了！
    for j in range(0, len(strs)):
        special_char = strs[j]
        while(substr.__contains__(special_char)):
            substr.remove(strs[i]) # 注意这里不是删除special char，而是删除第i个字符
            i+=1 # i不断累加，不断删除，直到删除special char

        substr.add(special_char)
        max_len = max(max_len, len(substr))

    return max_len

def max_substring_3(strs):
    char_pos = dict()
    max_len = 0
    start_index = 0
    for end_index in range(0, len(strs)):
        char = strs[end_index]
        if(char_pos.get(char) is not None):
            start_index = max(start_index, char_pos[char]+1) # 注意这里不需要才能够dic中删掉char，因为后面会直接覆盖

        char_pos[strs[end_index]] = end_index
        max_len = max(max_len, end_index - start_index + 1)
    
    return max_len

if __name__ == "__main__":
    max_len = max_substring_3('degfeafeauv')
    print(max_len)
    # d = dict()
    # d['a']='A'
    # d['b']='B'
    # d['c']='C'

    # print('a' in d)
