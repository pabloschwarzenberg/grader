def amigos(a,b):
        contadora=1
        contadorb=1
        sumaa=0
        sumab=0
        
        if a==1 and b==1:
            return True
        elif a==1 and b!=1:
            return False
        elif b==1 and a!=1:
            return False

        else:
            while contadora<a:
                if a%contadora==0:
                    sumaa=sumaa+contadora

                contadora=contadora+1

        
            while contadorb<b:
                if b%contadorb==0:
                    sumab=sumab+contadorb

                contadorb=contadorb+1

        if sumab==a or sumaa==b:
            return True

        
        else:
            return False