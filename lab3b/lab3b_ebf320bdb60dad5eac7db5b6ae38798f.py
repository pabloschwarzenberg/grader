#calculadora
n=[]
cantidad=int(0)
maximo=0
suma=0
numero=0
while numero!=-1:
   numero=int(input("ingrese un numero"))
   if numero!=-1:
      n.append(numero)
for k in n:
   suma+=k
if len(n)>0:
   print('cantidad=',len(n))
   print('maximo=', max(n))
   print('suma=', suma )
else:
   print('cantidad=',0)
   print('maximo=nd')
   print('suma=',0)     