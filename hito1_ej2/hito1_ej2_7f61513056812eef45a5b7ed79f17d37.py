#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
hora= int(input("Ingrese hora de la llamada: "))
if  0<= hora <= 7 :
    print("CONTESTAR")
if hora < 14 or  numero%1000 == 909 :
    print( "CONTESTAR")
if 17< hora < 19 and 87699999 <= numero <=87800000 :
    print(" NO CONTESTAR")
if hora>19 :
    print("NO CONTESTAR")