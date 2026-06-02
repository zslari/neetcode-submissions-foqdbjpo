class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        circle = 0
        square = 1

        When taking a sandwich (students[0] == sandwiches[0]), sandwiches.pop(0) and students.pop(0)

        When students[0] != sandwiches [0], top_student = students.pop(0) and students.append(top_student)

        Iterate in a while loop until either sandwiches and students are empty

        Or 

        Iterate in a while loop until sandwiches are all of type 1 or type 0 and students are all of opposite type

        - Check if set(sandwiches) = 1 and set(students) = 1 and
             if set(sandwitches) == set(students) continue else break

        Break

        and return len(students)
        """

        # unable_to_eat = 0


        # while sandwiches and students:
        #     if students[0] == sandwiches[0]:
        #         sandwiches.pop(0)
        #         students.pop(0)
        #     else:
        #         top_student = students.pop(0)
        #         students.append(top_student)

        #     if len(set(students)) == 1:
        #         print(f"Sandwiches end of loop: {sandwiches}")
        #         print(f"Students end of loop: {students}")
        #         if set(students) != set(sandwiches) and students[0] != sandwiches[0]:
        #             return len(students)


        # unable_to_eat = len(students)

        # return unable_to_eat


        res = len(students)

        cnt = Counter(students)

        for i in sandwiches:
            if cnt[i] > 0:
                cnt[i] -= 1
                res -= 1
            else:
                return res


        return res


        