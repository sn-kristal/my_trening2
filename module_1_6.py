my_dict={'Kolja':1998,"Kira":1984,"Sveta":1972,"Danil":2019}
print("Дикт:", my_dict)
print("Текущее значение:", my_dict["Kira"])
print(my_dict.get("Sergey","Несуществующее значение.Нет"))
my_dict.update({"Semen":2024,"Evgen":1982})
print("Модифицированный словарь:", my_dict)
a = my_dict.pop("Sveta")
print("Модифицированный словарь:", my_dict)
#a = my_dict.pop("Sveta")
print("Удаленное значение:", a )
print("Модифицированный словарь", my_dict)
my_set = {28,"Orang","book",62.5,28}
print(my_set)
my_set.update([8,5])
print(my_set)
my_set.remove("book")
print(my_set)