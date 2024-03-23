k,n,w = map(int, input().split())


lc=((k*(w)*(w+1))/2)-n
if lc<=0:
    print(0)
else:
    print(int(lc))