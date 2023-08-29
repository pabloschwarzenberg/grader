n = int(2);
no = int(input(" Ingrese el numero primo: "));
while(no != 1):

  if (no % n == 0):
    print(str(n) + " ");
    no = no / n;
  else:
      n = n + 1