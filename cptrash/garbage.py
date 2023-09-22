n=int(input())
result=[]
for _ in range(n):
    N,s=input().split()
    N=int(N)
    s=int(s)
    lst=input().split()
    sum=0
    val=0

    while val==0:
        x=0
        for _ in lst:
            if  int(_)<=x:
                lst.remove(_)

            print(lst)
        for _ in lst:
            sum+=int(_)
        if s-sum<=0:
            x+=1
            pass
        else:
            result+=[x,]
            val=1
for _ in result:
    print(_)
