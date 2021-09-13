import collections
import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        #Step 1 :  get freq dict
        freq = collections.Counter(arr)

        #step 2(a) : flip the freq dict and store it in heap
        #Ex : freq = {9:2,10:1} after flip and multiplt, heap = {-2:9, -1:10}
        heap = []
        for key, values in freq.items():
            #multiply -1 to the values to make it maxheap
            heap.append((-1*values, key))

        #heapify to get the max on the front of the list
        heapify(heap)

        size = len(arr)
        length = size

        #step 3:pop the number/val from key,val in the heap. Ex : pop({-2,9}[1])=9

        for i in range(len(heap)):
            #get the freq of the popped element
            #occ = freq[heappop(heap)[1]]
            occ = -1*heappop(heap)[0]
            #subract freq from length to get new length
            length = length - occ
            #check condition
            if length <= size/2:
                return i+1
