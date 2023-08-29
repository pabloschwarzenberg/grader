#Conversión de Decimal a Binario
num=int(input("ingrese numero decimal")) 

modulos = [] # la lista para guardar los módulos

while num != 0: 
    modulo = num % 2
    cociente = num // 2
    modulos.append(modulo) 
    num = cociente 

print(modulos)