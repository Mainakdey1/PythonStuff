def recurse(arrs,n, count):
    for  i in range(n-1):
        if arrs[i]=='0' and arrs[i+1]=='1' or arrs[i]=='1' and arrs[i+1]=='0':
            count+=1
            del(arrs[i:i+2])
            return recurse(arrs,len(arrs), count)
            break


    return 2*count


arrs=list(input())

print(recurse(arrs, len(arrs), 0))



