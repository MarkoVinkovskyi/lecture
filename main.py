l = int(input("Введіть число: "))
i = 1
factorial = 1
while i<=l:
    factorial *=i
    i+=1
print("Факторіал числа {} дорівнює {}".format(l,factorial))

