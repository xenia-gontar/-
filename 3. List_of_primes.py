def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True        
while True:
    number = int(input("Введите число: \n"))
    print("Список простых чисел: \n")
    for i in range(2, number):
        if is_prime(i) == True:
            print(i)
 
