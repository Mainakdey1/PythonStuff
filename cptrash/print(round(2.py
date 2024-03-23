def cover(arrs,sum1, par_arr):
    print(arrs)
    if sum(par_arr)==sum1:
        print(par_arr)

    else:
        r=len(list(arrs))
        for i in range(r):
            par_arr=list(arrs[0:r])
            cover(arrs[i+1],sum1, par_arr)
            par_arr=list(arrs[0:r])


arr=[1,2,3]
print(cover(arr,3,[]))