class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        element_dict = {}

        for i in nums:
            if str(i) not in element_dict.keys():
                element_dict[str(i)] = 1
            else:
                element_dict[str(i)] += 1
        
        top_values = sorted(element_dict.values())
        top_values.reverse()
        top_values_cut = top_values[0:k]

        top_vals_to_return = [int(key) for key, val in element_dict.items() if val in top_values_cut]        
        
        return top_vals_to_return
        