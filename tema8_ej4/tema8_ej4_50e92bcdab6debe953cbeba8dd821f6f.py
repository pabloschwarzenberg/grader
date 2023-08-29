def rot13(palabra):
   abc = "abcdefghijklmnopqrstuvwxyz"
   L = ""
   for char in palabra:
       L += abc[(abc.find(char)+13)%26]
   return L
