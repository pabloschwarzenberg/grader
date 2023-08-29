x=int(input('ingrese el primer numero:'))
y=int(input('ingrese el segundo numero:'))
z=int(input('ingrese el tercer numero:'))
if x<=y and x<=z:
    men=x
    if y<=z:
        med=y
        may=z
    else:
        med=z
        may=y
elif y<=x and y<=z:
    men=y
    if x<=z:
        med=x
        may=z
    else:
        med=z
        may=x
else:
    men=z
    if x<=y:
        med=x
        may=y
    else:
        med=y
        may=x
print(str(men),',',str(med),',',str(may))        