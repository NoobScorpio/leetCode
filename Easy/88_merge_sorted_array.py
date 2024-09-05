# NEED TO CONVERT TO PYTHON
class Solution {
  void merge(List<int> nums1, int m, List<int> nums2, int n) {
   if(m>0){
       for(int i=0;i<nums1.length;i++){
        if(nums1[i]==0){
            for(int j=0;j<nums2.length;j++){
                if(nums1[j]!=0){
                    nums1[i]=nums2[j];
                    nums2.remove(nums2[j]);
                    break;
                }
            }
        }
    }
   }else{
      for(int i=0;i<nums2.length;i++){
        if(nums2[i]!=0){
            for(int j=0;j<nums1.length;j++){
                if(nums1[j]==0){
                    nums1[j]=nums2[i];
                    nums2[i]=0;
                    break;
                }
            }
        }
    }
   }
  for(int i=0;i<nums1.length;i++){
     
      for(int j=0;j<nums1.length-1;j++){
        if(nums1[j]>nums1[j+1]){
          int temp=nums1[j];
          nums1[j]=nums1[j+1];
          nums1[j+1]=temp;
        }
    }
    }
  print(nums1);
}
}