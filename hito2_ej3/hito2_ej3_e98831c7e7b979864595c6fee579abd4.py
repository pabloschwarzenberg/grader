secuencia=str(input())
entero=int(input())
n=1
while n<= len(secuencia)/entero:
    subsecuencia=secuencia[entero*(n-1):entero*n]
    subsecuencia2=secuencia[1+entero*(n-1):1+entero*n]
    subsecuencia3=secuencia[2+entero*(n-1):2+entero*n]
    if subsecuencia==subsecuencia2 or subsecuencia==subsecuencia2 or subsecuencia2==subsecuencia3:
         print("ninguna")
    else:
        if secuencia.count(subsecuencia)==1:
            print(subsecuencia)
        if secuencia.count(subsecuencia)>1:
            print("ninguna")
        if secuencia.count(subsecuencia2)==1:
            print(subsecuencia2)
        if secuencia.count(subsecuencia2)>1:
            print("ninguna")
        if secuencia.count(subsecuencia3)==1:
            print(subsecuencia3)
        if secuencia.count(subsecuencia3)>1:
            print("ninguna")
      
    n+=1