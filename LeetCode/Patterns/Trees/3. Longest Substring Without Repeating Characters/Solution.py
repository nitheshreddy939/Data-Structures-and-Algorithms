class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        maximum = float('-inf')

        count = 0

        j=0

        for i in range(len(s)):

            while s[i] in seen:
                seen.remove(s[j])
                j+=1
                count-=1

            seen.add(s[i])

            count+=1

            maximum = max(maximum,count)

        return maximum


            
        