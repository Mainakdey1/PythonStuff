def drawline(n):
    if n<=0:
        return False
    else:
        print("-"*n)
        
def drawinterval(k):
    if k<=0:
        return False
    else:
        drawinterval(k-1)
        drawline(k)
        drawinterval(k-1)
        
def ruler(limit,maxlen):
    drawline(maxlen)
    for i in range(limit):
        drawinterval(maxlen-1)
        drawline(maxlen)
        
        

m,n=map(int,input().split())
print(ruler(m,n))