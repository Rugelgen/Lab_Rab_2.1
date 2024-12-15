# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest
doctest.testmod()

class fridge:
    def __init__(self, status: bool, content: str):
        """
        инициализация объекта холодильник
        пареметры холодильник:
        :param status: информация о том, закрыт холодильник или открыт
        :param content: информация о содержании холодильника
        >>>Xolodilnik_1 = fridge(False,слон)  # инициализация экземпляра класса
        """
        self.status = False
        self.content = None

        if not isinstance(status, bool):
            raise TypeError("Статус должен быть типа bool")
        self.status = status

        if not isinstance(content, str):
            raise TypeError("Предмет должен быть типа str")
        self.content = content

    def open_fridge(self):
        """
        Открывает холодильник если тот закрыт
        Если холодильник открыт, выводит информацию об этом в виде строки
        """
        if self.status == False:
            self.status = True
        else:
            print("холодильник открыт")

    def close_fridge(self):
        """
        Закрывает холодильник если тот открыт
        Если холодильник закрыт, выводит информацию об этом в виде строки
        """
        if self.status == True:
            self.status = False
        else:
            print("холодильник закрыт")

    def put_in_fridge(self, predmet:str):
        """"
        Позволяет положить предмет в холодильник, если тот открыт и в нём ничего нет
        """
        if self.content == None and self.status == True:
            self.content = predmet
        elif self.status == False:
            print("Холодильник зыкрыт")
        elif self.content != None:
            print(f"В холодильнике уже лежит {self.content}")

    def get_out_fridge(self):
        """"
        Позволяет убрать предмет из холодильник, если тот открыт и в нём что-то есть
        """
        if self.content != None and self.status == True:
            self.content = None
        elif self.status == False:
            print("Холодильник зыкрыт")
        elif self.content == None:
            print("В холодильнике ничего нет")

class wallet:
    def __init__(self, status: Union[int,float], color: str):
        """
        инициализация объекта Кошелёк
        пареметры Кошелька:
        :param status: информация о количесвте денег в колешьке
        :param color: информация о цвете колешелька
        пример:
        >>>Koshelek_1 = wallet(0,чёрный)  # инициализация экземпляра класса
        """
        self.status = 0
        self.color = None

        if not isinstance(status, Union[int,float]):
            raise TypeError("Статус должен быть числовым значением")
        self.status = status

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

    def put_money(self, put_money):
        """
        Позволяет положить определённое количество деньги в кошелёк
        """
        self.status = self.status + put_money

    def get_it_money(self, get_money):
        """
        Позволяет достать определённое количество денег из кошелька, если нужная сумма имеется на счету
        """
        if self.status - get_money >= 0:
            self.status = self.status - get_money
        else:
            print("Недостаточно средств для совершения операции")

class Fruit:
    def __init__(self, name: str, weight: float, colour: str):
        """
        Инициализация объекта Фрукт.
        :param name: Название фрукта
        :param weight: Вес фрукта в граммах
        :param colour: Цвет фрукта
        Примеры:
        >>> fruit = Fruit(pear, 25.8, yellow)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть числовым значением")
        if weight <= 0:
            raise ValueError("Вес фрукта должен быть положительным числом.")
        self.weight = weight

        if not isinstance(colour, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = colour

    def cut(self, piece:int) -> float:
        """
        Порезать фрукт на равные куски и вывести массу каждого из них.
        :param piece: Количество кусков
        :return: Масса куска
        Примеры:
        >>> fruit = Fruit(banana, 100, yellow)
        >>> fruit.cut(5)
        """
        if not isinstance(piece, int):
            raise TypeError("Количество кусков должно быть целым числом")
        if piece < 2:
            raise ValueError("Количество кусков должно быть не меньше двух")

    def s_estb_fruct(self):
        """
        Позволяет съесть фрукт.
        """
        del self.name 

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
