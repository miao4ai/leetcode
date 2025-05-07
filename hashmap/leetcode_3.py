class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        hashmap = {}
        longest = 0
        start = previous = 0

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]]=i
            else:
                previous = hashmap[s[i]]
                
                start =max(previous+1,start)
                hashmap[s[i]]=i
            
            longest= max(longest,i-start+1)
        
        return longest
