#Contestador de celular
#Entradas
cel = int(input("ingrese numero celular: "))
hora = int(input("ingrese la hora de la llamada: "))
cel_str = str(cel)
tres_f = cel_str[5], cel_str[6], cel_str[7]
tres_i = cel_str[0], cel_str[1], cel_str[2]

#procesamiento
if len(str(cel)) == 8:
    if hora <= 7:
        print("Resultado: Contestar")
    elif hora <= 14 and (('9','0','9') == tres_f):
        print("Resultado: Contestar")
    elif hora <= 14:
        print ("Resultado: No Contestar")
    elif hora > 14 and hora < 17:
        print ("Resultado: No Contestar")
    elif (hora >= 17 and hora <= 19) and (('8','7','7') != tres_i):
        print ("Resultado: Contestar")
    elif (hora >= 17 and hora <= 19) and (('8','7','7') == tres_i):
        print ("Resultado: No Contestar")
    elif hora > 19:
        print ("Resultado: No Contestar")