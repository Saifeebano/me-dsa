class Solution {
    public void moveZeroes(int[] nums) {
        int insertPos = 0;

        // Step 1: Saare non-zero elements ko aage shift karo
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[insertPos] = nums[i];
                insertPos++;
            }
        }

        // Step 2: Baki bache hue positions par 0 fill karo
        while (insertPos < nums.length) {
            nums[insertPos] = 0;
            insertPos++;
        }
    }
}