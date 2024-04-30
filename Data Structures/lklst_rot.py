class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def create(self, data):
        new = Node(data)
        if self.head is None:
            self.head=new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
    def delete_beg(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
    def rotat(self,data):
        data1=data
        temp=self.head
        while data>=1:
            self.create(temp.data)
            temp=temp.next
            self.delete_beg()
            data-=1
    def display(self):
        if self.head is None:
            print("The Linked List is Empty")
        else:
            temp=self.head
            while temp:
                if temp.next is None:
                    print(temp.data,end="")
                else:
                    print(temp.data,"=>",end="")
                temp = temp.next
            print()
obj = LinkedList()
arr=[1,2,3,5,6,7,8,9]
for i in range(len(arr)):
    obj.create(arr[i])
obj.display()
obj.rotat(4)
obj.display()