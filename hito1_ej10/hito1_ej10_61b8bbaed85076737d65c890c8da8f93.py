#Cajero Automático
 # rafaga es : año-mes-dia-cta-operacion-monto

#          xxxx-xx-xx-xxxx-x-xxxxxx

#          Operación: 1- Deposito 2- Retiro

#          1000000 deposito

#          45000 retiro

#          2021042156542100000


claveValida="1803"

ctaValida="7867"

saldoCta=55000

respuesta="S"

errorclave=1

fuera=True

while (respuesta=="S" or respuesta=="s") and fuera:

  print("Saldo:",saldoCta)

  clave=input("Introduza clave:")

  if clave==claveValida :

      rafaga=int(input("Ingrese la rafaga:"))

      numStr=str(rafaga)

      if len(numStr)==19 :

        año=numStr[0]+numStr[1]+numStr[2]+numStr[3] 

        dia=numStr[6]+numStr[7]

        mes=numStr[4]+numStr[5] 

        operacion=numStr[12] 

        nroCta=numStr[8]+numStr[9]+numStr[10]+numStr[11]

        monto=numStr[13]+numStr[14]+numStr[15]+numStr[16]+numStr[17]+numStr[18]

        print("fecha:",año+mes+dia)

        print("cta:",nroCta)

        print("operación:",operacion)

        print("monto",monto)

        if nroCta==ctaValida :

          if operacion=="1":

            saldoCta+=int(monto)

          else :

            if int(monto) <= saldoCta:

               saldoCta-=int(monto)

            else :

              print("No tiene suficiente dinero para retirar el monto ")

        else:

           print("cta invalida ")

      else :

        print("Debe ser de longitud 19 y solo ingresastes "+str(len(numStr) ))

  else :

    print("clave invalida")

    errorclave+=1

  if errorclave > 3 :

         print("tarjeta bloqueada")

         fuera=False

  else :

    respuesta=input("Deseas Seguir procesando operaciones bancarias (S/N):")   