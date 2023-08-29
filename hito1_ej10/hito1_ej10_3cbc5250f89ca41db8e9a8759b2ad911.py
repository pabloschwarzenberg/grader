#Cajero Automático
# rafaga es : año-mes-dia-cta-operacion-monto

#          xxxx-xx-xx-xxxx-x-xxxxxx
#          Operación: 1- Deposito 2- Retiro
#          20210421103341511100000 deposito
#          2021042110334151245000 retiro
#          202104211000000245000

claveValida="1803"
ctaValida="10334151"
saldoCuenta=100000
saldoCajero=1000000
respuesta="S"
errorclave=1
fuera=True
while (respuesta=="S" or respuesta=="s") and fuera:
  print("Saldocuenta:",saldoCuenta)
  if (respuesta=="S" or respuesta=="s") and fuera:
   print("Saldocajero:",saldoCajero)
   clave=input("Introduza clave:")
  if clave==claveValida :
      rafaga=int(input("Ingrese la rafaga:"))
      numStr=str(rafaga)
      if len(numStr)==22 :
        mes=numStr[4]+numStr[5] 
        dia=numStr[6]+numStr[7]
        año=numStr[0]+numStr[1]+numStr[2]+numStr[3] 
        operacion=numStr[16] 
        nroCta=numStr[8]+numStr[9]+numStr[10]+numStr[11]+numStr[12]+numStr[13]+numStr[14]+numStr[15]
        monto=numStr[17]+numStr[18]+numStr[19]+numStr[20]+numStr[21]
        print("fecha:",año+mes+dia)
        print("cta:",nroCta)
        print("operación:",operacion)
        print("monto",monto)
        if nroCta==ctaValida :
          if operacion=="1":
            saldoCuenta+=int(monto)

          else :

             if int(monto) <= saldoCuenta:
               saldoCuenta-=int(monto)
               
        if nroCta==ctaValida :
          if operacion=="1":
            saldoCajero-=int(monto)

          else :

            if int(monto) <= saldoCajero:
               saldoCajero-=int(monto)

            else :
              print("No tiene suficiente dinero para retirar el monto ")

        else:
           print("cta invalida ")

      else :
        print("Debe ser de longitud 22 y solo ingresastes "+str(len(numStr) ))

  else :
    print("clave invalida")
    errorclave+=1
  if errorclave > 3 :
          print("tarjeta bloqueada")
          fuera=False

  else :
    respuesta=input("Deseas Seguir procesando operaciones bancarias (S/N):")
