"""
ID: mainakd1
LANG: PYTHON3
PROG: gift1

"""

fin=open("gift1.in","r")
fout=open("gift1.out","w+")


n=int(fin.readline())
namedict={}
for i in range(n):
    name=fin.readline()
    namedict.update({name:0,})

for i in range(n):
    giver=fin.readline()
    amt,k=map(int,fin.readline().split())

    tmplist=[]
    for i in range(k):
        tmp=fin.readline()
        tmplist+=[tmp,]

    if k==0:
        div_amt=0
        rem_amt=0  
    else:
        div_amt=amt//k
        rem_amt=amt%k
    for j in namedict:
        if j==giver:
            namedict.update({j:namedict[j]+rem_amt})
            namedict.update({j:namedict[j]-amt})
        elif j in tmplist:
            namedict.update({j:namedict[j]+div_amt})
        else:
            pass



for i in namedict:
    fout.write("{} {} ".format(i,str(namedict[i])))

fout.close()




