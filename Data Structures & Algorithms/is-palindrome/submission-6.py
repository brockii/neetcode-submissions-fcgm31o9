class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_new = ""
        for char in s:
            if char.isalnum():
                s_new += char
        s_new = s_new.lower()

        for i in range(len(s_new)//2):
            first_char_place = i
            last_char_place = len(s_new) - 1 - i

            if s_new[first_char_place] != s_new[last_char_place]:
                return False
        return True