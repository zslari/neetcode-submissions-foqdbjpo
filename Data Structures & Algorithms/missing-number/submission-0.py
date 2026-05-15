class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        range_nums = [i for i in range(0, len(nums)+1) if i not in nums]
        print(range_nums)
        print(nums)

        ## which number is in range_nums that is not in nums

        return range_nums[0]



        