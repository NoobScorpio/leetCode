# WILL MAKE IT BETTER
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ""
        i = (len(a) if len(a) > len(b) else len(b) ) -1
        if len(a)>len(b):
            x = len(a) - len(b) 
            b = "".join(["0" for _ in range(x)]) + b
        elif len(b)>len(a):
            x = len(b) - len(a) 
            a = "".join(["0" for _ in range(x)]) + a
        carry = False
        while i>-1:
            if a[i] == "0" and b[i] == "0":
                if carry:
                    sum += "1"
                    carry = False
                else:
                    sum += "0"
            elif a[i] == "1" and b[i] == "0":
                if carry:
                    sum += "0" 
                else:
                    sum += "1"
            elif a[i] == "0" and b[i] == "1":
                if carry:
                    sum += "0"
                else:
                    sum += "1"
            elif a[i] == "1" and b[i] == "1":
                if carry:
                    sum += "1"
                else:
                    sum += "0"
                    carry = True
            i = i-1
        if carry:
            sum = "1" + sum[::-1]
        else:
            sum = sum[::-1]
        return sum