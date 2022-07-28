# Only for practice

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(0,len(nums)):
            for b in range(0,len(nums)):
                if a==b:
                    continue
                if nums[a]+nums[b]==target:
                    return [a,b]
