N=int(input("numero:"))
i=1
r=2
a=0
cont=0
m=1
while i<N-1:
    cont=0
    r=1
    i=i+1
    if N%i==0:
        while r<i-1:
            r=r+1
            if i%r==0:
                cont=cont+1
        if cont==0:
            print(i)
            m=m*i
if N/m!=1:
    print(int(N/m))
            
