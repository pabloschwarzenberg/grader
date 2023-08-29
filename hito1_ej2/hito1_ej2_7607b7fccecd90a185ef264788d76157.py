#Contestador de celular
N_T = int(input("ingrese numero telefonico: "))
H_D_LL = int(input("ingrese hora de la llamada: "))
while True:
  if N_T>=0 and H_D_LL<=7:
      print("CONTESTAR")
      break
  if H_D_LL<14:
      if N_T%1000==909:
        print("CONTESTAR")
        break
  if H_D_LL>=17 and H_D_LL<=19:
      if N_T//1000 == 877:
        print("CONTESTAR")
        break
  if H_D_LL>19:
    print("NO CONTESTAR")
    break
  else:
    print("NO CONTESTAR")
    break