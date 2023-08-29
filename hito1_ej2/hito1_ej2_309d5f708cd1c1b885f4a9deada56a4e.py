#Contestador de celular
numT=eval(input("Ingrese su numero telefonico:"))
hora=eval(input("Ingrese hora de llamada:"))
if numT>9999999 and numT<99999999:
    excepcion = numT % 1000
    aux = numT // 1000
    aux = aux // 100
    if (hora>=0 and hora<=7):
        print("CONTESTAR")
    if (hora<=14 and hora>=8):
        print("CONTESTAR")
    else:
        excepcion==909
        print("CONTESTAR")
    if (hora<=19 and hora>17):
        print("CONTESTAR")
    if aux==877:
        print("NO CONTESTAR")
    if hora>19:
        print("NO CONTESTAR") 