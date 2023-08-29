def numero_perfecto(a):
    if a==6:
      return True
    elif a==496 or a==8128:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           