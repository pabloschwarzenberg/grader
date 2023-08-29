#Suma de los N primeros números
#Suma de los N primeros números
#-------------------------------------------------------#
class Number:
  while True:
     try:
         NaturalNumber = int(input('Enter your number '))
         if NaturalNumber < 0:
            print("ERROR! Natural numbers cannot be negative!")
            continue
         break
     except:
        print("ERROR! You must enter a natural number!")
#-------------------------------------------------------#
def Calculation():

 Result = int(Number.NaturalNumber * (Number.NaturalNumber + 1) / 2)
 print("The sum of the first {} natural numbers is {}" .format(Number.NaturalNumber, Result))
#-------------------------------------------------------# 
Calculation()
#-------------------------------------------------------#       