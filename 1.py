money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
counter = 0
capital = (money_capital + (salary))
while spend <= capital:
    counter += 1
    capital -= spend
    spend += (spend * (increase))
    capital+=salary

print("Количество месяцев, которое можно протянуть без долгов:", counter)
