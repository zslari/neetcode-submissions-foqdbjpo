class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Iterate through arr, maintain what is current maximum value to the right by comparing to current value
        if i > current maximum value to the right, insert into array the current highest value to the right
        If arr[i] is not as high value as current maximum
        """

        new_arr = []

        current_maximum = max(arr)

        for i in range(0, len(arr)):
            if arr[i] < current_maximum:
                new_arr.append(current_maximum)
            else:
                slice_array = arr[i:]
                if len(slice_array) > 1:
                    slice_array.pop(0)
                    new_maximum = max(slice_array)
                    current_maximum = new_maximum
                    new_arr.append(current_maximum)
                else:
                    new_arr.append(current_maximum)
        
        arr = [i for i in new_arr]
        arr[-1] = -1

        return arr
