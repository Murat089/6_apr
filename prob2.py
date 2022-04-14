a = int(input('Введите 1-число:'))
b = int(input('Введите 2-число:'))
c = int(input('Введите 3-число:'))

if a > b and a > c:
    print('1-число больше')
elif b > a and b > c:
    print('2-число больше')
elif c > a and c > b:
    print('3-число больше')
elif a == b and a == c:
    print('Все числа равны')
