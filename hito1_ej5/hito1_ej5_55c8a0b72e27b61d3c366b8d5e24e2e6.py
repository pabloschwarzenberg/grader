#entrada:ingrese un numero.
#salida:mostrar el digito verificador.
#el numero es:
numero=int(input("el numero es: "))
while not(numero>1000000 and numero<99999999):
    numero=int(input("error, el numero debe ser mayor a 1000000 y menor a 99999999: "))
#calcular el digito verificador
numero_invertido=str(numero)[::-1]
num1=int(numero_invertido[0])*2
num2=int(numero_invertido[1])*3
num3=int(numero_invertido[2])*4
num4=int(numero_invertido[3])*5
num5=int(numero_invertido[4])*6
num6=int(numero_invertido[5])*7
num7=int(numero_invertido[6])*2
if((len(str(numero)))==8):
    num8=int(numero_invertido[7])*3
else:
    num8=0
suma_de_numeros=num1+num2+num3+num4+num5+num6+num7+num8
resto=suma_de_numeros%11
digito_verificador=11-resto
#mostrar resultado
print("dv=", digito_verificador)
if(digito_verificador==11):
    digito_verificador=0
    print("dv=",digito_verificador)
elif(digito_verificador==10):
    digito_verificador="K"
    print("dv=",digito_verificador)

