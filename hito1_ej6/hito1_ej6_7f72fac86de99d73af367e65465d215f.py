#Ordenar tres números
primero=int(input("ingrese el primer numero: "))
segundo=int(input("ingrese el segundo numero: "))
tercero=int(input("ingrese el tercer numero: "))
if primero < (segundo or tercero) and (segundo<=tercero):
  print(primero,",",segundo,",",tercero)
elif segundo < (primero or tercero) and (primero<=tercero):
  print(segundo,",",primero,",",tercero)     
elif tercero < (primero or segundo) and (primero<=segundo):
  print(tercero,",",primero,",",segundo)
elif primero < (segundo or tercero) and (tercero<=segundo):
  print(primero,",",tercero,",",segundo)
elif segundo < (primero or tercero) and (tercero<=primero):
  print(segundo,",",tercero,",",primero)
elif tercero < (segundo or primero) and (segundo<=primero):
  print (tercero,",",segundo,",",primero)
else:
    print(primero,",",segundo,",",tercero)
