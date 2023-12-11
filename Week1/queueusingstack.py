#Link -> https://leetcode.com/problems/implement-queue-using-stacks/submissions/

class MyQueue:

    def __init__(self):
        self.arr = []
        

    def push(self, x: int) -> None:
        self.arr.append(x)
        

    def pop(self) -> int:
        val = len(self.arr) != 0 and self.arr.pop(0)
        return val
        

    def peek(self) -> int:
        return len(self.arr) != 0 and self.arr[0]
        

    def empty(self) -> bool:
        return len(self.arr) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()