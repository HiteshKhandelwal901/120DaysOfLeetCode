class Solution:
    def romanToInt(self, s: str) -> int:

        chardict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        size = len(s)
        total = 0
        i=0

        while(i<size-1):
            if(s[i] == 'I' and s[i+1] == 'V'):
                    total -= 1
            elif(s[i] == 'I' and s[i+1] == 'X'):
                total -= 1
            elif(s[i] == 'X' and s[i+1] == 'L'):
                total -= 10
            elif(s[i] == 'X' and s[i+1] == 'C'):
                total -= 10
            elif(s[i] == 'C' and s[i+1] == 'D'):
                total -= 100
            elif(s[i] == 'C' and s[i+1] == 'M'):
                total -= 100
            else:
                total += chardict.get(s[i])
            i=i+1

        total = total + chardict.get(s[size-1])

        return total


            
