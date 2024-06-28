while True:
    array = []
    number = int(input("Введите число: \n"))
    for i in range(1, number):
        if number % i == 0:
            array.append(i)
    sum = 0
    for element in array:
        sum = sum + element
    if sum == number:
        print("Число совершенное.")
    else:
        print("Число не совершенное.")
