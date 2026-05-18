class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Iterate through arr, maintain what is current maximum value to the right by comparing to current value
        if i > current maximum value to the right, insert into array the current highest value to the right
        If i is not as high value 
        """

        new_arr = []


        sorted_values = sorted(arr)
        sorted_values.reverse()


        current_maximum = sorted_values[0]
        number_shifts = 0

        for i in range(0, len(arr)):
            print(f"value of arr at i: {arr[i]}")
            print(f"Current Maximum: {current_maximum}")
            if arr[i] < current_maximum:
                new_arr.append(current_maximum)

                print(f"New Arr: {new_arr}")
            else:
                # number_shifts += 1
                # new_maximum = sorted_values[number_shifts]
                slice_array = arr[i:]
                print(f"Slice array: {slice_array}\n")
                if len(slice_array) > 1:

                    slice_array.pop(0)
                    new_maximum = max(slice_array)
                    print(f"New Maximum:{new_maximum}")

                    current_maximum = new_maximum
                    new_arr.append(current_maximum)
                else:
                    new_arr.append(current_maximum)
        
        arr = [i for i in new_arr]
        arr[-1] = -1

        return arr
