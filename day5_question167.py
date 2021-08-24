class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(numbers)):
            #print("i = ", i, " nums = ", nums[i])
            #if target > nums[i]:
            #print("sinsie greater than")
            diff = target - numbers[i]
            #print("diff = ", diff)
            #else:
                #print("inside lesser than")
                #diff  = nums[i] - target
                #print("diff = ", diff)

            if numbers[i] not in hashmap.keys():
                #print("diff not in dict")
                hashmap[diff] = i
                #print("hashmap = ", hashmap)

            else:
                #print("diff found in dict")
                #print("resutl = ", [i, hashmap[nums[i]]])
                return [hashmap[numbers[i]]+1,i+1]
