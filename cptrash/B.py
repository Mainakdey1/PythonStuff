n,x=input().split()
a=input().split(" ")

def sequence(a):
    for _ in range(len(a)):
        for _ in range(len(a)-1):

            if int(a[_])>=int(a[_+1]):
                k=a[_+1]
                a[_+1]=a[_]
                a[_]=k
            else:
                pass
    return a
n=int(n)
x=int(x)
new=sequence(a[1:len(a)-1])

sum=0
for _ in range(len(new)):
    sum+=int(new[_])



answer=x-sum
new=sequence(new+[answer,])
newsum=0
for _ in range(len(new)):
    newsum+=int(new[_])


if newsum==x:
    print(answer)
elif newsum<x:
    print(-1)
else:
    print(0)