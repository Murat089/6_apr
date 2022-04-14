mashina = input("Марка авто: ")
mashina1 = input("Модель авто: ")
god = int(input("Год выпуска: "))
cena = int(input("Цена: "))
probeg = int(input("Пробег км: "))
cvet = input("Цвет авто: ")
hoz = int(input("Хозяин: "))
rul = input("Руль 'правый или левый': ")

if mashina == "Toyota" and mashina1 == "Lexus" or god >= 2004:
    print("OK0")
if cena <= 100000 and probeg == 150000 or probeg == 200000 and cena <= 80000:
    print("OK1")
if cvet == "white" or cvet == "grey" and hoz <= 2 and rul == "left":
    print("OK2")
else:
    print("Bolboit")
