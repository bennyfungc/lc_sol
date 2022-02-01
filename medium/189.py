# Given an array, rotate the array to the right by k steps, where k is 
# non-negative.

# Do it in-place with O(1) extra space

class Solution:
    
    # Helper function for reversing an array in place from a set beginning to end
    def reverse(self, arr, begin, end):
        while(begin < end):
            temp = arr[begin]
            arr[begin] = arr[end]
            arr[end] = temp
            
            begin += 1
            end -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr_len = len(nums)
        k = k % arr_len
        
        # if rotate amount is 0, then we are done
        if k == 0:
            return
               
        self.reverse(nums, 0, arr_len-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, arr_len-1)
        