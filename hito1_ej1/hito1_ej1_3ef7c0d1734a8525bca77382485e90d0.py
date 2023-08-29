#Nota final
PT = float(input("favor ingresar nota 1:"))
PI = float(input("favor ingresar nota 2:"))
NE = float(input("favor ingresar nota 3:"))
PP = float(input("favor ingresar nota 4:"))
 
nota1 = PT  
nota2 = PI   
nota3 = NE   
nota4 = PP   
 
NF = round((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP), 1)

 
print(NF)
