class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        We will use local max and global max varibales
        intialize localmax to zero and golbalmax to large negitive so that if  onlynegitive inputs are there, the sum of negitve will be the maxsum,
        ex: [-1,-2,-3] sum = -6 < -10000 hence max = -6

        for each number
          Add the number to local max

          if localmax > globalmax
             globalmax = localmax, ex : [5,3] gm = 8. lm = 8  next [5,3,-1] lm = 7, gb = 8

          if localmax falls below zero[because anything added to this will be lesser than the sum of added elements, ex : -2 + 3 +5 +7 < 3+5+7
             update localmax = 0

        """

        localmax = 0
        globalmax = -10000

        for i in range(len(nums)):
            localmax = localmax + nums[i]

            if globalmax < localmax:
                globalmax = localmax

            if localmax < 0:
                localmax = 0

        return globalmax