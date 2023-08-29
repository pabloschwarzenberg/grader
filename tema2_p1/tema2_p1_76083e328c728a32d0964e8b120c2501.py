# por favor escribe aquí tu función
 
def es_primo(numero):
  listaprimo = [i for i in range(1,numero+1) if numero%i==0]
  
  if len(listaprimo)==2 :
    return True
 
  else:
    return False
if __name__ == "__main__":
  numero = eval(input("ingrese un numero"))
  print(es_primo(numero))
           