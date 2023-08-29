#Nota final
PT = float(input("nota PT:"))        
PI = float(input("nota PI:"))      
NE = float(input("nota NE:"))         
PP = float(input("nota PP:"))

promedio = (PT*(0.3) + PI*(0.3) + NE*(0.3) + PP*(0.1))
print("promedio aproximado %5.1f" %round(promedio,1))
      