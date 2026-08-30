class Solution {
    public int myAtoi(String s) {
        if (s == null || s.length() == 0) return 0;
        
        int index = 0;
        int n = s.length();
        
        // 1. Ignore leading whitespace
        while (index < n && s.charAt(index) == ' ') {
            index++;
        }
        
        // Return early if string is only whitespace
        if (index == n) return 0;
        
        // 2. Determine sign
        int sign = 1;
        if (s.charAt(index) == '+' || s.charAt(index) == '-') {
            sign = (s.charAt(index) == '-') ? -1 : 1;
            index++;
        }
        
        // 3. Convert digits and check overflow
        long result = 0;
        while (index < n && Character.isDigit(s.charAt(index))) {
            int digit = s.charAt(index) - '0';
            result = result * 10 + digit;
            
            // 4. Handle 32-bit integer overflow/underflow rounding
            if (sign * result > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }
            if (sign * result < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
            
            index++;
        }
        
        return (int) (sign * result);
    }
}