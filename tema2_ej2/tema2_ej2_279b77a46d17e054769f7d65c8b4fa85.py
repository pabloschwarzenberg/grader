def amigos(a,b):
  contadora = 0
  contadorb = 0
  for divisores in range(1,int(a)):
    if int(a) % divisores == 0:
      contadora += divisores
     
    else:
          contadora += 0
   
  for divisores in range(1,int(b)):
    if int(b) % divisores == 0:
      contadorb += divisores
     
    else:
          contadorb += 0
  if contadora == b and contadorb == a:
      return True
  else:
      return False

def main():
    a = int(input("ingrese numero: "))
    b = int(input("ingrese numero: "))
    amigos(a, b)

if __name__ == "__main__":
    main()