def obtenerDV(rutSinDv):
  cadena=reversed(str(rutSinDv))
  aux=2
  suma=0
  for digitos in cadena:
    resultado=int(digitos)*aux
    suma+=resultado
    if aux==7:
      aux=2
    else:
      aux+=1
  print(suma)
  parteEntera=(suma//11)
  resto=suma-(11*parteEntera)
  dv=11-resto
  if dv==11:
    dv=0
  if dv==10:
    dv="k"
  return dv
rutSinDv=int(input())
dv=obtenerDV(rutSinDv)
print("dv=",end="")
print(dv)
