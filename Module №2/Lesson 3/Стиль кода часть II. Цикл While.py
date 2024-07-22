while True:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print('Число чётное')
        continue
    else:
        print('Не чётное число')
    print('Меня не забыли')

print('Я за циклом')
