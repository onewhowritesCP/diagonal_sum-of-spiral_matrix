input_arr=[1,2,3,
           4,5,6,
           7,8,9]



n = int(len(input_arr)**0.5)

result = []
temp = []

for i in range(1,n*2):

    if i > n:
        i = 2*n-i

    sub_result = []

    for k in range(0,n*n):

        if input_arr[k] not in temp:
            idx = k
            while (len(sub_result)<i) and idx < n*n:
                temp.append(input_arr[idx])
                sub_result.append(input_arr[idx])
                idx += (n-1)
            print(temp)
            print(sub_result)
            result.append(sub_result)

            if len(sub_result)==i:break
print(result)
