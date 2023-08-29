def numero_perfecto(a):
    divs = []
    for i in range (1, a):
      if a % i == 0:
        i = divs.append(i)
        
    suma = 0
    for div in divs: 
      suma = suma + div
      
    if suma == a:
      Perfecto = True
    
    else:
       Perfecto = False
       
    return Perfecto

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           