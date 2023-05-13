class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
  
        lengths=[]
        length =1
        if len(nums)==1:
            return 1
        for i in range(0,len(nums)):
            if i==len(nums)-1:
                if nums[i-1] +1 == nums[i]:
                    lengths.append(length)
                    length+=1 
                    
                    
            elif nums[i] + 1 == nums[i+1]:
                length+=1
             
            else:
                length=1
                lengths.append(length)
        

        lengths.sort()
        if len(lengths) > 0:
         return lengths[-1]
        else:
            return 0

sl=Solution()
print(sl.longestConsecutive([0]))