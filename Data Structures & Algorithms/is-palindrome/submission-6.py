class Solution:
    def isPalindrome(self, s: str) -> bool:

        ## Turn into an array of letters after removing spaces
        ## Cut array into two pieces
        ## Check if first array is equal to second array reversed
        
        cleaned_string = "".join([char for char in s if char.isalnum()]).lower()
        print(f"Cleaned String: {cleaned_string}")

        length_string = int(len(cleaned_string))
                
        print(f" Length of cleaned string: {length_string}")

        first_half = None
        second_half = None

        if length_string % 2 == 0:  # s is even in length
            first_half = cleaned_string[0:int((length_string) / 2)]
            second_half = cleaned_string[int((length_string / 2)) : (length_string)]       # s[3:]
        else:  # s length is odd
            first_half = cleaned_string[0:int((length_string - 1) / 2)]

            second_half = cleaned_string[int(((length_string + 1) / 2)) : length_string] 

        second_half_reversed = second_half[::-1]

        return first_half == second_half_reversed
        