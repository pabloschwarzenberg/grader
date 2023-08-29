#Cajero Automático
claveValida=1803
ctaValida="10334151"
saldoCajero=1000000
saldoCta=100000
respuesta="N"
errorclave=1
fuera=True
while (respuesta=="N" or respuesta=="n") and fuera:
  print("Saldo cuenta=",saldoCta)
  print("Saldo cajero=",saldoCajero)
  rafaga=str(input("Ingrese la rafaga:"))
  clave=rafaga[9]+rafaga[10]+rafaga[11]+rafaga[12]
  if int(clave)==claveValida:
      if len(rafaga)==20:
        nroCta=rafaga[0]+rafaga[1]+rafaga[2]+rafaga[3]+rafaga[4]+rafaga[5]+rafaga[6]+rafaga[7]
        monto=rafaga[14]+rafaga[15]+rafaga[16]+rafaga[17]+rafaga[18]+rafaga[19]
        if nroCta==ctaValida:
            if int(monto)<=saldoCta:
                saldoCta-=int(monto)
                saldoCajero-=int(monto)
            else :
              print("Monto no permitido")
        else:
           print("cta invalida ")
      else :
        print("Debe ser de longitud 20 e ingresastes: "+str(len(rafaga) ))
  else :
    print("clave invalida")
    errorclave+=1
  if errorclave > 3 :
         print("tarjeta bloqueada")
         fuera=False
  else :
    respuesta=input("Deseas Seguir procesando operaciones bancarias (Si: Nn / No: Otro digito):")
