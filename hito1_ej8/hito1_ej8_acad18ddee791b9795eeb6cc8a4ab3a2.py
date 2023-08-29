#Descomponer un número
a=input("ingrese numero de 4 digitos:")
if(len(a)==4):
    s=a[0]
    d=a[1]
    f=a[2]
    g=a[3]
    print(s+"M+"+d+"C+"+f+"D+"+g+"U")
else:
    if(len(a)==3):
     s="0"
     d=a[-3]
     f=a[-2]
     g=a[-1]
     print(s+"M+"+d+"C+"+f+"D+"+g+"U")
    else:
        if(len(a)==3):
         s="0"
         d=a[-3]
         f=a[-2]
         g=a[-1]
         print(s+"M+"+d+"C+"+f+"D+"+g+"U")
        else:
            if(len(a)==2):
              s="0"
              d="0"
              f=a[-2]
              g=a[-1]
              print(s+"M+"+d+"C+"+f+"D+"+g+"U")
            else:
                if(len(a)==1):
                 s="0"
                 d="0"
                 f="0"
                 g=a[-1]
                 print(s+"M+"+d+"C+"+f+"D+"+g+"U")
                else:
                    print("no ingresaste un numero")
                
