#Contestador de celular
numero_telefono= int(input("Ingrese numero telefonico: "))
horas= int(input("Ingrese hora de la llamada: "))

def contestadora(numero,horas):

    if horas <0 and horas >23:
        return print ("horas mal ingresadas")
    if len (str (numero)) !=8:
        return print ("numero de telefono mal ingresado")

    if horas >=0 and horas <=7:
        return print ("resultado: CONTESTAR")
    elif horas <14:
        if str (numero) [5:8] == "909":
            return print ("resultado: CONTESTAR")
        else: ("resultado: NO CONTESTAR")

    elif horas >=17 and horas <=19:
        if str(numero)[0:3] == "877":
            return print("resultado: NO CONTESTAR")
        else: ("resultado: CONTESTAR")

    elif horas >19 and horas <=23:
        return print ("resultado: NO CONTESTAR")

contestadora(numero_telefono,horas)