#Contestador de celular
N_telefonico=int(input('Ingrese numero telefonico: '))
H=int(input('Ingrese hora de llamada: '))
contador=0
numero=[]
while (N_telefonico)<=10000000 or (N_telefonico)>=99999999:
    N_telefonico=int(input('Ingrese un numero valido:'))
for i in str(N_telefonico):
    numero.append(i)
if (N_telefonico)>=10000000 and (N_telefonico)<=99999999 and 0<=H and H<=23 :
    if 0<=H<=7:
        print('Contestar')
    elif H<14:
        for i in reversed(numero):
            if i == '9':
                contador = contador + 1
            if i == '0':
                contador = contador + 1
            if contador==3:
                print('Contestar')
                break
        if contador!=3:
            print('No contestar')
    elif 17<=H<=19:
        contador=0
        for i in (numero):
            if i == '8':
                contador = contador + 1
            if i == '7':
                contador = contador + 1
            if contador==3:
                print('No contestar')
                break
        if contador!=3:
            print('Contestar')
    elif H>=19:
        print('No contestar')
        
            
print('Fin del programa')
     