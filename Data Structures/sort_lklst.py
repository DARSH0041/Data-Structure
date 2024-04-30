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

    def sortfun(self):
        temp=self.head
        data=temp.data
        c=0
        while c!=2:
            if temp.data==data:
                c+=1
            else:
                temp1 = self.head
                d=0
                while d!=2:
                    if temp1.data == data:
                        d += 1
                    else:
                        next1=temp1.next
                        if temp1.data>next1.data:
                            temp1.data,next1.data=next1.data,temp1.data
                    temp1=temp1.next
            temp=temp.next
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
arr=[7,3,6,4,1,9]
for i in range(len(arr)):
    obj.create(arr[i])
obj.display()
obj.sortfun()
obj.display()