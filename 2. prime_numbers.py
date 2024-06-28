while True:
    number = int(input("Введите число: \n"))
    
    is_prime = 0
    for i in range(2, number):
        if number % i == 0:
            is_prime =1
            print("Данное число не является простым.")
            break;
    if is_prime == 0:
        print("Данное число является простым.")
