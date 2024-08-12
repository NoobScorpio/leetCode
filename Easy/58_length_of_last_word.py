class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sp = " ".join(s.split())
        sp = sp.split(" ")
        print(sp)
        return len(sp[-1])