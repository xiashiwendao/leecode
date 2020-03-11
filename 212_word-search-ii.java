import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    
    class Node {
         Node[] next = new Node[26];
 
         /**
          * 只有一个单词的结尾才有值
          */
         String value;
         boolean leaf;
         public Node() {
         }
     }
 
     Node root = new Node();
     int l1, l2;
 
     public List<String> findWords(char[][] board, String[] words) {
         //构建前缀树
         // 遍历所有单词
         for (String word : words) {
             Node node = root; // 每个单词都是从根节点开始构建
             // 遍历单词字母，树结构中如果已经存在则直接跳过，不存在则创建子节点
             for (int i = 0; i < word.length(); i++) {
                 if (node.next[word.charAt(i) - 'a'] == null) {
                     node.next[word.charAt(i) - 'a'] = new Node();
                 }
                 // 指向node下一个节点
                 node = node.next[word.charAt(i) - 'a'];
             }
             node.value = word;
             node.leaf = true;
         }
 
         l1 = board.length;
         if (l1 == 0) {
             return new ArrayList<>();
         }
         l2 = board[0].length;
         if (l2 == 0) {
             return new ArrayList<>();
         }
         boolean[][] visited = new boolean[l1][l2];
         //        max = l1 > l2 ? l1 : l2;
         Set<String> results = new HashSet<>();
         for (int i = 0; i < l1; i++) {
             for (int j = 0; j < l2; j++) {
                 searchTrie(board, i, j, root, results, visited);
             }
         }
         return new ArrayList<>(results);
     }
 
     public void searchTrie(char[][] board, int i, int j, Node node, Set<String> result,
             boolean[][] visited) {
         if (i < 0 || j < 0 || i >= l1 || j >= l2) {
             return;
         }
         if (visited[i][j]) {
             return;
         }
         visited[i][j] = true;
         Node next = node.next[board[i][j] - 'a'];
         if (null == next) {
             visited[i][j] = false;
             return;
         }
         if (next.leaf) {
             result.add(next.value);
         }
         searchTrie(board, i - 1, j, next, result, visited);
         searchTrie(board, i + 1, j, next, result, visited);
         searchTrie(board, i, j - 1, next, result, visited);
         searchTrie(board, i, j + 1, next, result, visited);
         visited[i][j] = false;
 
     }
 }