#Ordenar tres números
a=int(input("priemer numero: "))
b=int(input("segundo numero: "))
c=int(input("tercer numero: "))

if a<=b and a<=c:
  if b<=c:
    lista=[a,b,c]
    for i in range(0,3):
      lista[i]=str(lista[i])
    print(",".join(lista))
    
  else:
    lista=[a,c,b]
    for i in range(0,3):
      lista[i]=str(lista[i])
    print(",".join(lista))
   
elif b<=a and b<=c:
  if c<=a:
    lista=[b,c,a]
    for i in range(0,3):
      lista[i]=str(lista[i])
    print(",".join(lista))

  else:
    lista=[b,a,c]
    for i in range(0,3):
      lista[i]=str(lista[i])
    print(",".join(lista))
    
elif c<=a and c<=b:
  if a<=b:
    lista=[c,a,b]
    for i in range(0,3):
      lista[i]=str(lista[i])
    print(",".join(lista))
  else:
    lista=[c,b,a]
    for i in range(0,3):
      lista[i]=str(lista[i])
    print(",".join(lista))
     

