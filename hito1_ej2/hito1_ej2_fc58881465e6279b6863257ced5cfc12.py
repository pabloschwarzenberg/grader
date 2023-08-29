#Contestador de celular
nt = input("Ingrese numero telefonico: ")
h = input("Ingrese la hora: ")

if h >= "20":
  print("No contestar")
elif h >= "17" or h <= "19" and nt[5:20] == "877":
  print("No contestar")
elif h >= "17" or h <= "19":
    print("Contestar")
elif h <= "14" and nt[5:120] == "909":
    print("Contestar")
elif h >= "0" or h <= "7":
    print("Contestar")
