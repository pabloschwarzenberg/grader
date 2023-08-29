#Sistema de Ecuaciones
def solucion_sistema_ecuaciones(a,b,c,d,e,f):
  determinante = a*e - b*d
  if determinante !=0:
    x = (c*e - b*f)/ determinante
    y = (a*f - c*d)/ determinante
      
  else:
       print("Digite los valores  para a , b , c , d , e ,f: )
        a,b,c,d,e,f = map(float,input().split())
        print(solucion_sistema_ecuaciones(a,b,c,d,e,f))