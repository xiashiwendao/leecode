# 这个版本实现有问题，因为没有考虑到正则匹配的前匹配性；
# 即模式中.*md可能会匹配abcdef，但是模式中其实还是要求结尾是md
def regular_analysis_ver1(s, p):
    if len(s) == 0 or len(p)==0:
        return False

    ret = True
    pre_p_ch = ''
    p_pos = 0
    for index in range(len(s)):
        if not ret:
            break
        # 首字母分析是否为“.”
        if index==0:
            p_ch_first = p[0]
            if p_ch_first == '.':
                continue
            else:
                if len(p) > 1:
                    p_next = p[p_pos]
                    if p_next == "*":
                        ret = True
                    else:
                        ret = p_ch_first == s[0]
                else:
                    ret = p == s
                    return ret
        # 后续字母处理
        else:
            ch = s[index]
            if pre_p_ch == "*":
                # *匹配
                if p[p_pos -1] == ch:
                    ret = True
                # *无法匹配，则取出下一个p的字符，看看是否匹配
                else:
                    p_pos += 1
                    ret = p[p_pos] == ch
            else:
                p_pos += 1
                # 如果p当前字符为*，用s中当前字符和P的*的前一个字母进行比较
                if p[p_pos] == "*":
                    if pre_p_ch == ".":
                        ret = True
                    else:
                        ret = pre_p_ch == ch
                # 如果是“."，则匹配任意字符
                elif p[p_pos] == ".":
                    ret = True
                # 正常字符，则直接比较
                else:
                    ret = p[p_pos] == ch

        pre_p_ch = p[p_pos]

    return ret

# 第二个版本，首先进行后匹配，只有后匹配都OK了再进行前向匹配
# 正则表达式的关键要理解模式字符串一个位置是可以匹配多个字符，
# 如果不匹配则向后查找是否有匹配的
def regular_analysis(s, p):
    match = True
    p_list = list(p)
    s_list = list(s)
    # p_tail = p_list.pop()
    same = True
    while(same):
        p_tail = p_list.pop()
        if not p_tail.isalpha():
            p_list.append(p_tail)
            break

        s_tail = s_list.pop()
        same = s_tail == p_tail

    # 逐个比较发现完全一致
    if len(p_tail) == 0 and same and len(s_tail) == 0:
        match =True
    # 如果尾部字母有不一致情况，返回False
    elif not same:
        match = False
    else:
        p_pos = 0
        p_ch = p_list[p_pos]
        for s_pos in range(len(s_list)):
            if not match:
                break
            s_ch = s_list[s_pos]
            p_ch = p_list[p_pos]
            if s_ch == p_ch:
                match = True
                p_pos += 1
            else:
                if p_ch == "*":
                    # 取出前一个字符，看看是否匹配
                    if p_list[p_pos-1] == s_ch:
                        match = True
                    elif p_list[p_pos-1] == ".":
                        match = True
                    # 前字符不匹配，则取出模式后一个字符，看是否匹配
                    else:
                        p_pos += 1
                        if p_list[p_pos] == ".":
                            match = True
                        else:
                            match = p_list[p_pos] == s_ch
                        p_pos += 1 # 只是match=True有意义
                elif p_ch == ".":
                    match= True
                    p_pos +=1
                # 非特殊字符的比较
                else:
                    # 首先判断模式前一个字符是否为*
                    if p_list[p_pos-1] == "*":
                        match=True
                    # 字符间比较
                    else:
                        match = p_ch == s_ch
                        p_pos +=1 # 只是match=True有意义

    return match

if __name__ == "__main__":
    # s = 'ab'
    # p = '.*'
    # s = 'ab'
    # p = 'a*'
    # s = "aab"
    # p = "c*a*b"
    s = "mississippi"
    p = "mis*is*ip*."
    ret = regular_analysis(s, p)
    if(ret):
        print('match!')
    else:
        print('NG match!')


'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''