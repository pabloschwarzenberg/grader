#Factores Primos
lista=[]
def primo(num1):

for x in range (1,num1):
if (num1%x==0 and x!=num1 and x!=1):
return False
return num1