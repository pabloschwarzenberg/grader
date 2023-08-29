def numero_perfecto(a):
    a = int(a)
    divisores =  []
    suma = 0
    if a == 1:
        return True
    else:
        for i in range(1, a):
            if a%i == 0:
                divisores.append(i)

    for i in divisores:
        suma = suma + i
    if suma == a:
        return True
    else:
        return False
if __name__=="__main__":
  print(suma_divisores(a=input()))
    


    
           