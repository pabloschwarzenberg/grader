#Ordenar tres números
#profe me toco usar el argumento sep="," ya que no me permite usar el print(f"{menor},{medio},{mayor}") por que me da un error

N1=input("Ingrese primer numero: ")
N2=input("ingresew segundo numero: ")
N3=input("ingrese tercer numero: ")

if N1<N2 and N2<N3:
    menor=N1
    medio=N2
    mayor=N3
elif N2<N1 and N1<N3:
    menor=N2
    medio=N1
    mayor=N3
elif N3<N1 and N3<N2:
    menor=N3
    medio=N2
    mayor=N1
elif N1<N2 and N3<N2:
    menor=N1
    medio=N3
    mayor=N2
elif N2<N1 and N2<N3:
    menor=N2
    medio=N3
    mayor=N1
    
print(menor, medio, mayor, sep=", ")
