class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        k = n -1
        left , right = 0, n-1
        result = [0] * n

        while left<= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                result[k] = left_sq
                left += 1
            else:
                result[k] = right_sq
                right -= 1

            k -=1
        return result
            

        