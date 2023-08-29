#Nota final
PT= float(input("ingrese nota tarea: ")) 
PI= float(input("ingrese nota interrogaciones: ")) 
NE= float(input("ingrese nota examen: ")) 
PP= float(input("ingrese nota presentacion: "))
    
    
total=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

total_nota=round(total,1)                             
    
print("nota :" +str(total_nota))