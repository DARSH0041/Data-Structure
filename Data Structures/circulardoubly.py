class Node:
    def __init__(self,data):
        self.prev=None
        self.data = data
        self.next = None
class circularlst:
    def __init__(self):
        self.head = None

    def insert_beg(self,data):
        new=Node(data)
        temp=self.head.prev
        t=self.head
        self.head=new
        self.head.next = t
        self.head.prev=temp
        temp.next = self.head
        t.prev=self.head
    def create(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = self.head
            new.prev = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new
            self.head.prev = new
            new.prev=temp
            new.next=self.head
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
        dlt=self.head.prev
        last=dlt.prev
        self.head.prev=last
        last.next = self.head
    def delete_beg(self):
        temp = self.head
        last=self.head.prev
        first=temp.next
        self.head=first
        self.head.prev=last
        last.next=self.head
        temp= None
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
            t=temp.data
            temp = temp.next
            print(t,'=>',end='')
            while temp.data != t:
                print(temp.data,"=>",end="")
                temp = temp.next
            print()
obj = circularlst()
arr=[1,2,3,4,5,6,7,8,9]
for i in range(len(arr)):
    obj.create(arr[i])
obj.insert_beg(0)
obj.insert_mid(4,4)
obj.display()
obj.delete_mid(4)
obj.display()
obj.create(10)
obj.display()
obj.delete_beg()
obj.display()
obj.del_end()
obj.display()
obj.del_end()
obj.display()