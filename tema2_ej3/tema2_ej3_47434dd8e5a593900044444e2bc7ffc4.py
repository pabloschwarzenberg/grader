def numero_perfecto(a):
    da=0
    for divisor in range(1,a):
          if a%divisor==0:
             da=da+divisor
    if da==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           