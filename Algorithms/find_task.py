def find_tasks(activities):
    ans=[activities[0]]
    for i in range(1,len(activities)):
        a,b=ans[-1],activities[i]
        if b[0]>a[-1]:
            ans.append(b)
    return ans,len(ans)
activities=[[3,4],[1,2],[5,7],[5,9],[0,6],[8,9]]
activities=sorted(activities,key=lambda x:x[1])
print(find_tasks(activities))