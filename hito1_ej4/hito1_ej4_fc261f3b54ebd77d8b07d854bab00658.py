
a = input("ingrese numero: ") 
numero_decimal = int(a)
modulos = [] 
bin=""
cont = 0
while numero_decimal != 0: 

    modulo = numero_decimal % 2
    cociente = numero_decimal // 2
    modulos.append(modulo) 
    numero_decimal = cociente 
    cont=cont+1
while cont != 0:
  bin=bin+str(modulos[cont-1])
  cont=cont-1
res = "resultado=" + bin
str.strip(res)
print(res)