class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        end = len(nums)
        k = 1

        for i in range(1,end):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
           


        return k
