#Link -> https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _map = {}
        for i in s:
            _map[i] = _map.get(i,0)+1
        
        for i in t:
            if _map.get(i):
                _map[i] -= 1
            else:
                return False
        
        return all([c == 0 for c in _map.values()])
        