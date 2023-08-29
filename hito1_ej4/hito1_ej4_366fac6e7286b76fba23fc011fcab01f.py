numero=float(input('Ingrese su numero a convertir: '))
lista= []
while (numero>0):
    a= int(numero%2)
    print(a)
    lista.append(a)
    numero=(numero-a)/2
lista.append(0)
string=""
for j in lista[:-1:]:
    string=string+str(j)
    binario = string[::-1]
print("Resultado=",binario)