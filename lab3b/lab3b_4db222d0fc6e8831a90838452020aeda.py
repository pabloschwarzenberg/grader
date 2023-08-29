#calculadora
numeros=[]
numero=0
cantidad=0
suma=0

while numero!=-1:
 numero=int(input('ingrese numero:'))
 if numero==-1:
     break
 cantidad=cantidad+1
 suma=suma+numero
 numeros.append(numero)




if len (numeros)==0:
    print('cantidad=0')
    print('suma=0')
    print('maximo=nd')
else:
     print('cantidad=',cantidad)
     print('suma=',suma)
     print('maximo=',max(numeros))
    
