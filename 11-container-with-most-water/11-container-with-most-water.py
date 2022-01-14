class Solution(object):
    val=0
    def maxArea(self, height):
        val=0
        i,j=0,len(height)-1
        
        while i<j:
            area=(j-i)*min(height[i],height[j])
            val=max(val,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return val
        
        """
        :type height: List[int]
        :rtype: int
        """
        
         
                    
