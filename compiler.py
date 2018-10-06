class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def isempty(self):
        return True if self.head is None else False
    def pop(self):
        if self.isempty():
            return "Stack is empty"
        temp = self.head
        self.head = self.head.next
        return temp.data
    def peek(self):
        return self.head.data
    def printSt(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
if __name__=='__main__':
    st = Stack()
    for i in range(int(input())):
        command = input()
        count = 0
        print("Entered command",command)
        for j in command:
            if j == '<':
                st.push(j)
                print("Pushed ",j)
            elif j == '>':
                print("Popped ",st.pop())
                count +=2
            print("Stack ", st.printSt())
        print("Final command",st.printSt())
        print("Final count",count)



