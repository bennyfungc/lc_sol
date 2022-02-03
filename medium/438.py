# Given two strings s and p, return an array of all the start indices of p's 
# anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different
# word or phrase, typically using all the original letters exactly once.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        alphabet = defaultdict(int)
        result = []
        len_s = len(s)
        len_p = len(p)
        
        # build hashmap of character frequencies
        for char in p:
            alphabet[char] += 1
        
        # return if target string p is longer than s
        if len_p > len_s:
            return result
        
        # initial pass
        for i in range(len_p):
            if s[i] in alphabet:
                alphabet[s[i]] -= 1
        
        for i in range(len_s - len_p + 1):
        
            # check if current window is an anagram (frequencies of all characters = 0)
            if all(alphabet[char_freq] == 0 for char_freq in alphabet):
                result.append(i)
            
            if s[i] in alphabet:
                alphabet[s[i]] += 1
            if i+len_p < len_s and s[i+len_p] in alphabet:
                alphabet[s[i+len_p]] -= 1
            
        
        return result