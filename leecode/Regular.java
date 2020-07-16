package suanfa;

public class Regular {
	public static void main(String[] args) {
		Regular r = new Regular();
//	    String s = "misssissippi";
//	    String p = "mis*is*ip*.";
//		String s = "aaaaa";
//	    String p = "a*";
	    String s = "aab";
	    String p = "c*a*b";
		
		boolean result = r.isMatch_5(s, p);
		
		System.out.println(result);
		
	}
	
	boolean isMatch(String s, String p) {
	    if (s == null || p == null) {
	        return false;
	    }
	    
	    return isMatch(s, 0, p, 0);
	}
	
	boolean isMatch(String s, int i, String p, int j) {
	    int m = s.length();
	    int n = p.length();
	  
	    // 看看pattern和字符串是否都扫描完毕
	    if (j == n) {
	        return i == m;
	    }
	  
	    // next char is not '*': 必须满足当前字符并递归到下一层
	    // 前面有了j == n，这里可以放心大胆的访问j+1
	    if (j == n - 1 || p.charAt(j + 1) != '*') {
	        return (i < m) && 
	        	(p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)) && 
	            isMatch(s, i + 1, p, j + 1);
	    }
	  
	    // next char is '*', 如果有连续的s[i]出现并且都等于p[j]，一直尝试下去
	    if (j < n - 1 && p.charAt(j + 1) == '*') {
	    	// 注意，j是不变的，i每次加1；
	    	// 在*的情况下，j+1取值就是j，一直拿p[j]和s[i++]来进行比较
	        while ((i < m) && (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j))) {
	            if (isMatch(s, i, p, j + 2)) {
	                return true;
	            }
	            i++;
	        }
	    }
	  
	    // 接着继续下去
	    return isMatch(s, i, p, j + 2);
	}
	
	boolean isMatch_2(String s, String p) {
	    if (s == null || p == null) return false;

	    return isMatch_2(s, s.length(), p, p.length());
	}
	
	boolean isMatch_2(String s, int i, String p, int j) {
	    if (j == 0) return i == 0; 
	    if (i == 0) {
	    	// 这里为什么是j > 1呢？貌似用于s的子字符串来匹配a*的场景，所以一定要j>1;
	    	// 这种实现方式i和j代表的长度（从前分析i和j代表的是下标索引
	        return j > 1 && p.charAt(j - 1) == '*' && isMatch(s, i, p, j - 2);
	    }
	  
	    if (p.charAt(j - 1) != '*') {
	        return isMatch_2(s.charAt(i - 1), p.charAt(j - 1)) && 
	        		isMatch_2(s, i - 1, p, j - 1);
	    }
	  
	    return  isMatch_2(s, i, p, j - 2) || isMatch_2(s, i - 1, p, j) &&
	            isMatch_2(s.charAt(i - 1), p.charAt(j - 2));
	}

	boolean isMatch_2(char a, char b) {
	    return a == b || b == '.';
	}
	
	// 分别用 m 和 n 表示 s 字符串和 p 字符串的长度
	boolean isMatch_3(String s, String p) {
	    int m = s.length(), n = p.length();

	    // 定义一个二维布尔矩阵 dp
	    boolean[][] dp = new boolean[m + 1][n + 1];

	    // 当两个字符串的长度都为 0，也就是空字符串的时候，它们互相匹配
	    dp[0][0] = true;
	  
	    for (int j = 1; j <= n; j++) {
	        dp[0][j] = j > 1 && p.charAt(j - 1) == '*' && dp[0][j - 2];
	    }

	    for (int i = 1; i <= m; i++) {
	        for (int j = 1; j <= n; j++) {
	            // p 的当前字符不是 '*'，判断当前的两个字符是否相等，如果相等，就看 dp[i-1][j-1] 的值，因为它保存了前一个匹配的结果
	            if (p.charAt(j - 1) != '*') {
	                dp[i][j] = dp[i - 1][j - 1] && 
	                   isMatch_3(s.charAt(i - 1), p.charAt(j - 1));
	            } else {
	                dp[i][j] = dp[i][j - 2] || dp[i - 1][j] && 
	                   isMatch_3(s.charAt(i - 1), p.charAt(j - 2));
	            }
	        }
	    }
	  
	    return dp[m][n];
	}

	boolean isMatch_3(char a, char b) {
	    return a == b || b == '.';
	 
	}
	
	// 分别用 m 和 n 表示 s 字符串和 p 字符串的长度
	boolean isMatch_5(String s, String p) {
	    int m = s.length(), n = p.length();

	    // 定义一个二维布尔矩阵 dp
	    boolean[][] dp = new boolean[m + 1][n + 1];

	    // 当两个字符串的长度都为 0，也就是空字符串的时候，它们互相匹配
	    dp[0][0] = true;
	    // 第一波计算，看看在第一行上面有哪些是匹配项（空字符串匹配）
	    for (int j = 1; j <= n; j++) {
	        dp[0][j] = j > 1 && p.charAt(j - 1) == '*' && dp[0][j - 2];
	    }
	    // 第二步计算，看看非空字符串的比较，这里就存在逐位匹配过程
	    for (int i = 1; i <= m; i++) {
	        for (int j = 1; j <= n; j++) {
	            // p 的当前字符不是 '*'，判断当前的两个字符是否相等，如果相等，就看 dp[i-1][j-1] 的值，
	        	// 因为它保存了前一个匹配的结果
	        	// 这里补充一下，长度为j的字符，对应索引是j-1，所以j长度字符索引是j-1
	            if (p.charAt(j - 1) != '*') {
	            	// 第[i][j]位置对应的是s[i-1]和p[j-1]之间的匹配关系；这个是因为
	            	// [0][0]代表的是空字符串匹配，[m+1][n+1]才是m和n的匹配关系
	            	// 但是dp是索引代表的字符串的长度，所以这里都是i，j但是里面比较的结果其实是j-1，i-1的
	            	// 如果不是*，那么首先要保证前一个是匹配的，然后当前字符和模式的当前字符是匹配的
	                dp[i][j] = dp[i - 1][j - 1] && 
	                   isMatch_5(s.charAt(i - 1), p.charAt(j - 1));
	            } else {
	            	// 如果当前字符和*前面的字符匹配，那么就是匹配，因为*代表重复匹配；
	            	// 或者当前字符的前一个字符*匹配，并且，当前字符和前一个字符匹配，那么也是匹配，即字符重复嘛
	                dp[i][j] = dp[i][j - 2] || dp[i - 1][j] && 
	                   isMatch_5(s.charAt(i - 1), p.charAt(j - 2));
	            }
	            // 我在想isMatch_5中发现不匹配，是不是可以直接跳出循环呢？只要有一个不匹配就可以玩完了吧？
	        }
	    }
	  
	    return dp[m][n];
	}

	boolean isMatch_5(char a, char b) {
	    return a == b || b == '.';
	 
	}
}
