numero_decimal = int(input("ingrese numero: "))

listas = [] 

while numero_decimal != 0:
  
    lista = numero_decimal % 2
    cociente = numero_decimal // 2
    listas.append(lista) 
    numero_decimal = cociente 

listas.reverse()
print(listas)