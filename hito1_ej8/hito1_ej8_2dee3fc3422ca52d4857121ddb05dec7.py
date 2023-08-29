nu=input("Ingrese un numero")
n=len(nu)
i=0
u=len(nu)
while i<n:
    letter=nu[i]
    if(u==4):
        print(letter+"M",end=" + ")
    elif(u==3):
        print(letter+"C", end=" + ")
    elif(u==2):
        print(letter+"D", end=" + ")
    elif(u>=1):
        print(letter, "U")
    u-=1
    i+=1