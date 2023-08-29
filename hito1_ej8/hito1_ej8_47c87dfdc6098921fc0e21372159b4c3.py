n=str(input("numero de hasta 4 digitos: "))
q=str(n)[0:1]
w=str(n)[1:2]
e=str(n)[2:3]
r=str(n)[3:4]
U=r
D=e
C=w
M=q
K=0
if r==(""):
    U=e
    D=w
    C=q
    K=K+1      
if e==("") and r==(""):
        U=w
        D=q
        K=K+1          
if w==("") and r==("") and e==(""):
        U=q
        K=K+1
U=U+"U"
D=D+"D +"
C=C+"C +"
M=M+"M +"
if K==0:
    print (M,C,D,U)
if K==1:
    print(C,D,U)
if K==2:
    print(D,U)
if K==3:
    print(U)
