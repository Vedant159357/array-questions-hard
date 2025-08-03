class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: #check if current element is duplicate of previous element
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k] #the triplet

                if total > 0: #total exceeds 0 so decrement the right pointer
                    k -= 1
                elif total < 0: #total less than 0 so increment the left pointer
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k: #check that there is no duplicate triplet and if present then skip it
                        j += 1


        return res

