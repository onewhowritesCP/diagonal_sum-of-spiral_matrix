n = int(input())
k=n-1
count = 0
i=1
sum = 1
while i <= n*n-1:
    count+=1
    i+=k
    print(i)
    sum+=i
    if count == 4:
        count = 0
        k-=2
print(sum)
