def numero_perfecto(a):
    d = 1
    divisores = 0
    perfecto = False
    while d<a:
          if a%d == 0:
             divisores = divisores + d
             
             if divisores == a:
                 perfecto = True
             else:
                 perfecto = False
          d = d + 1
    return perfecto

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           