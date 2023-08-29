#Contestador de celular
def resultado(telefono,h):
    if h > -1 and h < 8:
        return("CONTESTAR")
    elif h > 6 and h < 15:
        if telefono[5:8]=="909":
            return("CONTESTAR")
        else:
            return("NO CONTESTAR")
    elif h > 16 and h < 20:
        if telefono[:3] == "877":
            return("NO CONTESTAR")
        else:
            return("CONTESTAR")
    elif h > 19:
        return("NO CONTESTAR")
    else:
        return("NO CONTESTAR")


telefono=int(input(">>>Ingrese numero telefonico: "))
digitos=len(str(telefono))
telefono = str(telefono)
if digitos == 8:
    h=int(input(">>>Ingrese la hora de llamada: "))
    if h >= 0 and h <= 23:
        print(">>>Resultado:",resultado(telefono,h))