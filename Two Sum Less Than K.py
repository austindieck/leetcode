

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        #Cut out all numbers greater than k
        newnums = []
        for i in nums:
            if(k > i):
                newnums.append(i)
        
        #Obtain all possible sum possibilities
        sums = []
        for i in newnums:
            for j in newnums:
                if(j != i):
                    s = 0
                    s = i + j
                    sums.append(s)
               
        #Remove all sums greater than k
        newsums = []
        for i in sums:
            if(i < k):
                newsums.append(i)
              
        #Pull out and return best sum
        best = max(newsums)
        return best
