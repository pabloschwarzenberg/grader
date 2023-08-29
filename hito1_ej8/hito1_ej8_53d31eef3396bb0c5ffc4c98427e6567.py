#Descomponer un número
numero = eval(input("ingrese numero de 4 digitos: "))
unidades = numero%10
numero = numero//10
decenas = numero%10
numero = numero//10
centenas = numero%10
numero = numero//10
unidad_mil = numero%10

print(unidad_mil,"M +",centenas,"C +",decenas,"D +",unidades,"U")

# por favor escribe aquí tu función
def es_primo(numero):
    cont=2
    div=0
    if numero>2:
     while cont!=numero:
        if numero%cont==0:
            div+=1
        cont+=1
    if numero==1:
        return False
    elif div==0:
        return True
    else:
        return False