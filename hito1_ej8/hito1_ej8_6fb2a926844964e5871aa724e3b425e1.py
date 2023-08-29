#Descomponer un número
N=input("ingrese numero")
I=0
S=""
largo=len(N)-1
while I<= largo:
     letra=N[I]
     if(largo-I)==0:
         S=S+letra+ "U"
     if(largo-I)==1:
         S=S+letra+ "D+"
     if(largo-I)==2:
         S=S+letra+ "C+"
     if(largo-I)==3:
         S=S+letra+ "M+"
     I=I+1
print (S)   