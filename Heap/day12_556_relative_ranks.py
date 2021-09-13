import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        # check the base case where score length = 1 or 2
        if len(score)==1:
            score[0] = "Gold Medal"
            return score

        elif len(score)==2:
            if score[0] > score[1]:
                score[0] = "Gold Medal"
                score[1] = "Silver Medal"
            else:
                score[0] = "Silver Medal"
                score[1] = "Gold Medal"
            return score

        #create a dictionary of scores and their index. key = index and val = score
        dic= dict()

        for i in range( len(score)):
            #index = score
            dic[i] = score[i]


        heap = []

        #since we want to heapify with values as the key and not the index, flip it
        for keys, values in dic.items():
            #multiply the val by -1 because heapify is minheap but we want maxheap
            heap.append((-1*values, keys))


        #This creates heap with max value at the top but all values are not sorted yet.
        heapify(heap)



        sortedkey = []
        index = []
        #Now sort heap by key by poping max element in loop. key is the score and value is the index
        for i in range(len(heap)):
            sortedkey.append(heappop(heap))
            #store the indexes in the index array. so say after sort we have index = [3,0,2,1]
            index.append(sortedkey[i][1])


        #since index array represent the sorted indexes of score arrray, we take first three.
        score[index[0]] = 'Gold Medal'
        score[index[1]] = "Silver Medal"
        score[index[2]] = "Bronze Medal"

        #for remaining indexes loop and set thier rank as i+1 because i starts from 0.
        for i in range(3, len(index)):
            score[index[i]] = str(i+1)


        return score
