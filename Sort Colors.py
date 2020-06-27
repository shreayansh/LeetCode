class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeroPtr = 0
        twoPtr = len(nums) - 1
        index = 0
        
        while( index <= twoPtr and zeroPtr < twoPtr ):            
            if( nums[zeroPtr] == 0 ):
                zeroPtr += 1
                index += 1
                continue
                            
            if( nums[twoPtr] == 2 ):
                twoPtr -= 1
                continue
            
            if( nums[index] == 2 ):
                nums[index] , nums[twoPtr] = nums[twoPtr], nums[index]
                continue
                
            if( nums[index] == 0 ):
                nums[index] , nums[zeroPtr] = nums[zeroPtr], nums[index]
                continue
            
            if( nums[index] == 1):
                index += 1
        
        return nums