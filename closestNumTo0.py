class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest): 
                closest = i

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
    #time O(n) space: O(1) (not using any storage)
  #learned using abs(), abs() absolutely clutched here
