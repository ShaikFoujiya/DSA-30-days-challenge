class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=len(nums)
        pos=0
        for i in range(l):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        for i in range(pos,l):
            nums[i]=0 
        return nums               
