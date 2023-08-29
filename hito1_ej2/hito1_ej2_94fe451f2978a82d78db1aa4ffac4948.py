#Contestador de celular
      
num = input('\nIngrese número telefonico (8 cifras): ')
hora = int(input('Ingrese hora de la llamada: '))
l_num = []

for i in num:
    l_num.append(i)

if hora>=0 and hora<=7:
        print('\nContestar.')
elif hora>=17 and hora<=19:
    if l_num[0]=='8' and l_num[1]=='7' and l_num[2]=='7':
        print('\nNo Contestar.')
    else:
        print('\nContestar.')
elif hora>7 and hora<14:
    if l_num[5]=='9' and l_num[6]=='0' and l_num[7]=='9':
        print('\nContestar.')
    else:
        print('\nNo Contestar.')
elif hora>19 and hora<=24:
    print('\nNo Contestar.')
