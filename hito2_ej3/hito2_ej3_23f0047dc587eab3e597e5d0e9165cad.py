secuencia=str(input("Ingrese secuencia: "))
largo=int(input("Ingrese largo: "))
i=0
while i<(len(secuencia)):
    contador=0
    for secuencia[j][:largo] in range(i,len(secuencia)):
        
        if secuencia[i][:largo]!=secuencia[j][:largo]:
            contador=0
            i=j
            break
        else:
            contador+=1
            
    i+=1

    if contador==1:
        print("ninguna")
    else:
        print(str(secuencia[i][:largo]))
            
            


        
  