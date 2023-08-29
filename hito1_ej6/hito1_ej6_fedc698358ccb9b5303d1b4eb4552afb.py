x=int(input("ingrese el primer numero"))
y=int(input("ingrese el segundo numero"))
z=int(input("ingresr tercer numero"))
ma=0
mi=0
me=0
if x>=y and x>=z:
    ma=x
elif y>=x and y>=z:
    ma=y
elif z>=x and z>=y:
    ma=z
if x>=y or x>=z:
    mi=x
elif y>=x or y>=z:
    mi=y
elif z>=x or z>=y:
    mi=z
if x<=y and x<=z :
    me=x
elif y<=x and y<=z:
    me=y
elif z<=y and z<=x:
    me=z
print(me,",",mi,",",ma)