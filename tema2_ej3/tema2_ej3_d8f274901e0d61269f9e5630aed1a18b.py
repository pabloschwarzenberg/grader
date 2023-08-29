def numero_perfecto(a):
    dividir = [1]
    #for
    for i in range(2, a + 1):
        if a %i == 0:
            #appened
            dividir.append(i)
    #Change >:)
    x= sum(dividir)
    #True
    if x-a == a:
        return True
    #False
    if x-a != a:
        return False
    
if __name__=="__main__":
  #Resultado
  x = int(input("Ingrese un numero: "))
  resultado = numero_perfecto(x)
  print(resultado)
           