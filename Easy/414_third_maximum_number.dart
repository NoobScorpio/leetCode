class Solution {
  int thirdMax(List<int> nums) {
  for (int i = 0; i < nums.length; i++) {
    for (int j = i; j < nums.length; j++) {
      if (nums[i] > nums[j]) {
        int temp = nums[j];
        nums[j] = nums[i];
        nums[i] = temp;
      }
    }
  }
  for (int index = 0; index < nums.length / 2; ++index) {
    int temp = nums[index];
    nums[index] = nums[nums.length - 1 - index];
    nums[nums.length - 1 - index] = temp;
  }
  int elemCounted = 1;
  int prevElem = nums[0];
  for (int index = 1; index < nums.length; ++index) {
    if (nums[index] != prevElem) {
      elemCounted += 1;
      prevElem = nums[index];
    }
    if (elemCounted == 3) {
      return nums[index];
    }
  }

  return nums[0];
      
  }
}