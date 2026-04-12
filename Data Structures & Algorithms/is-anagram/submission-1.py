class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        for i in s:
            s_map[i] = s_map.get(i, 0) + 1

        for i in t:
            if i not in s_map or s_map[i] == 0:
                return False
            else:
                s_map[i] -= 1

        return True
            
