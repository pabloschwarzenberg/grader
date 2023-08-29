def numero_perfecto(a):
    list1 = [0]
    for i in range(1,a):
        if a % i == 0:
            list1.append(i)
    if sum(list1) == a:
        return True
    if sum(list1) !=a:
        return False

