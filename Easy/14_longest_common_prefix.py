def longestCommonPrefix(strs):
       """
       :type strs: List[str]
       :rtype: str
       """
       if strs is []:
           return ""
       else:
            ans = ""
            sort = sorted(strs)
            first = sort[0]
            last = sort[-1]
            if first == "" or last == "":
                return ans
            for i in range(min(len(first),len(last))):
                if first[i]!=last[i]:
                    return ans
                ans += first[i]
            return ans