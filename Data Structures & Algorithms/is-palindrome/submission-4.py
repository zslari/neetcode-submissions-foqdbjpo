class Solution:
    def isPalindrome(self, s: str) -> bool:

        ## Turn into an array of letters after removing spaces
        ## Cut array into two pieces
        ## Check if first array is equal to second array reversed

        print(s)
        
        # cleaned_string = [i for i in s if i != " "]
        cleaned_string = "".join([char for char in s if char.isalnum()]).lower()
        print(f"Cleaned String: {cleaned_string}")

        length_string = int(len(cleaned_string))

        ## [tabacat] length 7, we want 0:2 and 4:6

        ## [tabbat]  length 6, we want 0:2 and 3:5
                

        print(f" Length of cleaned string: {length_string}")

        first_half = None
        second_half = None

        if length_string % 2 == 0:  # s is even in length
            first_half = cleaned_string[0:int((length_string) / 2)]
            print(f"First Half: {first_half}")
            second_half = cleaned_string[int((length_string / 2)) : (length_string)]       # s[3:]
            print(f"Second Half: {second_half}")
        else:  # s length is odd
            print("You are here")
            first_half = cleaned_string[0:int((length_string - 1) / 2)]
            print(f"First Half: {first_half}")

            print(length_string + 1)
            print((length_string + 1) / 2)
            print(int(((length_string + 1) / 2)))
            print(length_string - 1)
            second_half = cleaned_string[int(((length_string + 1) / 2)) : length_string] 
            print(f"Second Half: {second_half}")

        second_half_reversed = second_half[::-1]
        print(f"Second Half Reversed: {second_half_reversed}")

        return first_half == second_half_reversed
        