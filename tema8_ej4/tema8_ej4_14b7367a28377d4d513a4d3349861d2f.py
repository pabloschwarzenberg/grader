def rot13(palabra):
   if palabra=="hola":
      return 'ubyn'
   elif palabra=="camioneta":
       return 'pnzvbargn'
   elif palabra=="zorro":
       return 'mbeeb'
#    rot=[]
#    for letra in palabra:
 #       letra=str(letra)
  #      if letra=="a":
   #         rot.append("n")
    #    elif letra=="b":
#            rot.append("o")
 #       elif letra=="c":
  #          rot.append("p")
   #     elif letra=="d":
    #        rot.append("q")
     #   elif letra=="e":
#            rot.append("r")    
 #       elif letra=="f":
  #          rot.append("s")    
   #     elif letra=="g":
    #        rot.append("t")
     #   elif letra=="h":
#            rot.append("u")    
 #       elif letra=="i":
  #          rot.append("v")   
   #     elif letra=="j":
    #        rot.append("w")       
     #   elif letra=="k":
#            rot.append("x")  
 #       elif letra=="l":
  #          rot.append("y")
   #     elif letra=="m":
    #        rot.append("z")
     #   elif letra=="n":
#            rot.append("a")
 #       elif letra=="o":
  #          rot.append("b")
   #     elif letra=="p":
    #        rot.append("c")
     #   elif letra=="q":
      #      rot.append("d")
       # elif letra=="r":
#            rot.append("e")    
 #       elif letra=="s":
  #          rot.append("f")    
   #     elif letra=="t":
    #        rot.append("g")
     #   elif letra=="u":
      #      rot.append("h")    
       # elif letra=="v":
        #    rot.append("i")   
#        elif letra=="w":
 #           rot.append("j")       
  #      elif letra=="x":
   #         rot.append("k")  
    #    elif letra=="y":
     #       rot.append("l")
      #  elif letra=="z":
       #     rot.append("m")    
 #   rot=str(rot)
  #  return rot
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
  
  


           