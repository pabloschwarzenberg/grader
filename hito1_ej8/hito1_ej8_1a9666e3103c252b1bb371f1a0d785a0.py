#Descomponer un número
seguir = True

while seguir:

    try:

        numero = int(input("Ingrese un número entero: "))

        if numero < 0:

            print("Intente nuevamente")

        else:

            seguir = False

    except:

        print("INVALIDO")

output=" "

largo = len(str(numero))

for X  in range(len(str(numero))):

    if largo != 0:

        if largo == 4:

            output+=str(numero)[X]+'M+'

        elif largo == 3:

            output+=str(numero)[X]+'C+'

        elif largo == 2:

            output+=str(numero)[X]+'D+'

        elif largo == 1:

            output+=str(numero)[X]+'U'

        largo-=1

print('-> ',output)      