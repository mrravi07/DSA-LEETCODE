class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k =0

        for num in nums:
            nums[k] = num*num
            k += 1

        nums.sort()

        return nums