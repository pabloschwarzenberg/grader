#Ordenar tres números
numero1=int(input("Ingresa un número "))
numero2=int(input("Ingresa un número "))
numero3=int(input("Ingresa un número "))
suma=numero1+numero2+numero3
máximo=max(numero1,numero2,numero3)
mínimo=min(numero1,numero2,numero3)
medio=suma-máximo-mínimo
print(str(mínimo) +"," +str(medio) +"," +str(máximo))




      