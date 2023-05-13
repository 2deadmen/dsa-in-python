class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dicty={}
        
        for i in range(len(nums)):
            if nums[i] in dicty.keys():
                count=dicty[nums[i]]
                count+=1
                dicty[nums[i]]=count
            else:
                dicty[nums[i]]=1
        result=[]
        count=1
        print(dicty)

        for i in range(k+1):
            if count > k:
                break
            val=max(dicty,key=dicty.get)
            result.append(val)
            del dicty[val]
            count+=1
        return result
        


   
sl=Solution()
print(sl.topKFrequent([4,1,-1,2,-1,2,3],2))
