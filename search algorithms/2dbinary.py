def searchMatrix( matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        startl=0
        endl=len(matrix) -1
      
        
        while startl <= endl:
            midl=startl + (endl - startl)//2
            start=0
            end=len(matrix[midl])-1

            while start <= end:
                mid= start + (end - start)//2
                print(matrix[midl][mid])
                if matrix[midl][mid]==target:
                    return True
                elif matrix[midl][mid] > target:
                    end = mid-1
                else:
                    start=mid+1
            
            if target > matrix[midl][-1]:
                startl = midl+1
            else:
                endl  = midl -1
        return False


print(searchMatrix( [[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))