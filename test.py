def max_substring(strs):
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
            for tmp_pos in range(i, j+1):
                tmp_char = strs[tmp_pos]
                hash_pos.pop(tmp_char)

            i = char_pos+1
        # 当前字符不存在
        else:
            pass
        j+=1

    max_len = max(max_len, j - i)
    return max_len

if __name__ == "__main__":
    max_len = max_substring('defgafea')
    print(max_len)
    # d = dict()
    # d['a']='A'
    # d['b']='B'
    # d['c']='C'

    # print('a' in d)
