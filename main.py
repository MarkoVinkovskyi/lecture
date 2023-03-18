l = int(input("Введіть число: "))
factorial = 1
for i  in range(1,l+1):
    factorial *=i
print("Факторіад числа {} дорівнює {}".format(l,factorial))