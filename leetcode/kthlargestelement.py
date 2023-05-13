class Solution(object):
    def topKFrequent(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        new=[]
        for i in nums:
            if i not in new:
                new.append(i)
        if (len(new) < 3):
            return max(new)
        else:
            new.sort()
            print(new)
            return new[-3]
        


   
sl=Solution()
print(sl.topKFrequent([3,2,1]))
