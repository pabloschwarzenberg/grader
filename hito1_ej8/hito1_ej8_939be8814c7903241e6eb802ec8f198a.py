#Descomponer un número
seguir = True
while seguir:
    try:
        n1 = int(input('Ingrese número entero: '))
        if n1 < 0:
            print('Error, intente nuevamente.')
        else:
            seguir = False
    except:
        print('Valor inválido.')
output=''
lengh = len(str(n1))
for i  in range(len(str(n1))):
    if lengh != 0:
        if lengh == 4:
            output+=str(n1)[i]+'M+'
        elif lengh == 3:
            output+=str(n1)[i]+'C+'
        elif lengh == 2:
            output+=str(n1)[i]+'D+'
        elif lengh == 1:
            output+=str(n1)[i]+'U'
        lengh-=1
print('-> ',output)
      