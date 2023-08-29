#Nota final
PT= float(input("ingrese notas:"))
PI= float(input("ingrese nota interrogaciones:"))
NE= float(input("ingrese nota examen:"))
PP= float(input("ingrese nota presentacion:"))

resultado= (0.3*PT+0.3*PI +0.3*NE+PP*0.1)

print(format(resultado,'0.1f'))