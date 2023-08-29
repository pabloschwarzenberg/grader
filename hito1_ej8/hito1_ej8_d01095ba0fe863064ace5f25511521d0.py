#Descomponer un número
numero=input()
lista=list(numero)
if len(lista)==4:
   a=lista[0]
   b=lista[1]
   c=lista[2]
   d=lista[3]
   print(a,"M +",b,"C +",c,"D +",d,"U")
elif len(lista)==3:   
   a=lista[0]
   b=lista[1]
   c=lista[2]
   print(a,"C +",b,"D +",c,"U")
elif len(lista)==2:
   a=lista[0]
   b=lista[1]
   print(a,"D +",b,"U")
elif len(lista)==1:
   a=lista[0]
   print(a,"U")
   