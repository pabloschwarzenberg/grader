#Contestador de celular
numero_telefono=int(input("INGRESE NUMERO DE TELEFONO:"))
x=int(input("HORA DE LLAMADA:"))
lista=list(str(numero_telefono))
#largo= debe tener 8 numeros
inicio=False
final=False
if int(lista[5])==9 and int(lista[6])==0 and int(lista[7])==9:
    final=True
if int(lista[0])==8 and int(lista[1])==7 and int(lista[2])==7:
    inicio=True
if 0<x<7:
    print("CONTESTAR")
elif 7<x<14 and final:
    print("CONTESTAR")
elif 17<x<19 and inicio==False:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")