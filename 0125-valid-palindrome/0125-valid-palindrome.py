class Solution:
    # def alphaNum(self, char):
    #     return (("a" <= char.lower() <= "z") or ("0" <= char <= "9"))
    def isPalindrome(self, s: str) -> bool:
    
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True
        
 