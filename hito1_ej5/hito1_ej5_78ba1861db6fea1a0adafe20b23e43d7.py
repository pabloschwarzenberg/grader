n_rut=str(input("Ingrese su rut"))
largo=len(n_rut)
posicion=largo-1
x=range(largo)
prod=0
for n in x:
      if n == 6:
          prod = prod + (int(n_rut[posicion]) * 2)
          posicion = posicion -1
      elif n == 7:
          prod = prod + (int(n_rut[posicion]) * 3)
          posicion = posicion -1
      else:
          prod = prod + (int(n_rut[posicion]) *(n+2))
          posicion = posicion -1
          
prod=prod % 11
prod=11-prod

if prod>=11:
    print("dv=0")
elif prod==10:
    print("dv=K")
else:
    print("dv=",prod)
