#Ordenar tres números

a=int(input("Ingrese el primer número :"))
b=int(input("Ingrese el segundo número :"))
c=int(input("Ingrese el tercer número :"))


if a>b and a>c:
  mayor = a 
  if a>b:
             segundo=b
             tercer=c
  else:
             segundo=c
             tercer=b
if b>a and b>c:
  mayor = b
  if a>c:
             segundo=a
             tercer=c
  else:
             segundo=c
             tercer=a
                    
if c>a and c>b:
  mayor = c 
  if a>b:
             segundo=a
             tercer=b
  else:
             segundo=b
             tercer=a             
print(tercer,",",segundo,",",mayor)
    
    
    