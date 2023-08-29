#Factores Primos
A = int(input ("Ingresar número:"))
B = A
C = 2
while C<A:
    X = 2
    primo = True
    while X<C:
        if C%X == 0:
            primo = False
            break
        X = X+1
    if primo == True:
    
        while B%C == 0:
            print(C)
            B = B/C
    C = C+1 
if A == 2:
  print(2)
        
