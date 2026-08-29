class Solution {
    public int singleNumber(int[] nums) {
        
        int ans = 0;
        for (int num : nums) {
            ans ^= num; // Duplicate elements 0 ho jayenge (a ^ a = 0)
        }
        return ans;
    }
}