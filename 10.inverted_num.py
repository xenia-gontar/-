while True:
    number = input("Введите число: \n")
    
    result = ""
    i = len(number)-1
    while i !=-1:
        result = result + number[i]
        i = i - 1
    result = result.lstrip('0')    
            

    print(f"Перевернутое число: {result} ")
