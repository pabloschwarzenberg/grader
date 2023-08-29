def determinar_primos():
    for i in range(3,101):
        contador=0
        for j in range(1,i+1):
            if i%j == 0:
                contador=contador+1
        if contador==2:
            print(str(i) + " ")

determinar_primos()