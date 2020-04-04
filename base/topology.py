# 获取入度信息
def getadj(topy):
    V=[]
    indegree={1:0}
    for v, endpoints in topy.items():
            V.append(v)
            for endpoint in endpoints:
                indegree.setdefault(endpoint,0)
                indegree[endpoint]+=1
    
    return V, indegree

def topo_sort(indegree, topo):
    q = []
    for v, count in indegree.items():
        if(count == 0):
            q.append(v)
    print('len(q)=',len(q))
    while len(q)!=0:
        v = q.pop(0)
        print('output element: ', v)
        for u in topo[v]:
            # print('find %s endpoint %s'%(v, u))
            indegree[u]-=1
            # print('reduce indegree to: ', indegree[u])
            if(indegree[u]==0):
                # print('add %s to queue'%u)
                q.append(u)

if __name__ == "__main__":
    # topo = [[1,[2,4]],[2,[4,3]],[3,[5]],[4, [3,5]],[5,[]]]
    # topo = [(1,[2,4]),(2,[4,3]),(3,[5]),(4, [3,5]),(5,[])]
    topo = {1:[2,4], 2:[4,3], 3:[5], 4:[3,5],5:[]}
    V, indegree = getadj(topo)
    print(indegree)
    topo_sort(indegree, topo)
    # g = Adj_graph(1,[2,4])


# '''邻接矩阵法完成图的表示'''

# #创建图，输入图的顶点个数、顶点、以及创建邻接表和存储顶点的数组
# class Graph(object):

#     def __init__(self):
#         self._count = int(input('输入图的顶点的个数:'))
#         self._adjlist = [[None for i in range(self._count)] for i in range(self._count)]
#         self._peak_list = []
#         for i in range(self._count):
#             self._peak = input('输入顶点:')
#             self._peak_list.append(self._peak)

#     #顶点之间的关系
#     def ad_relationship(self):
#         print('输入顶点之间的关系')
#         for i in range(self._count):
#             self._adjlist[i][i] = 0
#             for j in range(self._count):
#                 while self._adjlist[i][j] == None:
#                     msg = input('输入顶点%s--%s之间的关系(0表示无连通，1表示有连通)' % (self._peak_list[i],self._peak_list[j]))
#                     if msg == '0' or msg == '1':
#                         self._adjlist[i][j] = int(msg)
#                         self._adjlist[j][i] = self._adjlist[i][j]
#                     else:
#                         print('输入有误....')
#         #输出
#         for k in range(self._count):
#             print(self._adjlist[k])

# if __name__ == '__main__':
#     s = Graph()
#     s.ad_relationship()


