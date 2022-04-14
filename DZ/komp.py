print('Введите параметры')
ram = int(input('Оперативная память: '))
ssd = int(input('Размер диска SSD: '))
hdd = int(input('Размер диска HDD: '))
price = int(input('Цена: '))
a = int(input('Состояние: '))

if ram >= 4 and ram <= 8 and ssd >=256 and hdd >= 1024:
    print('Yes0')
elif price <= 1000 and a == 5:
    print('Yes2')
else:
    print('No3')
