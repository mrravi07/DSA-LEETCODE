class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9 + 7
        
        left, right = 0, len(nums) - 1
        ans = 0
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                
                ans = (ans + pow(2, right - left, MOD)) % MOD
                left += 1
            else:
                right -= 1
                
        return ans
        