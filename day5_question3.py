class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        window_position = 0
        maxlength = 0
        currlength = 0
        i = 0

        while(i<len(s)):
            print("i = ", i)
            if s[i] in visited.keys() and window_position <=visited[s[i]]:
                print("true")
                maxlength = max(maxlength, currlength)
                print("maxlen = ", maxlength)
                window_position = visited[s[i]]+1
                print("window_position = ", window_position)
                currlength = i-window_position +1
                print("currlen = ", currlength)
                visited[s[i]]=i


            else:
                print("false")
                currlength = currlength+1
                print("currlen = ", currlength)

            visited[s[i]] = i
            i = i+1
            print("visited at end of loop = ", visited)

        return max(maxlength, currlength)

    """
output

i =  0
false
currlen =  1
visited at end of loop =  {'p': 0}

i =  1
false
currlen =  2
visited at end of loop =  {'p': 0, 'w': 1}

i =  2
true
maxlen =  2
window_position =  2
currlen =  1
visited at end of loop =  {'p': 0, 'w': 2}

i =  3
false
currlen =  2
visited at end of loop =  {'p': 0, 'w': 2, 'k': 3}

i =  4
false
currlen =  3
visited at end of loop =  {'p': 0, 'w': 2, 'k': 3, 'e': 4}

i =  5
true
maxlen =  3
window_position =  3
currlen =  3
visited at end of loop =  {'p': 0, 'w': 5, 'k': 3, 'e': 4}

    """
