class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        
        for i in range(len(s)//2):
            first_char_place = i
            last_char_place = len(s) - 2 - i

            if s[first_char_place] != s[last_char_place]:
                return False
        return True