#Cálculo del dígito verificador de un rut
numero=input("ingrese su RUT: ")
largo=len(numero)
i=0

if largo==6:
  digito1=int(numero[0])
  digito2=int(numero[1])
  digito3=int(numero[2])
  digito4=int(numero[3])
  digito5=int(numero[4])
  digito6=int(numero[5])

  suma2=(digito6*2)+(digito5*3)+(digito4*4)+(digito3*5)+(digito2*6)+(digito1*7)
  parte_entera=suma2//11
  resultado=suma2-(parte_entera*11)
  resto=int(11-resultado)

  l = [0,1,2,3,4,5,6,7,8,9,"k",0]
  print("dv=",l[resto])

elif largo==7:
  digito1=int(numero[0])
  digito2=int(numero[1])
  digito3=int(numero[2])
  digito4=int(numero[3])
  digito5=int(numero[4])
  digito6=int(numero[5])
  digito7=int(numero[6])

  suma1=(digito7*2)+(digito6*3)+(digito5*4)+(digito4*5)+(digito3*6)+(digito2*7)+(digito1*2)
  parte_entera=suma1//11
  resultado=suma1-(parte_entera*11)
  resto=int(11-resultado)

  l = [0,1,2,3,4,5,6,7,8,9,"k",0]
  print("dv=",l[resto])

elif largo==8:
    digito1=int(numero[0])
    digito2=int(numero[1])
    digito3=int(numero[2])
    digito4=int(numero[3])
    digito5=int(numero[4])
    digito6=int(numero[5])
    digito7=int(numero[6])
    digito8=int(numero[7])

    suma=(digito8*2)+(digito7*3)+(digito6*4)+(digito5*5)+(digito4*6)+(digito3*7)+(digito2*2)+(digito1*3)
    parte_entera=suma//11
    resultado=suma-(parte_entera*11)
    resto=int(11-resultado)
    l = [0,1,2,3,4,5,6,7,8,9,"k",0]
    print("dv=",l[resto])

