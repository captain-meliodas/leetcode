#Link -> https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        count = {}
        for i in magazine:
            count[i] = count.get(i,0)+1
        for i in ransomNote:
            if count.get(i):
                count[i] = count[i] - 1
                if count[i] < 0:
                    return False    
            else:
                return False
        
        return True