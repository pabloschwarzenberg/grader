#Descomponer un número
def string_int(txt):
     num_int = [int(i)for i in txt]
     print(num_int)

user_in = input("enter a number: ")
string_int(user_in)