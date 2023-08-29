#Entrada del programa
string=str(input())
#El programa nos distingue entre mayuscula y minuscula
string=string.upper()
if string.find('A') and string.find('C') and string.find('T') and string.find('G'):
    print('Secuencia correcta')
else:
    print('Secuencia incorrecta')