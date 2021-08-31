class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        if n==0:
            return 0
        if n==1:
            return 1

        dp = [None]*(n+1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        counter = 2

        for i in range(3, n+1):
            if i%2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[counter]+dp[counter-1]
                counter = counter+1
        print(dp)
        return max(dp)
