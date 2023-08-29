#Contestador de celular
numero=int(input("numero telefonico: "))
hora=int(input("hora de la llamada: "))
termina=numero%1000
if 0<hora<7:
    print("CONTESTAR")
if hora>=14 or termina==909:
    print("CONTESTAR")
if 17<hora<19 and 87699999<=numero<=87800000:
    print("NO CONTESTAR")
if hora>19:
    print("NO CONTESTAR")
  