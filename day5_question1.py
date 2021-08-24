class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            #print("i = ", i, " nums = ", nums[i])
            #if target > nums[i]:
            #print("sinsie greater than")
            diff = target - nums[i]
            #print("diff = ", diff)
            #else:
                #print("inside lesser than")
                #diff  = nums[i] - target
                #print("diff = ", diff)

            if nums[i] not in hashmap.keys():
                #print("diff not in dict")
                hashmap[diff] = i
                #print("hashmap = ", hashmap)

            else:
                #print("diff found in dict")
                #print("resutl = ", [i, hashmap[nums[i]]])
                return [i, hashmap[nums[i]]]
