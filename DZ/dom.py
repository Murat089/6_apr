print('Выбор дома')
dom = input('Введите район: ' )
material = input('Материал дома: ')
sotyh = int(input('Введите площадь участка: '))
summa = int(input('Введите сумму: '))

if dom == "ortosay" or dom == "baytik" or dom == "chonaryk": 
    print('Район подходит!')
if material == 'kirpich' and sotyh == 4 and summa <= 50000 or summa >= 46000: 
    print('Кирпичный дом.')
elif material == 'peskoblok' and sotyh == 5 and summa <= 45000:
    print('Песблочный дом.')
else:
    print('не подходит!')
