#Ordenar tres números
      
ingresar_n= int(input("Por favor ingresar n: "))
ingresar_n1= int(input("Por favor ingresar n: "))
ingresar_n2= int(input("Por favor ingresar n: "))
      
if((ingresar_n <= ingresar_n1)) and ((ingresar_n <= ingresar_n2)):
    primero = ingresar_n
    if(ingresar_n1 <= ingresar_n2):
        segundo= ingresar_n1
        tercero= ingresar_n2
    else:
        segundo= ingresar_n2
        tercero= ingresar_n1
elif((ingresar_n1 <= ingresar_n)) and ((ingresar_n1 <= ingresar_n2)):      
    primero = ingresar_n1
    if(ingresar_n1 <= ingresar_n2):
        segundo= ingresar_n
        tercero= ingresar_n2
    else:
        segundo= ingresar_n2
        tercero= ingresar_n
else:
    primero = ingresar_n2
    if(ingresar_n <= ingresar_n1):
        segundo= ingresar_n
        tercero= ingresar_n1
    else:
        segundo= ingresar_n1
        tercero= ingresar_n
print(primero,",", segundo,",",tercero)