#Aprobación de créditos
while(1):
  ing=int(input("cuanto gana?"))
  nac=int(input("cuando nacio?"))
  hij=int(input("cuantos hijos tiene?"))
  bco=int(input("cuanto lleva en el banco?"))

  ecivil=input("estado civil? (s/c)")
  lugar=input("urbano o rural (u/r)")
  
  edad=2023-nac

  if(bco>=10 and hij>=2):
    print("aprueba")
  
  if(ecivil=="c" and hij>=3 and edad>45 and edad<55):
    print("aprueba")
  
  if(ing>2500000 and ecivil=="s" and lugar=="u"):
    print("aprueba")
  
  if(ing>3500000 and bco>5):
    print("aprueba")
  
  if(lugar=="u" and ecivil=="c" and hij<2):
    print("aprueba")
