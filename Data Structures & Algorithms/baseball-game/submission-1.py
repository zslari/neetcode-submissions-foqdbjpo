class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in operations:
            ## Special case when record is empty and no previous score and no two previous scores
            if i == '+':
                if len(record) > 0:
                    record.append(sum(record[-2:]))
                else:
                    record.append(0)
            elif i == 'C':
                if len(record) > 0:
                    record.pop(-1)
            elif i == 'D':
                if len(record) > 0:
                    record.append(int(2 * record[-1]))
                else:
                    record.append(0)
            else:
                record.append(int(i))

        return sum(record)