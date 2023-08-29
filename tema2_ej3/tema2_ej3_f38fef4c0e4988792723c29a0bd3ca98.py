def numero_perfecto(a):
    d=1
    suma=0
    while a>d:
        if a%d==0:
            suma=suma+d
        d=d+1
    if suma==a:
        return True
    else:
        return False

if __name__=="__main__":
    opciones=0
    while opciones!=-1:
          opciones=int(input("Si desea saber; si su número es perfecto, ingrese 1; la suma de los númerps perfectos anteriores a su número, ingrese 2: "))
          if opciones==1:
             a=int(input("Ingrese un número natural: "))
             np=numero_perfecto(a)
             if np is True:
               print("Sí es perfecto")
             else:
                 print("No es perfecto")
          elif opciones==2:
               n=int(input("Ingrese un número natural: "))
               f=1
               sum_np=0
               sum_npl=[]
               while f<n:
                     np_f=numero_perfecto(f)
                     if np_f is True:
                        sum_np=sum_np+f
                        sum_npl.append(f)
                        f=f+1
                     else:
                         f=f+1
               print("Números perfectos anteriores a",n,": ", sum_npl)
               print("Suma de esos números: ",sum_np)
           