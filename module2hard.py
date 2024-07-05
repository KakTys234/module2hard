
def your_password(n):
    numbers = ''
    for i in range(1, (n + 1) // 2):
        j = i + 1
        while i + j <= n:
            if n % (i + j) == 0:
                numbers += str(i) + str(j)
            j += 1
    return numbers


name = True
while name:
    num = int(input('Введите проверочное число для пароля: '))
    if num in range(3, 21):
        name = False
    else:
        print('Превышен предел ряда чисел от 3 до 20')
        print('Введите число еще раз')
password = your_password(num)
print(f'К Вашему числу {num} подходят пароли: {password}')
