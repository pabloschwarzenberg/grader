def jerigonzo(palabra):
 jerigonzo=""
 for vocal in palabra:
    if vocal=="a":
        jerigonzo+="apa"
    elif vocal=="e":
        jerigonzo+="epe"
    elif vocal=="i":
        jerigonzo+="ipi"
    elif vocal=="o":
        jerigonzo+="opo"
    elif vocal=="u":
        jerigonzo+="upu"
    elif vocal=="A":
        jerigonzo+="Apa"
    elif vocal=="E":
        jerigonzo+="Epe"
    elif vocal=="I":
        jerigonzo+="Ipi"
    elif vocal=="O":
        jerigonzo+="Opo"
    elif vocal=="U":
        jerigonzo+="Upu"    
    else:
        jerigonzo+=vocal
 return jerigonzo
    
if __name__ == "__main__":
  palabra=input()
  jerigonzo(palabra)