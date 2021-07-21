# diagonal_sum-of-spiral_matrix
Consider a spiral square matrix below:

|**1** | 2 | 3 | 4 |  **5** |<br />
|16 |**17** |18 |**19** |6|<br />
|15 |24| **25** |20  |7|<br />
|14 |**23** |22 |**21**| 8|<br />
|**13**| 12 |11 |10 |**9**|<br />

We have to find the sum of diagonal elements(highlighted elements) given a number **n** (odd number), where n*n is the number of elements to form square sprial matrix.
For above matrix sum = 1+17+25+21+9+13+23+19+5 = 133

Example, if n=7, n*n = 49 then the matrix would look like:

**1**  2  3  4  5  6  **7**<br />
24 **25** 26 27 28 **29** 8<br />
23 40 **41** 42 **43** 30 9<br />
22 39 48 **49** 44 31 10<br />
21 38 **47** 46 **45** 32 11<br />
20 **37** 36 35 34 **33** 12<br />
**19** 18 17 16 15 14 **13**<br />

sum = 1+25+41+49+45+33+13+19+37+47+43+29+7=389

Python Code: 

```Python
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

