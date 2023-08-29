#Contestador de celular
 
 #!/usr/bin/python3
numero_telefono = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))
num = str(numero_telefono)
if 0 <= hora_llamada <= 7:
    print('CONTESTAR')
elif hora_llamada<14 or num[:3]=='909':
    print ('CONTESTAR')
elif 17 < hora_llamada < 19 or num[3:]=='877':
    print ('NO CONTESTAR')
elif hora_llamada > 19:
    print ('NO CONTESTAR')
