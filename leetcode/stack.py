class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        sa=list(s)
        flag=True
        copy=list(s)
        for i in sa:
          if i in copy:
            copy.remove(i)
            if i == '(':
                i=')'
            elif i== '[':
                i=']'
            elif i=='{':
                i='}'
            elif i == ')':
                i='('
            elif i== ']':
                i='['
            elif i== '}':
                i='{'
            if i in copy:
                copy.remove(i) 
          if copy !=[]:
            flag=False
   
        return flag

sl=Solution()
print(sl.isValid("()[]"))
