
def reverseString( s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        copys=s
        for i in range(0,len(s)-1):
            ele=copys.pop()
            s.insert(i,ele)
            print(s)
            s[:len(s)//2]
      

        return s
        
print(reverseString(["h","e","l","l","o"]))
