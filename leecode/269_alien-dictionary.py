def alien_dic(words):
    order_list=[]
    order_sub_list=[]
    max_len = 0
    for word in words:
        index = 0
        for ch in word:
            # 每个字母位置都设置一下appendlist，如果没有则创建，如果有可以直接取用
            if len(order_sub_list) < index+1:
                order_sub_list.append([])
            tmp_lst = order_sub_list[index]
            # 这一步可以优化，不需要每次都遍历一遍  
            if ch not in tmp_lst:
                tmp_lst.append(ch)
            
            index+=1
    
    return order_sub_list

def aline_dic_graph(words):
    adjList = {}
    visited = []
    loop = []
    stack = []
    # 构建邻接列表
    for index in range(len(words)-1):
        word1 = words[index]
        word2 = words[index+1]
        len1 = len(word1)
        len2 = len(word2)
        max_len = max(len1, len2)
        found = False
        for i in range(max_len):
            c1 = word1[i] if i < len1 else None
            c2 = word2[i] if i < len2 else None
            if(c1 != None and c1 not in adjList.keys()):
                adjList[c1] = []
            if(c2 != None and c2 not in adjList.keys()):
                adjList[c2] = []
            if(c1 != None and c2 != None and c1 != c2 and not found):
                adjList[c1].append(c2)
                # 只要两个words中有一个字母是不相同，之后的字母间后面就无法判断前后关系；
                # 但是这里不能够break，因为后面可能还有未出现的字母，需要放置到adjList里面
                found = True 
    for key in adjList.keys():
        if key not in visited:
            if (not topoSort(adjList, key, visited, loop, stack)):
                return ""

    return stack[::-1]

def topoSort(adjList, u, visited, loop, stack):
    visited.append(u)
    loop.append(u)
    for v in adjList[u]:
        if v in loop:
            return False
        if v not in visited:
            if(not topoSort(adjList, v, visited, loop, stack)):
                return False

    loop.remove(u)
    stack.append(u)

    return True



if __name__ == "__main__":
    # words = ["wrt", "wrf","er","ett", "rftt"]
    words = ["z", "x", "z"]
    # ret = alien_dic(words)
    # print(ret)
    ret = aline_dic_graph(words)
    print(ret)

'''
现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。
假设，您并不知道其中字母之间的先后顺序。但是，会收到词典中获得一个 不为空的 单词列表。因为是从词典中获得的，所以该单词列表内的单词已经 按这门新语言的字母顺序进行了排序。
您需要根据这个输入的列表，还原出此语言中已知的字母顺序。

示例 1：

输入:
["wrt","wrf","er","ett","rftt"]
输出: "wertf"

示例 2：
输入:
["z","x"]
输出: "zx"

示例 3：
输入:
["z","x","z"] 
输出: "" 
解释: 此顺序是非法的，因此返回 ""。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/alien-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''