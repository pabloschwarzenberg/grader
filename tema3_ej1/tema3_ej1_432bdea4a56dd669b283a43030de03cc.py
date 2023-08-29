# completa el código de la función

def sumadivisores(a):
  suma=0
  pos_div=1
  while a%pos_div==0:
    if pos_div<a:
      suma=suma+pos_div
      pos_div+=1
      return suma
    elif pos_div>=a:
      break
if __name__ == "__main__":
    b=int(input("Ingrese numero a "))
    if sumadivisores(b)==1:
        print(b,"es numero primo")
