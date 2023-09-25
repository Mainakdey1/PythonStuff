n=int(input())
answer=[]
for _ in range(n):
    k=int(input())
    sdict={}
    xlist=[]
    ylist=[]
    for _ in range(k):
        x,y=input().split()
        sdict.update({x:y,})
        xlist+=[int(x),]
        ylist+=[int(y),]
        
    print(max(xlist))
    ps=xlist[0]
    max_strength=max(xlist)
    xlist.pop(0)
    
    if sdict[str(ps)]<=sdict[str(max_strength)]:
        answer+=["-1",]
    else:
        max_endurance=max(ylist)
        ylist.pop(0)
        
        value = {i for i in sdict if sdict[i]==str(max_endurance)}
        value=int(value.pop())
        print(type)
        value=value+1
        answer+=[value,]





for j in answer:
    print(j)


            
        


