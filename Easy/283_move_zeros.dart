
class Solution {
 
void moveZeroes(List<int> nums) {
    int unique=0,zeros=0;
    for(int i=0;i<nums.length;i++){
        if(nums[i]!=0){
            nums[unique]=nums[i];
            unique++;
        }else{
            zeros++;
        }
    }
    for(int i=nums.length-zeros;i<nums.length;i++){
        nums[i]=0;
    }
  }
}