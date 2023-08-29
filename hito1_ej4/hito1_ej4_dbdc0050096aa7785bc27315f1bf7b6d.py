#Conversión de Decimal a Binario
numero = int(input('Ingrese numero: '))

base = numero
lista = []
residuo = 0
while base != 0:
    residuo = base%2
    base = base//2
    a = str(residuo)
    lista.append(a)
lista.reverse()
resultado = ''.join(lista)
print('resultado=',eval(resultado))