#Factores Primos
supermeganumeritos = int(input("ingresa tu numero :D "))
w=2
while w<=supermeganumeritos:


    if supermeganumeritos%w==0:
    
    
        print(w)
        
        supermeganumeritos = supermeganumeritos/w
    else:
    
        w+=1
