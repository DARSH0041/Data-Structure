def find_change(lst,t,c):
    if t>0:
        for i in range(len(lst)):
            if lst[i]<=t:
                t-=lst[i]
                c+=1
                break
            else:
                pass
        return find_change(lst,t,c)
amount=[8,5,4,3,2]
target=10
amount.sort()
c=0
find_change(amount,target,c)
print(c)