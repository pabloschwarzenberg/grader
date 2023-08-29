# completa el código de la función
def amigos(a,b):
    list1 = []
    list2 = []
    for i in range(1,a):
        if a % i == 0:               
            list1.append(i)
         
    for j in range(1,b):
        if b % j == 0:           
            list2.append(j)
         
    
    if sum(list1) == b and sum(list2) == a:
        return True

    else:
        return False

