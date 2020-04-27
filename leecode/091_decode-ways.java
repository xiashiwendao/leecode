class Decode_ways {
    public int numDecodings(String s) {
        if (s.charAt(0) == '0')
            return 0;
        char[] chars = s.toCharArray();
        return decode(chars, chars.length - 1);
    }

    public int decode(char[] chars, int index) {
        if (index <= 0)
            return 1;
        int count = 0;
        char curr = chars[index];
        char prev = chars[index - 1];
        if (curr > '0') {
            count = decode(chars, index - 1);
        }
        if (prev == '1' || (prev == '2' && curr <= '6')) {
            count += decode(chars, index - 2);
        }

        return count;
    }

    public static void main(String[] args) {
        test t = new test();
        int count = t.numDecodings("2216");
        System.out.println("count is: "+count);
    }
}