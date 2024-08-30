class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False


        dict1, dict2 = Counter(s), Counter(t)

        for char in dict1:
            if char not in dict2:
                return False
            if dict2[char] != dict1[char]:
                return False
        
        return True

Method 2:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        return s == t
