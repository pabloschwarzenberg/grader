# completa el código de la función
def suma_divisores(a):
            c=1
            suma_total=0
            while c<a:
                if a%c==0:
                    suma_total += c
                   
                c += 1

            if suma_total ==1:
               return suma_total , True 
            else:
               return suma_total , False 