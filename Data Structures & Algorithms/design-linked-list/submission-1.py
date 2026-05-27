class MyLinkedList:

    def __init__(self):
        self.holder = []

    def get(self, index: int) -> int:
        try:
            return self.holder[index]
        except IndexError:
            return -1

    def addAtHead(self, val: int) -> None:
        self.holder.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.holder.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        self.holder.insert(index, val)
        

    def deleteAtIndex(self, index: int) -> None:
        try:
            self.holder.pop(index)
        except IndexError:
            return None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)