#calculadora
numero=0
numeros=[]
cuenta=0
cantidad=0
promedio=0
while numero!= -1:
   numero=int(input("ingrese numero:"));
   if numero==-1:
    break
   
   numeros.append(numero)

   cantidad=cantidad+numero
   cuenta=cuenta+1
   promedio=cantidad/cuenta
 
print("cantidad=",cuenta)
if cuenta>0:
    print("promedio=",round(promedio,1))
    print("valor minimo=",min(numeros))
if cuenta==0:
    print("promedio=nd")
    print("valor minimo=nd")
