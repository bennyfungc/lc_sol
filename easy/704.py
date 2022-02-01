# Given an array of integers nums which is sorted in ascending order, and an 
# integer target, write a function to search target in nums. If target exists, 
# then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    # Iterative binary search
    def search(self, nums: List[int], target: int) -> int:
        
        left_bound = 0
        right_bound = len(nums) - 1
        
        while left_bound < right_bound-1:
            idx = int ((right_bound + left_bound) / 2)
            
            if nums[idx] == target:
                return idx
            
            if nums[idx] > target:
                right_bound = idx
            elif nums[idx] < target:
                left_bound = idx
            
        if nums[left_bound] == target:
            return left_bound
        elif nums[right_bound] == target:
            return right_bound
        else:
            return -1
        
        