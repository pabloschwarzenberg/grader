#Descomponer un número
seguir = True
while seguir:
    try:
        n = int(input('Ingrese número entero: '))
        if n < 0:
            print('Error, intente nuevamente.')
        else:
            seguir = False
    except:
        print('Valor inválido.')
output=''
largo = len(str(n))
for i  in range(len(str(n))):
    if largo != 0:
        if largo == 4:
            output+=str(n)[i]+'M+'
        elif largo == 3:
            output+=str(n)[i]+'C+'
        elif largo == 2:
            output+=str(n)[i]+'D+'
        elif largo == 1:
            output+=str(n)[i]+'U'
        largo-=1
print('-> ',output)      