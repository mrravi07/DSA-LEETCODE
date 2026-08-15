class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = len(nums)
        k = 2

        for i in range(2,end):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1

        return k