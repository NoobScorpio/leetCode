def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        toValidate = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for h in s:
            if h in toValidate:
                el = stack.pop() if stack else '#'
                if toValidate[h] != el:
                    return False
            else:
                stack.append(h)
        
        return not stack

# PARANTHESIS
strs = '([)]'
strs = '()[]{}'
strs = '[([])]'
print(f"answer:[{str(isValid(strs))}]")