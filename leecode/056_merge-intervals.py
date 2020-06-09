def merge(lst_segment):
    lst = lst_segment.copy()

    # 排序
    lst = sorted(lst, key=lambda segment: segment[0])
    pre_seg = lst[0]
    lst.remove(pre_seg)
    ret = []
    ret.append(pre_seg)
    # ret.append(pre_seg)
    for segment in lst:
        next_seg = segment
        # 临近两个区间有交集
        if pre_seg[1] >= next_seg[0]:
            # 并且pre_seg和next_seg之间区间非包含关系（pre_seg > next_seg）
            if(pre_seg[1] < next_seg[1]):
                next_seg = [pre_seg[0], next_seg[1]]
                ret.remove(pre_seg) # 删除原范围
                ret.append(next_seg)
            # pre_seg包含了next_seg，即next_seg无效，则next_seg继续沿用pre_seg
            else:
                next_seg = pre_seg
        # 临近两个区间没有交集
        else:
            if len(ret) == 0:
                ret.append(pre_seg)
            else:
                ret.append(next_seg)

        pre_seg = next_seg

    return ret

def merge_2(lst_segment):
    lst = lst_segment.copy()

    # 排序
    lst = sorted(lst, key=lambda segment: segment[0])
    pre_seg = lst[0]
    lst.remove(pre_seg)
    ret = []
    ret.append(pre_seg)
    # ret.append(pre_seg)
    for segment in lst:
        next_seg = segment
        # 临近两个区间有交集
        if pre_seg[1] >= next_seg[0]:
            # 并且pre_seg和next_seg之间区间非包含关系（pre_seg > next_seg）
            if(pre_seg[1] < next_seg[1]):
                next_seg = [pre_seg[0], next_seg[1]]
                ret.remove(pre_seg) # 删除原范围
                ret.append(next_seg)
            # pre_seg包含了next_seg，即next_seg无效，则next_seg继续沿用pre_seg
            else:
                next_seg = pre_seg
        # 临近两个区间没有交集
        else:
            if len(ret) == 0:
                ret.append(pre_seg)
            else:
                ret.append(next_seg)

        pre_seg = next_seg

    return ret

if __name__ == "__main__":
    lst_segment = [[1, 3], [2, 6],[2,3],[5,7], [15, 18], [8, 10]]
    ret = merge(lst_segment)
    for seg in ret:
        print(seg)

'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
