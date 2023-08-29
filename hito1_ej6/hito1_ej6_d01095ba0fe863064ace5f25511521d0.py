#Ordenar tres número
primero=int(input())
segundo=int(input())
tercero=int(input())
if primero<=segundo<=tercero:
     print(primero,",",segundo,",",tercero)
if primero<=tercero<=segundo:
     print(primero,",",tercero,",",segundo)
if segundo<=primero<=tercero:
     print(segundo,",",primero,",",tercero)
if segundo<=tercero<=primero:
     print(segundo,",",tercero,",",primero)
if tercero<=segundo<=primero:
     print(tercero,",",segundo,",",primero)
if tercero<=primero<=segundo:
     print(tercero,",",primero,",",segundo)    