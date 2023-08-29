A=int(input("Numero:"))
S = ""
while A>0:
    Z=int(A%2)

    S = str(Z)+S
    
    B=A-Z
    A=B/2
print("resultado=",S)



    