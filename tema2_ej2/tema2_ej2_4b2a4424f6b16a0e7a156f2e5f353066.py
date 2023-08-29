def amigos(a,b):
    def findDivButDumb(a):
        divis = []  
        for div in range(1,a):
            if (a%div) == 0:
                divis.append(div)
        return divis
    divList1 = findDivButDumb(a)
    divList2 = findDivButDumb(b)
    if a == 1 or b == 1:
        return False
    if a == sum(divList2) and b == sum(divList1):
        return True
    else:
        return False