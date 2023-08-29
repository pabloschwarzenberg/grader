#Contestador de celular
# Contestador de telefono automatico
checker = False
# Mientras no es Falso, pregunta por telefono
while not(checker):
    numero_telefonico = input('Introduza numero de telefono: ')
    # si el numero es igual a 8, salir del bucle cambando checker a True
    if len(numero_telefonico) == 8:
        
        checker=True
    #Si el numero no tiene 8 digits, seguir preguntando hasta que los tenga
    else:
        print('ERROR: Introduzca un numero de 8 digitos')
        print('')
        continue
        

# preguntar por hora de la llamada
hora_llamada = int(input('Hora de la llamada (formato 24H): '))
# Variable para los ultimos tres digitos del numero
ultimos_tres_digitos = numero_telefonico[-3:]
primeros_tres_digitos = numero_telefonico[0:3]

def resolucion(numero_telefonico,hora_llamada):
    if hora_llamada >= 0 and hora_llamada <= 7:
        print('RESULTADO: CONTESTAR')
    elif hora_llamada < 14 and ultimos_tres_digitos == '909':
        print('RESULTADO: CONTESTAR')
        
    elif((hora_llamada>17 and hora_llamada<19) and (primeros_tres_digitos != '877')):
        print('RESULTADO: CONTESTAR')
        
    elif hora_llamada >19:
        print('RESULTADO: NO CONTESTAR')
    else:
        print('RESULTADO: NO CONTESTAR')
        
resolucion(numero_telefonico,hora_llamada)
        