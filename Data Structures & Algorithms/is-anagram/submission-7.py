class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = True

        num_elements_first_dict = {}
        num_elements_second_dict = {}

        for i in s:
            if i not in num_elements_first_dict.keys():
                num_elements_first_dict[i] = 1
            else:
                num_elements_first_dict[i] += 1
        
        for j in t:
            if j not in num_elements_second_dict.keys():
                num_elements_second_dict[j] = 1
            else:
                num_elements_second_dict[j] += 1

        for k,v in num_elements_first_dict.items():
            if k not in num_elements_second_dict.keys():
                is_anagram = False
                return is_anagram
            else:
                if v != num_elements_second_dict[k]:
                    is_anagram = False
                    return is_anagram
        
        for k,v in num_elements_second_dict.items():
            if k not in num_elements_first_dict.keys():
                is_anagram = False
                return is_anagram
            else:
                if v != num_elements_first_dict[k]:
                    is_anagram = False
                    return is_anagram
        
        return is_anagram

        
        