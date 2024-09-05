class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ""
        for d in digits:
            num+=str(d)
        
        num = str(int(num)+1)

        ans =[]
        for n in num:
            ans.append(int(n))
        
        return ans