def factorial(number):
    fac = 1
    for i in range(1, number + 1):
        fac = fac * i
    return fac     


while True:
    n = int(input("Введите число n: \n"))
    k = int(input("Введите число k: \n"))
        
    print(f"Число размещений из {n} по {k}:  равно {factorial(n)/factorial(n-k)}\n") 
    print(f"Число сочетаний из {n} по {k}:  равно {factorial(n)/(factorial(n-k)*factorial(k))}\n")  
