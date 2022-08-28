class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=0
        for i in range(0,len(nums)):
            if nums[n] == val:
                nums.pop(n)
            else:
                n+=1
        return len(nums)
