class Solution(object):
    def isBipartite(self, graph):
        # 节点着色记录
        color = {}
        # 遍历图节点，注意图在这里是通过二维数组形式进行存储
        # 数组的索引代表了节点索引，数组索引所对应元素（N个数）
        # 代表了和这个节点有连线关系的节点（索引）
        for node in range(len(graph)):
            print(node)
            # 如果当前节点并没有着过色，设置初始化颜色（0），放入堆栈中，这里有一个堆栈对象
            # 用于存放已经着色的节点
            if node not in color:
                stack = [node]
                color[node] = 0
                # 遍历堆栈
                while stack:
                    node = stack.pop()
                    # 遍历一下graph里面的节点，用于和堆栈中元素进行比较，如果相等
                    # 说明了这个图不是二部图，因为不满足节点首尾可以划分为两个集合
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True

if __name__ == "__main__":
    s = Solution()
    graph = [[1,3], [0,2], [1,3], [0,2]]
    rev = s.isBipartite(graph)

    print(rev)
    # s = Solution()
    # print(dir(s))