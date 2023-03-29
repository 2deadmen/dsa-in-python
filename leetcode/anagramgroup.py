class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        new =[]
        for i in strs:
            l1=list(i)
            l1.sort()
            inside=[]
            for j in range(1,len(strs)):
                if len(strs) > 1:
                    l2=list(strs[j])
                    l2.sort()
                    if not i in inside:
                        inside.append(i)
                        strs.remove(i)
                    if l1==l2:
                        inside.append(strs[j])
                        strs.remove(strs[j])
                    new.append(inside)
                
        return new
ana=Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(ana.groupAnagrams(strs))            


