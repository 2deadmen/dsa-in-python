class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        new=[]
        num = len(strs)
        i=0
        while num > 0:
            l1=list(strs[i])
            l1.sort()
            inside=[]
            j=0
            inside.append(strs[0])
            strs.remove(strs[0])
            num=len(strs)
            while num > 0 and j < num:
                anag=strs[j]
                l2=list(strs[j])
                l2.sort()
                if l1==l2:
                    inside.append(anag)
                    strs.remove(anag)
                else:
                    j+=1
                num=len(strs) 
                
                     
 
            inside.sort()
            if inside not in new and inside != []:
                new.append(inside) 
            
        return new
sl=Solution()
print(sl.groupAnagrams(["a"]))