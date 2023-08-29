def numero_perfecto(a):
    suma = 0
    for x in range(1,a):
      if (a%(x)==0):
        suma+=(x)
    if a==suma:
      return True
    else: 
      return False

if __name__=="__main__":
    #a=int(input("Ingrese a: "))
    a=1
    print(numero_perfecto(a))
