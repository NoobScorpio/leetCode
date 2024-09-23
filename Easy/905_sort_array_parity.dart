class Solution {
  List<int> sortArrayByParity(List<int> nums) {
    List<int> ans=[];
      for(int i=0;i<nums.length;i++){
          if(nums[i]%2==0){
              ans.add(nums[i]);
          }
      }
      for(int i=0;i<nums.length;i++){
          if(nums[i]%2!=0){
              ans.add(nums[i]);
          }
      }
      return ans;
  }
}