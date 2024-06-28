def is_even(number):
    if number % 2 == 0:
        return True
    return False

def action(number):
    if is_even(number) == True:
        return number / 2
    else:
       return (number*3) + 1
    

while True:
    number = int(input("Введите число: \n"))
    
    while number != 1:
        print(action(number))
        number = action(number)
