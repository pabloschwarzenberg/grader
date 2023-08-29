n=int(input())
M=n//1000
m=str(M)
C=(n//100)%10
c=str(C)
D=(n//10)%10
d=str(D)
U=n%10
u=str(U)
if M==0 and C==0 and D==0:
    print(u+"U")
elif M==0 and C==0:
    print(d+"D","+",u+"U")
elif M==0:
    print(c+"C","+",d+"D","+",u+"U")
else:
    print(m+"M","+",c+"C","+",d+"D","+",u+"U")

