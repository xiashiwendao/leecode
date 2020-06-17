package leecode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

public class Alien_words {
    public static void main(final String[] args) {
        final Alien_words aw = new Alien_words();
        final String[] words = { "wrt", "wrf", "er", "ett", "rftt" };
        final String ret = aw.alienOrder(words);

        System.out.println(ret);
    }

    // 基本情况处理，比如输入为空，或者输入的字符串只有一个
    String alienOrder(final String[] words) {
        if (words == null || words.length == 0)
            return null;
        if (words.length == 1) {
            return words[0];
        }

        // 构建有向图：定义一个邻接链表 adjList，也可以用邻接矩阵
        final Map<Character, List<Character>> adjList = new HashMap<>();
        // 遍历单词组中每个单词
        for (int i = 0; i < words.length - 1; i++) {
            final String w1 = words[i], w2 = words[i + 1];
            final int n1 = w1.length(), n2 = w2.length();

            boolean found = false;
            // 遍历相邻两个单词的中字母
            for (int j = 0; j < Math.max(w1.length(), w2.length()); j++) {
                final Character c1 = j < n1 ? w1.charAt(j) : null;
                final Character c2 = j < n2 ? w2.charAt(j) : null;
                // 第一个单词的当前字母不为空，并且邻接列表中没有此字母，则添加
                if (c1 != null && !adjList.containsKey(c1)) {
                    adjList.put(c1, new ArrayList<Character>());
                }
                // 第二个单词的当前字母不为空，并且邻接列表中没有此字母，则添加
                if (c2 != null && !adjList.containsKey(c2)) {
                    adjList.put(c2, new ArrayList<Character>());
                }
                // 两个单词的当前字母都不为null且不相等，并且，上一轮相邻两个单词的字母没有建立关联（c0和c1没有建立关联），
                // 则将c1和c2建立关联,那么当前位置已经没有关联关系，因为前一位已经不同；只有当前面几位都是一致的时候（found=false），
                // 当前位才有比较的价值
                if (c1 != null && c2 != null && c1 != c2 && !found) {
                    adjList.get(c1).add(c2);
                    found = true;
                }
            }
        }

        final Set<Character> visited = new HashSet<>(); // 访问过的字母容器
        final Set<Character> loop = new HashSet<>();
        final Stack<Character> stack = new Stack<Character>();
        // 邻接链表构建完成后，进行遍历邻接列表
        for (final Character key : adjList.keySet()) {
            // 如果visited容器中没有包含key
            if (!visited.contains(key)) {
                // 将当前节点 u 加入到 visited 集合以及 loop 集合中。
                if (!topologicalSort(adjList, key, visited, loop, stack)) {
                    return "";
                }
            }
        }

        final StringBuilder sb = new StringBuilder();

        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }

        return sb.toString();

    }

    // 将当前节点 u 加入到 visited 集合以及 loop 集合中。
    // 这个函数主要是判断图从一个节点出发是否有闭环，有闭环则此次构建图失败
    // 这里的stack很重要，数据顺序和visited正好相反，visited是Hashset，数据顺序无法维持，
    // 所以采用stack来记录数据以及数据的顺序，不过visited,利用Hash特性来判断存在性是有优势的
    boolean topologicalSort(final Map<Character, List<Character>> adjList, final char u, final Set<Character> visited,
            final Set<Character> loop, final Stack<Character> stack) {
        visited.add(u);
        loop.add(u);
        // 判断当前u节点的邻接节点是否放入到loop，如果有这说明存在闭环，非线性
        if (adjList.containsKey(u)) {
            for (int i = 0; i < adjList.get(u).size(); i++) {
                final char v = adjList.get(u).get(i);
                // 这里采用loop来判断而不是visited是因为loop中只是存储当前节点的路径
                // 后面可以看到loop最后是会remove掉这个u的；所以loop只是单个节点出发的路径节点信息
                if (loop.contains(v))
                    return false;

                if (!visited.contains(v)) {
                    if (!topologicalSort(adjList, v, visited, loop, stack)) {
                        return false;
                    }
                }
            }
        }

        loop.remove(u);
        stack.push(u);

        return true;
    }
}
