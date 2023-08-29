#Ordenar tres números
N1=int(input("ingrese numero: "))
N2=int(input("ingrese numero: "))
N3=int(input("ingrese numero: "))
menor=N1 or N2 or N3
medio=N1 or N2 or N3
mayor=N1 or N2 or N3
if N1<N2 and N3:
    N1=menor
if N2<N1 and N3:
    N2=menor
if N3<N2 and N1:
    N3=menor
if menor==N1 and N2<N3:
    menor=N1
    medio=N2
    mayor=N3
if menor==N2 and N1<N3:
    menor=N2
    medio=N1
    mayor=N3
if menor==N3 and N1<N2:
    menor=N3
    medio=N1
    mayor=N2
if menor==N1 and N3<N2:
    menor=N1
    medio=N3
    mayor=N2
if menor==N2 and N3<N1:
    menor=N2
    medio=N3
    mayor=N1
if menor==N3 and N2<N1:
    menor=N3
    medio=N2
    mayor=N1 

print(str(menor),",",str(medio),",",str(mayor))