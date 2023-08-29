def jerigonzo(string):
     s = ""
     for i in range(len(string)):
         letra=string[i]
         if letra=="a" or letra=="á" or letra=="A" or letra=="Á" or letra=="e" or letra=="é" or letra=="E" or letra=="É" or letra=="i" or letra=="í" or letra=="I" or letra=="Í" or letra=="o" or letra=="ó" or letra=="O" or letra=="Ó" or letra=="u" or letra=="ú" or letra=="U" or letra=="Ú":
            s = s + letra + "p" + letra
            print(letra+"p"+letra, end="")
         else:
            s = s + letra
            print(letra,end="")
     return s
            

if __name__ == "__main__":

  string=input()
  print(jerigonzo(string))
 
         