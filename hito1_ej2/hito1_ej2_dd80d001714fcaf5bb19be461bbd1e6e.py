#Contestador de celular
numt = input('Ingrese numero telefonico: ')
hora = int(input('Ingrese hora de la llamada: '))
C = 'CONTESTAR'
NC = 'NO CONTESTAR'

if hora >= 0 and hora <= 7:
    print(C)

elif hora > 7 and hora <= 14:
    if int(numt)%10**3 == 909:
        print(C)
    else:   
        print(NC)

elif hora >= 17 and hora <= 19:
    if int(numt[:3]) == 877:
        print(NC)
    else:
        print(C)    

elif hora > 19: 
    print(NC)

else:
    print(NC)

