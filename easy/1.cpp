// Given an array of integers nums and an integer target, return indices of the 
// two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may 
// not use the same element twice.

// You can return the answer in any order.

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // Brute force method
        //   - compute every possible sum and return index of elements 
        //     that sum up to the target value
        
        // for(int i=0; i < nums.size(); i++) {
        //     for(int j=i+1; j < nums.size(); j++) {
        //         if(nums[i] + nums[j] == target) {
        //             return {i, j};
        //         }
        //     }
        // }
        // return {};
        
        //      Optimization
        // store each value -> index pair into hashmap
        // search for an existing complement to 'target - value' for solution
        
        unordered_map<int, int> hm;
        
        for(int i=0; i < nums.size(); i++) {
            if(hm.find(target-nums[i]) != hm.end()) {
                return {i, hm[target-nums[i]]};
            }
            hm[nums[i]] = i;
        }
        return {};
    }
};