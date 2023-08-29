z = input('escribe un numero: ')
y = input('escribe un numero: ')
x = input('escribe un numero: ')

if1= (z)  + str(',') + (x) + str(',') + (y)
if z<x<y:
    print(if1)

if2= (x)  + str(',') + (z) + str(',') + (y)
if x<z<y:
    print(if2)

if3= (y)  + str(',') + (x) + str(',') + (z)
if y<x<z:
    print(if3)

if4= (y)  + str(',') + (z) + str(',') + (x)
if y<z<x:
    print(if4)

if5= (z)  + str(',') + (y) + str(',') + (x)
if z<y<x:
    print(if5)
    
if6= (x)  + str(',') + (y) + str(',') + (z)
if x<y<z:
    print(if6)


if x<y and y==z:
    print(if6)

if z<x and x==y :
    print(if1)

if y<x and x==z :
    print(if4)
      