#calculadora
n1=int(input("ingrese un numero: "))

C=0
E=-1
S=0
M=0
S=S+n1
while n1!=E:
    print("el numero vale",n1)
    if M<n1:
        print("aca")
        M=n1
    C=C+1
    n1=int(input("ingrese un numero: "))
    S=S+n1
    
 

print("cantidad=",C)
   
print("suma=",S+1)    
if C==0:
    print("maximo=nd")
else:
    print("maximo=",M)

      