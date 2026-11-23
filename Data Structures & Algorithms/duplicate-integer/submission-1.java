class Solution {
    public boolean hasDuplicate(int[] nums) {
    boolean output = false;
    int first = nums[0];
    for (int i = 0; i < nums.length; i++ ) {
        if (first == nums[i]){
            output = true;
        }
    }
        
    System.out.println("Output: " + output);
    return output;
    }
}