yazyk = input('Введите язык: ')
vozrast = int(input('Введите возраст: '))
opyt = int(input('Опыт: '))
zarplata = int(input('Желаемая зарплата: '))

if yazyk == "python" or yazyk == "java" or yazyk == "javascript":
    print('Ok1')
if vozrast >= 18 or vozrast <= 65:
    print('ok2')
if opyt >= 3:
    print('ok3')
if zarplata <= 60000:
    print('ok4')
else:
    print('NO')
