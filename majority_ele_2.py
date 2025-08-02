class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt1,cnt2 = 0,0
        ele1 = float('-inf')
        ele2 = float('-inf')

        for i in range(n):
            if cnt1 == 0 and ele2 != nums[i]:
                cnt1 = 1
                ele1 = nums[i]
            
            elif cnt2 == 0 and ele1 != nums[i]:
                cnt2 = 1
                ele2 = nums[i]
            elif nums[i] == ele1:
                cnt1 += 1
            elif nums[i] == ele2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            
        ls = []
        cnt1,cnt2 = 0,0
        for i in range(n):
            if nums[i] == ele1:
                cnt1 += 1
            if nums[i] == ele2:
                cnt2 += 1
            
        mini = int(n / 3) + 1
        if cnt1 >= mini:
            ls.append(ele1)
        if cnt2 >= mini:
            ls.append(ele2)

        return ls

