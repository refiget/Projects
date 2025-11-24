



class Solution:
    def __init__(self, nums, target):
        self.nums =  nums
        self.target = target

    def twoSum(self):
        i = 0
        for j in range(i + 1,len(self.nums)):
            if self.nums[i] + self.nums[j] == self.target:
                return [i,j]
                
            else:
                i += 1
        
        return "There are no such indices"   
                    
        






