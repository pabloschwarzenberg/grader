p=int(input())

if p==2:
    print(2)

for n in range(2,p):
    while p/n==p//n:
        p/=n
        print(n)