def numero_perfecto(a):
    div1=a-1
    sumdiv=0
    if a==1:
        sumdiv=0
    if a!=1:
        while div1!=0:
            if a%div1==0:
                divisor=div1
                sumdiv=sumdiv+divisor
            div1=div1-1
    if sumdiv==a:
      return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           