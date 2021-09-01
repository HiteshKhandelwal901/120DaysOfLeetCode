class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        start_index = 1
        final_list = [[1],[1,1]]
        dp = [1,1]
        size = len(dp)

        if numRows == 1:
            return [[1]]



        for i in range(2, numRows):
            for j in range(i-1, 0, -1):
                dp[j] = dp[j] + dp[j-1]


            dp.append(1)



            final_list.append(dp.copy())
                
        return final_list
