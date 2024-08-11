def isValid(s):
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
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