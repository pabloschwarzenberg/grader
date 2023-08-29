cajero = 1000000
persona = 100000
usuario = int(input())
clave = int(input())
salir = "N"

while salir == "N":
  count = 0
  if usuario == 10334151:
    if clave == 1803:
      monto = int(input())
      while monto > persona:
        print("monto no permitido")
        monto = int(input())        
      cajero -= monto
      persona -= monto
      cajero_str = str(cajero)
      persona_str = str(persona)
      print("saldo cuenta="+persona_str)
      print("saldo cajero="+cajero_str)
    elif clave != 1803:
      count +=1
      print("clave invalida")
    if count == 3:
      print("tajeta bloqueada")
      break
  else:
    print("usuario invalido")
  
      
      
      
