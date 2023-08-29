num=int(input())
n_b=[]
while num!=0:
    n=str(num%2)
    num=num//2
    n_b.append(n)
n_b.reverse()
n_b="".join(n_b)
print("resultado=",n_b)