#Cálculo del dígito verificador de un rut
def digito_verificador(n):
   suma_parcial=0
   a=str(n)
   lista=[]
   x=2
   y=0
   for i in range(len(a)):
       lista.append(a[i])
   lista.reverse()
   while y<len(lista):
       if x<8:
            z=int(lista[y])*x
            suma_parcial+=z
       else:
            x=2
            z=int(lista[y])*x
            suma_parcial+=z
       x+=1
       y+=1
       
   resto=suma_parcial%11
   digito=11-resto
   if digito==11:
        print("dv=",0)
   elif digito==10:
        print("dv=k")
   else:
        print("dv=",digito)
            
n=int(input("rut:"))
digito_verificador(n)