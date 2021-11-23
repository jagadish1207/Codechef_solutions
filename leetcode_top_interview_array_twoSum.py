from typing import List


#700+ ms
def twoSum(nums: List[int], target: int) -> List[int]:
    l1 = []
    for i in range(0,len(nums)-1):
        t = target - nums[i]
        nums[i] = 8777
        if (t in nums and nums.index(t)!=i):
            l1.append(i)
            l1.append(nums.index(t))
            return l1
    return l1

#50ms
def twoSumOptimmal(nums: List[int], target: int) -> List[int]:
        complement = {}
        
        for i in range(len(nums)):
            if target - nums[i] in complement:
                return [complement[target - nums[i]], i]
            
            complement[nums[i]] = i

print(twoSum([3,3],6))