#Contestador de celular
n_telefono=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de llamada: "))
if 0<hora<7:
    print("Resultado CONTESTAR")
if 7<=hora<14:
    if n_telefono%1000==909:
     print("ResultadoCONTESTAR")
    else:
     print("Resultado NO CONTESTAR")
if 14<=hora<=17:
 print("Resultado CONTESTAR")
if 17<hora<19:
    if 87700000<=n_telefono<=87799999:
     print("Resultado NO CONTESTAR")
    else:
     print("Resultado CONTESTAR")
if hora>19:
     print("Resultado NO CONTESTAR")
    