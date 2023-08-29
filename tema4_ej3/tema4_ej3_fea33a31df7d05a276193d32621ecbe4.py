def jerigonzo(string):
    a=""
    i=0
    while i<len(string):
       if string[i]=="a":
          a=a+string[i]+ ("pa")
          print(a)
       elif string[i]=="e":
          a=a+string[i]+ ("pe")
          print(a)
       elif string[i]=="i":
          a=a+string[i]+ ("pi")
          print(a)
       elif string[i]=="o":
          a=a+string[i]+ ("po")
          print(a)
       elif string[i]=="u":
          a=a+string[i]+ ("pu")
          print(a)
       else:
          a=a+string[i]
          print(a)
       i=i+1
          
    return a

if __name__ == "__main__":
    palabra=str(input("Ingrese palabra: "))
    print(jerigonzo(palabra))
    