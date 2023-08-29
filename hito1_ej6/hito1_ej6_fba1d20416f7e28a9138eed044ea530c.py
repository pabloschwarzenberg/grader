#Ordenar tres números
nm = []
print('Por favor ingresar tres números enteros')
for i in range(3):
  nr = int(input())
  nm.append(nr)

if nm[0] >= nm[1] and nm[0] >= nm[2]:
    if nm[1] >= nm[2]:
        print(nm[2],',',nm[1],',',nm[0])
    elif nm[2] >= nm[1]:
        print(nm[1],',',nm[2],',',nm[0])

elif nm[1] >= nm[0] and nm[1] >= nm[2]:
    if nm[0] >= nm[2]:
        print(nm[2],',',nm[0],',',nm[1])
    elif nm[2] >= nm[0]:
        print(nm[0],',',nm[2],',',nm[1])

elif nm[2] >= nm[1] and nm[2] >= nm[0]:
    if nm[1] >= nm[0]:
        print(nm[0],',',nm[1],',',nm[2])
    elif nm[0] >= nm[1]:
        print(nm[1],',',nm[0],',',nm[2])