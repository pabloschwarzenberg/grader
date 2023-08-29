n1=int(input("Ingrese primer numero:"))
n2=int(input("Ingrese segundo numero:"))
n3=int(input("Ingrese tercer numero:"))
if n1<n2 and n1<n3:
  menor=n1
  if n2<n3:
    medio=n2
    mayor=n3
  else:
    medio=n3
    mayor=n2
elif n2<n1 and n2<n3:
  menor=n2
  if n1<n3:
    medio=n1
    mayor=n3
  else:
    medio=n3
    mayor=n1
elif n3<n1 and n3<n2:
  menor=n3
  if n1<n2:
    medio=n1
    mayor=n2
  else:
    medio=n2
    mayor=n1
print(menor,',',medio,',',mayor)