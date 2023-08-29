#Contestador de celular
num= str(input("ingrese el numero telefonico"))
hora= int(input("ingrese la hora"))

A= num[5:9]
B= num[0:3]
int(A)
int(B)

if (0<= hora) and (hora <=19):
  if (0<= hora) and (hora <=7):
   print("resultado: contestar")
  elif (7 <= hora) and (14 >= hora):
    if (A == "909"):
      print("resultado: contestar")
    else:
       print("resultado: no contestar")

  elif (17 <= hora) and (19 >= hora):
    if (B == "877"):
        print("resultado:  no contestar")
    else:
        print("resultado: contestar")

else:
    print("resultado: no contestar")