numero=input("Ingresa Numero a Descomponer: ")
largo_numero=len(numero)
numero=eval(numero)
#NUM = 1235

# Para 36 debe imprimir: 3D + 6U

UM=''
C=''
D=''
U=''
a=numero
b=0

i=1
while (a!=0) and i<=largo_numero:
        b=a%10
        a=a//10
        if i==1:
           U=str(b)
        elif i==2:
           D=str(b)
        elif i==3:
           C=str(b)
        elif i==4:
           UM=str(b)
        i=i+1

if largo_numero==4:
   Cadena=UM+'M+'+C+'C+'+D+'D+'+U+'U'
   print(Cadena)
   #print(UM,'M+',C,'C+',D,'D+',U,'U')
elif largo_numero==3:
   Cadena=C+'C+'+D+'D+'+U+'U'
   print(Cadena)
   #print(C,'C+',D,'D+',U,'U')
elif largo_numero==2:
   Cadena=D+'D+'+U+'U'
   print(Cadena)
   #print(D,'D+',U,'U')
elif largo_numero==1:
   Cadena=U+'U'
   print(Cadena)
   #print(U,'U')