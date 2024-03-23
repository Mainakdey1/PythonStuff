def stupid(n, arrs):
    ret=0
    temp_sum=sum(arrs)
    for i in range(n):
        temp_sum=temp_sum-arrs[i]
        ret+=arrs[i]*temp_sum
        


    return ret


n=int(input())
arrs=list(map(int, input().split()))
print(stupid(n, arrs))
