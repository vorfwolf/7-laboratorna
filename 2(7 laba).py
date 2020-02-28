products = [{'Назва': 'Спічки', 'Кількість': '7', 'Ціна': 14, 'Виробник': 'Господарські', 'Дата': 28.03},
            {'Назва': 'Вино', 'Кількість': '7', 'Ціна': 26, 'Виробник': 'Швейн', 'Дата': 08.04},
            {'Назва': 'Олія', 'Кількість': '2', 'Ціна': 22, 'Виробник': 'Олейна', 'Дата': 21.07},
            {'Назва': 'Крупа', 'Кількість': '6', 'Ціна': 18, 'Виробник': 'Домашня', 'Дата': 03.08}]

all_price = 0

for i in range(len(products)):
    all_price += products[i].get('Ціна')

serednya_price = all_price/len(products)
print('Середня ціна:', serednya_price)

for i in range(len(products)):
    if(products[i].get('Ціна') > serednya_price):
        print(products[i])
