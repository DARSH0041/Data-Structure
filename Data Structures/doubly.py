class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class doublelst:
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
            new.prev=temp.next
    def insert_beg(self,data):
        new=Node(data)
        temp=self.head
        new.next=temp
        temp.prev=new
        self.head=new
    def insert_mid(self,data,i):
        new=Node(data)
        temp=self.head
        while i>1:
            temp=temp.next
            ele=temp.next
            i-=1
        new.next=ele
        ele.prev=new.next
        temp.next=new
        new.prev=temp.next
    def del_end(self):
        temp=self.head.next
        pr=self.head
        while temp.next:
            temp=temp.next
            pr=pr.next
        pr.next = None

    def delete_beg(self):
        temp = self.head
        self.head = temp.next
        temp.prev = None

    def delete_mid(self, pos):
        new = self.head
        temp = self.head.next
        while pos>1:
            temp = temp.next
            new = new.next
            pos-=1
        new.next = temp.next
        temp.prev = new

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

arr=[5,14,9,2,6]
obj = doublelst()
#arr=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(arr)):
    obj.create(arr[i])
obj.display()
"""obj.insert_beg(0)
obj.display()
obj.insert_mid(4,4)
obj.display()
obj.del_end()
obj.delete_mid(4)
obj.display()
obj.delete_beg()
obj.display()
"""
obj.insert_beg(100)
obj.display()
