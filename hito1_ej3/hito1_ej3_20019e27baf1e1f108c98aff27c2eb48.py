#Aprobación de créditos
ingreso=int(input("indique su ingreso mensual: "))
ano_naci=int(input("ingrese su año de nacimiento: "))
n_hijo=int(input("ingrese la cantidad de hijos: "))
ano_banco=int(input("¿cuando años lleva en esta banco?: "))
es_civil=str(input("indique su estado civil: S para Soltero y C para casado: "))

if es_civil=="C":
    es_civil=1
else:
    es_civil=2

lugar=str(input("indique lugar de alogamiento: U para Urbano y R para Rural: "))

if lugar=="U":
    lugar=1
else:
    lugar=0


edad=(2020-ano_naci)

if(ano_banco>10 and n_hijo>=2):
  print("APROBADO")
else:
  if(es_civil==1 and n_hijo>3 and edad>=45 or edad>=55):
      print("APROBADO")
  else:
      if(ingreso>2500000 and es_civil==1 and lugar==1):
          print("APROBADO")
      else:
          if(ingreso>3500000 and ano_banco>5):
              print("APROBADO")
          else:
              if(lugar==0 and es_civil==1 and n_hijo<3):
                    print("APROBADO")
              else:
                  print("RECHAZADO")