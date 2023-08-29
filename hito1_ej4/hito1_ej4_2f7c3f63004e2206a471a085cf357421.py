#Conversión de Decimal a Binario

num = float(input("Ingrese un numero: "))



cantidadcerounos = "binario ="
resto = num

cero = "0"
uno = "1"

while num//2 > 0:
    if num%2 == 0:
        cantidadcerounos += cero
        num = num//2
        resto = resto//2
        
    if num%2 == 1:
        cantidadcerounos += uno
        num = num//2
        resto = resto//2
        if resto == 1:
            cantidadcerounos += uno

cantidadcerounos = cantidadcerounos[9::1]
cantidadcerounos = cantidadcerounos[-1::-1]

print("resultado =",cantidadcerounos)
                      