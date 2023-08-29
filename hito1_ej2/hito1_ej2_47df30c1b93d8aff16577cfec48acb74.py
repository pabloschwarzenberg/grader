#Contestador de celular
numero = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese la hora de la llamada: "))
numero_str = str(numero)

if 0<=hora<=7:
    print("contestar")
elif 7<=hora<=14:
    if numero_str[5:8] == "909":
      print("contestar")
    else:
        print("no contestar")
elif 14<=hora<17:    
     print("no contestar")
elif 17<=hora<=19:
    if numero_str[0:3]=="877":
        print("no contestar")
    else:
        print("contestar")
elif hora>19:
  print("no contestar")

