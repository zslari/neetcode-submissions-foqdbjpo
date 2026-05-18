class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Iterate through nums, pop all values that are not val

        Get count of number of elements in set of nums after val has been removed

        """
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)
