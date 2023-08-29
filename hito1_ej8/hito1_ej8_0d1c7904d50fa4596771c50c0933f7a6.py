numero=int(input("ingrese numero: "))
b=str(numero)
c=list(b)
j=0
for i in c:
    j=j+1
  
if j==1:
    print(c[0]+"U")

elif j==2:
    
    print(c[0]+"D","+",c[1]+"U")

elif j==3:
    print(c[0]+"C","+",c[1]+"D","+",c[2]+"U")

elif j==4:
    print(c[0]+"M","+",c[1]+"C","+",c[2]+"D","+",c[3]+"U")