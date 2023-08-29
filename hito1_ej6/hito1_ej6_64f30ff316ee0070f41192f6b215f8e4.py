#Ordena e Impreme Ordenado tres nuemero
numero1=eval(input("Ingresa Numero: "))
numero2=eval(input("Ingresa Numero: "))
numero3=eval(input("Ingresa Numero: "))

Menor=min(numero1,numero2,numero3)
Mayor=max(numero1,numero2,numero3)
Medio=(numero1+numero2+numero3)-Menor-Mayor
print (Menor,",",Medio,",",Mayor)
      