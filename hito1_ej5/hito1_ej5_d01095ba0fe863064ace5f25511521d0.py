#Cálculo del dígito verificador de un rut
rut=(input())
lista=list(rut)
K=str("K")
if len(lista)==7:
   a=int(lista[6])*(2)
   b=int(lista[5])*(3)
   c=int(lista[4])*(4)
   d=int(lista[3])*(5)
   e=int(lista[2])*(6)
   f=int(lista[1])*(7)
   g=int(lista[0])*(2)
   suma=a+b+c+d+e+f+g
   resto=suma%11
   resultado=11-resto
   if resultado==11:
     digito=0
   elif resultado==10:
     digito=K
   else:
     digito=resultado
if len(lista)==8:
   a=int(lista[7])*(2)
   b=int(lista[6])*(3)
   c=int(lista[5])*(4)
   d=int(lista[4])*(5)
   e=int(lista[3])*(6)
   f=int(lista[2])*(7)
   g=int(lista[1])*(2)
   h=int(lista[0])*(3)
   suma=a+b+c+d+e+f+g+h
   resto=suma%11
   resultado=11-resto
   if resultado==11:
     digito=0
   elif resultado==10:
     digito=K
   else:
     digito=resultado
print("dv=",digito)     