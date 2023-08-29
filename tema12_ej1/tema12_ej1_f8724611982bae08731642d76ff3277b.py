import itertools as it
n=int(input())
r=it.product([0,1],repeat=n)

r=list(r)
for i in r:
    string=""
    for x in range(n):
        a=str(i[x])
        string+=a
        a=""
    print(string)

