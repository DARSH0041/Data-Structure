length=5
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_beg(self,data):
        c=self.lstlen()
        if c<=length:
            new=Node(data)
            t = self.head
            temp = self.head
            temp = temp.next
            while temp.next != t:
                temp = temp.next
            temp.next = new
            new.next=self.head
            self.head=new
        else:
            print('over flow for',data)
    """def insert_mid(self,data,i):
        new=Node(data)
        temp=self.head
        while i>1:
            temp=temp.next
            ele = temp.next
            i-=1
        new.next=ele
        temp.next = new"""
    def create(self, data):
        new = Node(data)
        if self.head is None:
            self.head=new
            new.next=self.head
        else:
            c = self.lstlen()
            print("c",c,data)
            if c<=length:
                t = self.head
                temp = self.head
                temp = temp.next
                while temp.next != t:
                    temp = temp.next
                temp.next = new
                new.next = self.head
            else:
                print('over flow for',data)
    """def delete_beg(self):
        t = self.head
        temp = self.head
        temp = temp.next
        while temp.next != t:
            temp = temp.next
        self.head=t.next
        temp.next=self.head"""
    def delete_end(self):
        c=self.lstlen()
        print(c)
        if c>=0:
            t=self.head
            temp = self.head.next
            prev = self.head
            while temp.next != t:
                temp = temp.next
                prev = prev.next
            prev.next = self.head
        else:
            print('under flow')
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
    def lstlen(self):
        c=-1
        if self.head is None:
            return c
        else:
            temp=self.head
            t=temp.data
            temp = temp.next
            while temp.data != t:
                c+=1
                temp = temp.next
            return c
obj = LinkedList()
arr=[1,2,3,4,5,6,7,8,9]
for i in range(len(arr)):
    obj.create(arr[i])
obj.display()
obj.insert_beg(0)
obj.delete_end()
"""obj.display()
obj.insert_mid(4,4)
obj.display()
obj.delete_beg()
obj.display()
obj.delete_mid(4)
obj.display()
obj.delete_end()
obj.display()"""