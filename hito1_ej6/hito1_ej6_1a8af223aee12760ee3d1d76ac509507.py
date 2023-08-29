num1 = int(input("ingresa el primer número: "));
num2 = int(input("ingresa el segundo número: "));
num3 = int(input("ingresa el tercer numero: "));


def ordenados(nums):
  s = len(nums);
  for i in range(s):
    for j in range(1, s - i):       
        if nums[j-1] > nums[j]:
            (nums[j-1], nums[j]) = (nums[j], nums[j-1])
  return nums;

numeros = ordenados([num1, num2, num3]);
print(numeros);