# por favor escribe aquí tu función
def es_primo(num):
    if num <= 1 :
        print ("FALSE")
        return False
    else:
       for i in range(2,num-1):
           if num%i==0:
              print ("FALSE")
              return False

    if num%1==0 and num%num==0:
        print ("TRUE")
        return True

num= int(input("ingrese numero"))

num= es_primo(num)

           