def num_palace(array):
    for i in array:
        temp=[]
        for j in i:

            if j not in temp:
                temp+=[j,]
            else:
                return 0
            
    for i in array:
        temp_col=[]
        if i[0] not in temp_col:
            temp_col+=[i[0],]
        else:
            return 0
        
    return 1

array=[]
for _ in range(9):
    row_arr=list(map(int, input().split()))

    array+=[row_arr,]

if num_palace(array):
    print("Yes")

else:
    print("No")