#Ordenar tres números
a= int(input('introdusca primer número:  '))
a1= int(input('introdusca sengundo número: '))
a2= int(input('introdusca tercer número: '))

#a menor que todos
if a <= a1 and a <= a2:
    if a1 <= a2:
        print(a,', ',a1,', ',a2)
    elif a2 <= a1:
        print(a,', ',a2,', ',a1)
        
#a1 menor de todos
elif a1 <= a and a1 <= a2:
    if  a <= a2:
        print(a1,', ',a,', ',a2)
    elif a2 <= a:
        print(a1,', ',a2,', ',a)

#a2 menor que todos
elif a2 <= a and a2 <= a1:
    if a <= a1:
        print(a2,', ',a,', ',a1)
    elif a1 <= a:
        print(a2,', ',a1,', ',a)