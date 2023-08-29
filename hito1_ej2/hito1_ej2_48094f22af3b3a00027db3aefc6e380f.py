#Contestador de celular
#Entrada de Datos
H_llamada = int(input("¿Que hora es ?, valor entre 0 a 23: "))
N_telefono = int(input("Introducir numero del celular de 8 digitos: "))
tres_ultimos_N= N_telefono%(10**3)

#Proceso - Salida de datos
if H_llamada > 19:
    print("NO CONTESTAR")
elif 0 <= H_llamada <= 7:
    print("CONTESTAR")
elif 7<= H_llamada <= 14 and tres_ultimos_N == 909:
    print("CONTESTAR")
elif 7<= H_llamada <= 14:
    print("NO CONTESTAR")
elif 17 <= H_llamada <= 19 and tres_ultimos_N ==877:
    print("NO CONTESTAR")
else:
    print("CONTESTAR")