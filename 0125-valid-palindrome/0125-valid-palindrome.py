class Solution:
    def alphaNum(self, char):
        return (("a" <= char.lower() <= "z") or ("0" <= char <= "9"))
    def isPalindrome(self, s: str) -> bool:
        
        left_pointer = 0
        right_pointer = len(s)-1
        
        while left_pointer < right_pointer:
            
            while left_pointer < right_pointer and not self.alphaNum(s[left_pointer]):
                left_pointer += 1
                
            while right_pointer > left_pointer and not self.alphaNum(s[right_pointer]):
                right_pointer -= 1
                
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            left_pointer += 1
            right_pointer -= 1
        return True
        
 