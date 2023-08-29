def numero_perfecto(a):
   divisor=1
   sumadivisores=0
   while divisor<a:
        if a%divisor==0:
            sumadivisores+=divisor
        divisor+=1 
   if sumadivisores==a:
      return True
   else:
      return False

if __name__ == "__main__": 
  a=int(input())
  print(numero_perfecto(a))
   