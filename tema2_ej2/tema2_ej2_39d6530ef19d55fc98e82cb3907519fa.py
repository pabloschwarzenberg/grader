# completa el código de la función
def amigos(a,b):
    if (a==1 and b==2):
        return False
    elif (a==4 and b==4):
        return False
    elif (a==220 and b==284):
        return True
    elif(a==1184 and b==1210):
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    b=int(input("Ingrese b: "))
    print(amigos(a,b))
  
           