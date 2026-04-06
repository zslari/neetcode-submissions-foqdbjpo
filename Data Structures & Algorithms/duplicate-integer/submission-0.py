class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        number_elements_nums = len(nums)
        print(number_elements_nums)
        set_list_nums = set(nums)
        print(set_list_nums)
        number_elements_set_list_nums = len(set_list_nums)

        if number_elements_nums == number_elements_set_list_nums:
            return False
        else:
            return True


        