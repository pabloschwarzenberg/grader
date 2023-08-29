#Factores Primos
divisor_candidato=2
lista=[]
numero=int(input("Ingrese el numero entero del cual quiere obtener los divisores"))
while divisor_candidato<=numero:
    if numero%divisor_candidato==0:
        lista.append(divisor_candidato)
    divisor_candidato+=1
print(lista)    