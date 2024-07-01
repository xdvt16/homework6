# Словарь.
# Создаём переменную "my_dict" и присваиваем ей словарь из нескольких пар ключ-значение.
my_dict = {'Timur': 2007, 'Stepan': 1994, 'Milana': 1990, 'Vadim': 1977}
print(my_dict)
print(my_dict.get("Timur"))  # По существущему ключу
print(my_dict.get("Alex", 'Отсутствующий ключ'))  # По отсутствующему ключу

# Добавляем две пары.
my_dict.update({'Masha': 1988,
                'Vlad': 2012,
                'Conor': 2001,
                'Zhora': 1999})
print(f'Добавили пары: {my_dict}')

# Удаляем одну из пар в словаре.
a = my_dict.pop("Vlad"); b = my_dict.pop("Masha")
print(f'Удалили пары: {my_dict}')
print(f'Значение удалённых пар: {a, b,}')

# Множество.
# Создаём переменную "my_set" и присваиваем ей множество.
my_set = {False, 1, 2, 2.3, 3, 4, 5, 675, "Mouse", False, 0, 2, 4, "Spoon", 1, 675, 2.3, "Fork", "Spoon"}
print(my_set)

# Добавляем 2 элемента.
my_set.add("Table",), my_set.add("Chair")

# Удаляем 1 элемент.
my_set.discard("Mouse")

print(my_set)
