names = input('Введите название файла: ')

if names == 'my_phtot.png':
    print(names.index('png'))
    print(names[::])
    print("Расширение файла: png") 
else:
    print('Расширение не найдено!')
