def longestCommonPrefix(strs):
       """
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".
        Example 1:

        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        Example 2:

        Input: strs = ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
       
       :type strs: List[str]
       :rtype: str
       """
       comm = ""
       n = len(strs)
       i=0
       while i<n-1:
           curr = len(strs[i])
           next = len(strs[i+1])
           l = curr if curr<next else next
           if l ==0:
               return ""
           j=0
           curr = strs[i]
           next = strs[i+1]
           if curr == "" or next == "":
               return ""
           if curr[0] != next[0]:
               return ""
           if len(next)<len(comm):
               comm = comm[:len(next)]
           if comm != "":
               l = len(comm) if len(comm)<len(next) else len(next)
               print(f"COMM: LENGTH SELECTED: {l} , COMM: {len(comm)}({comm}), NEXT: {len(next)}")
               
               while j<l:
                    if comm[j] != next[j]:
                        if len(next) == 1:
                            comm = ""
                        elif len(next)<len(comm):
                            comm = comm[:len(next)]
                        else:
                            comm = comm[:-1]
                        j -=1 
                        l -= 1
                    else:
                        if len(next)<len(comm):
                            comm = ""
                    j+=1
                   
           else:
               print(f"LENGTH SELECTED: {l} , CURR: {len(curr)}({curr}), NEXT: {len(next)}")
               while j<l:
                   if j == 0:
                       if curr[j] != next[j]:
                           return ""
                   if curr[j] == next[j]:
                       comm += str(curr[j])
                   else:
                       break
                   j+=1
               
           print(f"i={i}: {comm}")
           i+=1        
       return comm