       
while True:
    number = int(input("Введите число: \n"))
    
    fac = 1
    for i in range(1, number+1):
        fac = fac * i
        
    print(f"Факториал числа {number} равен {fac}")    
        
