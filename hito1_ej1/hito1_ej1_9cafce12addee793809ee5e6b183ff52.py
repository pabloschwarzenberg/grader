#Nota final
PT=float(input("Nota tareas:"))  
PI=float(input("Nota interrogaciones:"))     
PE=float(input("Nota examen:"))
PP=float(input("Nota Presentación:"))      

NF= 0.3*(PT+PI+PE)+0.1*PP
y=round(NF,1)
print(y)