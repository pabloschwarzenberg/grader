#Factores Primos
N = int(input ("Ingrese número:"))
M = N
J = 2
while J<N:
    I = 2
    es_primo = True
    while I<J:
        if J%I == 0:
            es_primo = False
            break
        I = I+1
    if es_primo == True:
    
        while M%J == 0:
            print(J)
            M = M/J
    J = J+1 
if N == 2:
  print(2)
        
