class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Iterate through nums with a counter, reset whenever i is not 1 and store maximum
        """

        total = 0
        counter = 0

        for i in nums:
            if i == 1:
                counter += 1
                if counter > total:
                    total = counter
            else:
                counter = 0
        
        return total
                



        
        