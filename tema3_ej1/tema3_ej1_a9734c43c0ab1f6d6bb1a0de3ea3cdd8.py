def suma_divisores(numero):
    contador=1
    sumatoria=0
    while contador!=numero-1:
        if numero == 1:
            return 0,False      
        if numero%contador==0:
            sumatoria=sumatoria+contador
        contador=contador+1
    if sumatoria==1:
        bm=True
    else:
        bm=False
    return sumatoria,bm
if __name__ == "__main__":
    numero=int(input("ingrese un numero entero: "))
    print("La suma de los divisores es: ", suma_divisores(numero))
    if suma_divisores(numero)==1:
      print (suma_divisores(numero),True)
    else:
      print (suma_divisores(numero),False)
