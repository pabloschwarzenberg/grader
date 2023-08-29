def jerigonzo(string):
     x=len(string)
     z=0
     i=0
     string1=""
     while i<x:
          string1=string1+string[i]
          if string[i]=="a":
               string1=string1+"p"
               string1=string1+"a"
               
          if string[i]=="e":
               string1=string1+"p"
               string1=string1+"e"
          if string[i]=="i":
               string1=string1+"p"
               string1=string1+"i"
          if string[i]=="o":
               string1=string1+"p"
               string1=string1+"o"
          if string[i]==u"":
               string1=string1+"p"
               string1=string1+"u"
          i=i+1
     string=string1
     return string


         