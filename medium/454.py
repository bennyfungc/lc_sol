# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples 
# (i, j, k, l) such that:

#     0 <= i, j, k, l < n
#     nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # split summing into nums1 + nums2 and num3 + nums4
        # store results in hashmap with sum value as key -> frequency as value
        
        # Since we are interested in nums1 + nums2 + num3 + nums4 = 0
        #   --> nums1 + nums2 = -(num3 + nums4)
        
        n = len(nums1)
        sum_freq = defaultdict(int)
        result = 0
        
        for i in range(n):
            for j in range(n):
                key1 = nums1[i] + nums2[j]
                sum_freq[key1] += 1
        
        for k in range(n):
            for l in range(n):
                key2 = -(nums3[k] + nums4[l])
                
                # if we find a key2 with the same value as a previous sum of key1, sum up its frequncy
                if key2 in sum_freq:
                    result += sum_freq[key2] 
       
        return result