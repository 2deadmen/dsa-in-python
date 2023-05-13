def search( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l <= r:
 
            mid = l + (r - l) // 2
            print(mid)
            if nums[mid] == target:
                return mid
    
        
            elif nums[mid] < target:
                l = mid + 1
    
        
            else:
                r = mid - 1
    
 
        return -1
        
print(search([-1,0,5],5))