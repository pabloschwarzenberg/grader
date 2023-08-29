from copy import copy
n=int(input())
l=["1","0"]
todas_combinaciones=[]
def combinaciones(actual=None):
    if not actual:
        actual=[]

    if len(actual)==n:
        x="".join(actual)
        todas_combinaciones.append(copy(x))
        return

    for i in l:
        actual.append(i)
        combinaciones(actual)
        actual.pop(-1)

combinaciones()
for i in todas_combinaciones:
    print(i)

