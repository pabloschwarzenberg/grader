unidades = "MCDU"
numero = input("Ingrese numero a descomponer: ")
x = 0
resultado = ""
unidades = unidades[-len(numero):]
while x < len(numero):
    resultado =  resultado + numero[x]+unidades[x] + "+"
    x = x + 1
print(resultado[0:-1])