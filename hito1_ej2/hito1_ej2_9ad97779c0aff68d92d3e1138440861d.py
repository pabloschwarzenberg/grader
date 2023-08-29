Telefono=int(input("Ingrese numero de telefono:"))
Hora=float(input("Hora de llamada"))

D=Telefono//10**7
C=(Telefono-(10**7*D))//10**6
U=(Telefono-(10**7*D)-(10**6*C))//10**5
a=(Telefono-(10**7*D)-(10**6*C)-(10**5*U))//10**4
b=(Telefono-(10**7*D)-(10**6*C)-(10**5*U)-(10**4*a))//10**3
c=(Telefono-(10**7*D)-(10**6*C)-(10**5*U)-(10**4*a)-(10**3*b))//10**2
m=(Telefono-(10**7*D)-(10**6*C)-(10**5*U)-(10**4*a)-(10**3*b)-(10**2*c))//10**1
f=(Telefono-(10**7*D)-(10**6*C)-(10**5*U)-(10**4*a)-(10**3*b)-(10**2*c)-(10**1*m))//1


if 0<=Hora<=7:
    print("CONTESTAR")
    
elif Hora<14 and c==9 and m==0 and f==9:
     print("CONTESTAR")
    
elif 17<=Hora<=19 and D!=8 and C!=7 and U!=7:
    print ("CONTESTAR")
   
else:
    print ("NO CONTESTAR")
