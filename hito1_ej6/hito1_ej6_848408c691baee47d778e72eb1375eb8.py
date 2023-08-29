#Ordenar tres números
#-------------------------------------------------------#
class Numbers:
  while True:
     try:
         FirstNumber = int(input('Enter the first number '))
         SecondNumber = int(input('Enter the second number '))
         ThirdNumber = int(input('Enter the third number '))
         break
     except:
        print("Enter a valid number")       
#-------------------------------------------------------#
class Calculations:
    
  Maximum = max(Numbers.FirstNumber, Numbers.SecondNumber, Numbers.ThirdNumber)
  Minimum = min(Numbers.FirstNumber, Numbers.SecondNumber, Numbers.ThirdNumber)
  Medium  = (Numbers.FirstNumber + Numbers.SecondNumber + Numbers.ThirdNumber) - Minimum - Maximum

#-------------------------------------------------------#
def PrintResults():
    print('The numbers in ascending order are {}, {}, {}'.format(Calculations.Minimum, Calculations.Medium, Calculations.Maximum))



PrintResults()      