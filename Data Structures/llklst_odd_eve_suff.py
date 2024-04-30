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

    def insert_end(self, data):
        new_node = data
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

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
    def odd_eve_suff(self):
        lst=[]
        lst1=[]
        c=0
        while self.head:
            if c==0:
                lst1.append(self.head)
                self.head=self.head.next
                c+=1
            elif c%2==0:
                lst1.append(self.head)
                self.head=self.head.next
                c+=1
            else:
                lst.append(self.head)
                self.head = self.head.next
                c+=1
        i = 0
        lst = lst[::-1]
        """self.create(lst[0].data)
        self.create(lst1[0].data)"""
        while i<len(lst) and i<len(lst1):
            self.create(lst1[i].data)
            self.create(lst[i].data)
            i+=1
        while i<len(lst1):
            self.create(lst1[i].data)
            i+=1
obj = LinkedList()
arr=[0,1,2,3,4,5,6,7,8,9,10]
for i in range(len(arr)):
    obj.create(arr[i])
obj.display()
obj.odd_eve_suff()
obj.display()