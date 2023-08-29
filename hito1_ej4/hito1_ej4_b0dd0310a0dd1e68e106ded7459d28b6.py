#Conversión de Decimal a Binario
def binario(numero):
    a=" "
    while numero//2!=0:
        a=str(numero%2)+a
        numero=numero//2
    return str(numero)+a
transformacion=int(input("Introduce un número para convertir: "))
print("resultado=",binario(transformacion))
