# por favor escribe aquí tu función
def es_primo(num):
  lstdivnum=[i for i in range(1,num+1) if num %i==0]
  if len(lstdivnum)==2:
    return True
  else:
    return False 

if __name__ == "__main__":
  num=int(input("numero: "))
  print (es_primo(num))