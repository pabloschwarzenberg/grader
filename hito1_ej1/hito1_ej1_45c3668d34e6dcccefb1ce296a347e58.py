#Nota final
def promedio(n1,n2,n3,n4):
  x=0.3*n1+0.3*n2+0.3*n3+0.1*n4
  promedio=round(x,1)
  return promedio
nt=float(input("ingrese nota tareas:"))
ni=float(input("ingrese nota interrogaciones:"))
ne=float(input("ingrese nota de examen:"))
np=float(input("ingrese nota de presentacion:"))
print(promedio(nt,ni,ne,np))