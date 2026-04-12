class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "").replace("?", "").replace(",", "").replace("'", "").replace(".", "")
        s_new = ""
        for char in s:
            if char.isalnum():
                s_new += char
        for i in range(len(s_new)//2):
            first_char_place = i
            last_char_place = len(s_new) - 1 - i

            if s_new[first_char_place] != s[last_char_place]:
                return False
        return True