#Contestador de celular
nume_celu=int(input("Ingrese numero telefonico: "))
hora_llam=int(input("Ingrese hora de la llamada: "))

cadena = str(nume_celu)

if hora_llam <= 7:
    print("Resultado: CONTESTAR")
elif hora_llam < 14:
  if cadena[-3:] == '909':
    print("Resultado: CONTESTAR" )
  else:
    print("Resultado: NO CONTESTAR" )
elif hora_llam == 15 or hora_llam == 16:
    print("Resultado: NO CONTESTAR" )
elif hora_llam >= 17 and hora_llam <= 19:
  if cadena[:3] == '909':
    print("Resultado: CONTESTAR" )
  else:
    print("Resultado: NO CONTESTAR" )
elif hora_llam > 19:
    print("Resultado: NO CONTESTAR" )
