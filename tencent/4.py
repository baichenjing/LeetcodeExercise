import sys


class Solution:
    def myAtoi(self, str):
        if str == ' ' or str == "":
            return 0

        sign = 1

        base = 0

        i = 0
        while i < len(str) and str[i] == ' ':
            i = i + 1
            if i >= len(str):
                return 0
        if str[i]=='-' or str[i]=='+':
            sign=str[i]=='-' and -1 or 1
            i=i+1
        while i<len(str) and str[i] >='0' and str[i] <='9':
            if base>214748364 or (base==214748364 and ord(str[i])-ord('0')>6):
                return sign==1 and 2147483647 or -2147483648

            base=10*base+(ord(str[i])-ord('0'))
            i=i+1

        return base*sign



if __name__ == '__main__':
    print(ord('8')-ord('0')>6)
    print(Solution().myAtoi("2147483648"))