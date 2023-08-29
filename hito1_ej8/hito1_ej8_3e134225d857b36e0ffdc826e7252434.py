#Descomponer un número
num=int(input("Ingresar un número de hasta 4 dígitos: "))
separar_numeros = [int(a) for a in str(num)]
cantidad_digitos=len(separar_numeros)

if cantidad_digitos==4:

    digito_1=separar_numeros[0]
    digito_2=separar_numeros[1]
    digito_3=separar_numeros[2]
    digito_4=separar_numeros[3]
    print(str (digito_1), "M + " + str(digito_2),"C + " + str(digito_3), "D + " + str(digito_4),"U")

if cantidad_digitos==3:

    digito_1=separar_numeros[0]
    digito_2=separar_numeros[1]
    digito_3=separar_numeros[2]
    print(str(digito_1),"C + " + str(digito_2), "D + " + str(digito_3),"U")

if cantidad_digitos==2:

    digito_1=separar_numeros[0]
    digito_2=separar_numeros[1]
    print(str(digito_1), "D + " + str(digito_2),"U")
    
if cantidad_digitos==1:

    digito_1=separar_numeros[0]
    print(str(digito_4),"U")