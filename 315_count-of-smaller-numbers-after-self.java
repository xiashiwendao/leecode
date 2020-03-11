
class SegmentTree {
    public List<int> list;
    private int nMaxRange;
    public SegmentTree (List<int> arr) {
        //n个不同数字构造树
        var n = arr.Count;
        nMaxRange = n;
        var x = (int) Math.Ceiling (Math.Log (n) / Math.Log (2));
        var maxSize = 2 * (int) (Math.Pow (2, x)) - 1;
        if (n == 0) {
            list = new List<int> ();
            return;
        }
        list = new List<int> (maxSize);
        for (var i = 0; i < maxSize; i++) {
            list.Add (0);
        }
        ConstructTree (arr, 0, n - 1, 0);
    }
    //开始 结束 Node编号
    private void ConstructTree (List<int> arr, int ss, int se, int si) {
        if (ss == se) { //叶子节点
            list[si] = 0;
            return;
        }
        var mid = (ss + se) / 2;
        list[si] = 0;
        ConstructTree (arr, ss, mid, si * 2 + 1);
        ConstructTree (arr, mid + 1, se, si * 2 + 2);
    }

    private void UpdateValue (int ss, int se, int i, int diff, int si) {
        if (i < ss || i > se) return;
        list[si] += diff;
        if (se != ss) {
            var mid = (ss + se) / 2;
            UpdateValue (ss, mid, i, diff, 2 * si + 1);
            UpdateValue (mid + 1, se, i, diff, 2 * si + 2);
        }
    }
    public void UpdateV (int ind, int c) {
        UpdateValue (0, nMaxRange - 1, ind, c, 0);
    }
    //5 2 6 1
    //1 2 5 6
    //0 1 2 3
    //[0~3]
    //[0,1] [2, 3]
    //[0], [1], [2], [3]
    //[3] + 1
    //[2] + 1
    //[1] + 1
    private int GetCounUtil (int ss, int se, int upBound, int si) {
        if (se < upBound) return list[si];
        if (ss >= upBound) return 0;
        var mid = (ss + se) / 2;
        return GetCounUtil (ss, mid, upBound, 2 * si + 1) + GetCounUtil (mid + 1, se, upBound, 2 * si + 2);
    }
    public int GetCount (int upBound) {
        return GetCounUtil (0, nMaxRange - 1, upBound, 0);
    }
}


class SmallRight {

    public IList<int> CountSmaller (int[] nums) {
        // System.Comparison<int> cmp = (a, b) => {
        //     return a - b;
        // };
        // LeftLeaningRedBlackTree<int, int> tree = new LeftLeaningRedBlackTree<int, int> (cmp);
        // var rest = new List<int> ();
        // for (var i = nums.Length - 1; i >= 0; i--) {
        //     var v = nums[i];
        //     //<= v-1  < v
        //     var lowBound = tree.GetLowerNode (v-1);
        // }
        var dictNums = new HashSet<int> ();
        foreach (var n in nums) dictNums.Add (n);
        var lst = dictNums.ToList ();
        lst.Sort ();
        var dictIndex = new Dictionary<int, int> ();
        for (var i = 0; i < lst.Count; i++) {
            dictIndex.Add (lst[i], i);
        }

        var ret = new List<int> ();
        // Console.WriteLine (JsonSerializer.Serialize (lst));
        var segTree = new SegmentTree (lst);
        //[0, 3]
        //[0,1],[2,3]
        //0 1   2  3
        for (var i = nums.Length - 1; i >= 0; i--) {
            var v = nums[i];
            var ind = dictIndex[v];
            // Console.WriteLine (ind + ":" + JsonSerializer.Serialize (segTree.list));
            var c = segTree.GetCount (ind);
            ret.Add (c);
            //增加一个 到SegmentTree中
            segTree.UpdateV (ind, 1);
        }
        ret.Reverse ();
        return ret;
    }
}


public class Solution {
    public IList<int> CountSmaller(int[] nums) {
        var sr = new SmallRight ();
        return sr.CountSmaller(nums);
    }
}