# por favor escribe aquí tu función
def es_primo(numero):
    if numero==1:
        return False
    elif numero>1:
        for x in range(2, numero):
            rest=numero%x
            if rest==0:
                return False                           
            else:
                return True

try:
  numero=int(input("Ingrese Numero:"))
  print(es_primo(numero))
except:
  print("Ingrese un numero")
           