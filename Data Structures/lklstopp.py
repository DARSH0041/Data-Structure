class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.count=0
    def create(self, data):
        new = Node(data)
        if self.head is None:
            self.head=new
            self.count+=1
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            self.count+=1
    def function(self):
        temp=self.head
        lst=[]
        for i in range(self.count):
            if temp.data % 2 == 0:
                lst.append(i)
            else:
                if len(lst)>0:
                    self.function1(lst)
                    lst=[]
            temp = temp.next
        print(lst)
    def function1(self, arr):
        temp=self.head.next
        pr=self.head
        a=arr[0]
        b=arr[len(arr)-1]
        node=[]
        count=0
        start=-1
        end=-1
        while pr.next:
            if count == a:
                if a!=0:
                    start=pr
            elif count==b:
                end = temp.next
            if count in arr:
                node.append(pr.data)
            count+=1
            temp=temp.next
            pr=pr.next
        node=node[::-1]
        for i in node:
            print(i,end='>')

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
arr=[2,18,24,3,5,7,9,12,6]
for i in range(len(arr)):
    obj.create(arr[i])
obj.function()
#obj.display()