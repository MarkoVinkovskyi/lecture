print("Для виходу натисніть Y")
while True:
    data=input("Введіть суму для обміну:")
    if data.lower() == "y":
        break
    money = int(data)
    if money <0:
        print("Сума має бути позитивною")
        continue
    cache = round(money/56.2)
    print("Да видачі {} доларів".format(cache))

print("Робота обмінного пункту завершано")