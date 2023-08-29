def rot13(palabra):
    abc = "abcdefghijklmnopqrstuvwxyz"
    secret = "".join([abc[(abc.find(c)+13)%26] for c in palabra])
    return secret
if _name_ == "_main_":
  s=input("Escriba algo: \n")
  x=rot13(s)
  print(x)
           