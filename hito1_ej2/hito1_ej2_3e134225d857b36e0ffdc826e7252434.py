#Contestador de celular
numero_celular=int(input("Ingrese numero de celular: "))
hora_llamada=int(input("Ingresar hora de llamada: "))
separar_numeros = [int(a) for a in str(numero_celular)]
ultimos_3_numeros=separar_numeros[5:8]
ultimos_numeros_909=[9,0,9]
primeros_3_numeros=separar_numeros[0:3]
primeros_numeros_877=[8,7,7]

if hora_llamada >=0 and hora_llamada<=7:
    print("CONTESTAR")
elif hora_llamada<14 and ultimos_3_numeros!=ultimos_numeros_909:
    print("NO CONTESTAR")
elif hora_llamada<14 and ultimos_3_numeros==ultimos_numeros_909:
    print("CONTESTAR")
elif hora_llamada>=17 and hora_llamada<=19 and primeros_3_numeros!=primeros_numeros_877:
    print("CONTESTAR")
elif hora_llamada>=17 and hora_llamada<=19 and primeros_3_numeros==primeros_numeros_877:
    print("NO CONTESTAR")
elif hora_llamada>19:
    print("NO CONTESTAR")      