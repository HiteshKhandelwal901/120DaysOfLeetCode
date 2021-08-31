class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)-1
        for i in range(size-2,-1,-1):
            cost[i] = cost[i] + min(cost[i+1],cost[i+2])
        return min(cost[0], cost[1])
