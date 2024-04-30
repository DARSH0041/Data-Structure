class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_beg(self,data):
        new=Node(data)
        new.next=self.head
        self.head=new
    def insert_mid(self,data,i):
        new=Node(data)
        temp=self.head
        while i>1:
            temp=temp.next
            ele = temp.next
            i-=1
        new.next=ele
        temp.next = new
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
    def delete_mid(self,pos):
        temp = self.head.next
        prev = self.head
        while pos>1:
            temp = temp.next
            prev = prev.next
            pos-=1
        prev.next = temp.next
    def delete_end(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
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
obj.insert_beg(0)
obj.insert_mid(4,4)
obj.delete_beg()
obj.delete_mid(2)
obj.delete_end()
obj.display()