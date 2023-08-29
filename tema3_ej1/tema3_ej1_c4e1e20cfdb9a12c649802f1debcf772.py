# completa el código de la función

def suma_divisores(a):
    sumadivisores=0
    divisor=1
    while divisor<a:
        if a%divisor==0:
            sumadivisores+=divisor
        divisor+=1      
    return (sumadivisores, sumadivisores == 1)
        

        
if __name__ == "__main__":
  a=int(input())
  print(suma_divisores(a))

