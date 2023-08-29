#Factores Primos
numero=int(input("Ingrese un numero entero:"))
lista=[]
for i in range(2,numero+1):
    while numero%i==0:
        lista.append(i)
        numero=numero/i
           
for e in lista:
    print(e)
          