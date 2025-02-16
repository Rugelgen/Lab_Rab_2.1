if __name__ == "__main__":
    class Conifer:
        """
        Основное применение - создание объектов (хвойное дерево), основной класс

        Attributes
        ----------
        id: int

            Уникальный неповторяющийся номер для каждого нового объекта
            Инкапсулирован, вследствие препятствия искажения данных пользователем

        date_of_seed: dict = {"day": ...,"mounth": ..., "year": ...}

            Дата посадки дерева (день, месяц, год)
            Инкапсулирован, вследствие препятствия искажения данных пользователем

        Methods
        -------
        def age_of_tree(self, date_of_seed, system_date):

            Метод возвращает возраст(года, месяца, дни) дерева в виде строкового значения
            Метод зависит от конкретной даты на данный момент
            У метода должен быть доступ к времени на устройстве
            Метод вычесляет разницу в годах, месяцах и днях между посадкой дерева и настоящим моментом

        def shed_needles(self):

            выводит текст - Хвойное дерево сбрасывает иглы.

        """
        def __init__(self, id: int, date_of_seed: dict = {"day": ..., "mounth": ..., "year": ...}):
            self._id = id
            self._date_of_seed = date_of_seed

            if not isinstance(date_of_seed['day'], int):
                raise TypeError("День должен быть типа int")

            if not isinstance(date_of_seed['mounth'], int):
                raise TypeError("Месяц посадки должен быть типа int")

            if not isinstance(date_of_seed['year'], int):
                raise TypeError("Год посадки должен быть типа int")

        @property
        def id(self):
            return self._id

        @property
        def date_of_seed(self):
            return self._date_of_seed

        def __str__(self):
            return f"ID дерева - {self.id}. Дата посадки - {self.date_of_seed['day']}.{self._date_of_seed['mounth']}.{self._date_of_seed['year']}"

        def __repr__(self):
            return f"{self.__class__.__name__}id={self.id!r}, date_of_seed={self.date_of_seed!r}"

        def age_of_tree(self, date_of_seed, system_date):
            ...

        @staticmethod
        def shed_needles():
            print("Хвойное дерево сбрасывает иглы.")


    class FirTree(Conifer):
        """
        Основное применение - создание объектов (еловое дерево), дочерний класс

        Attributes
        ----------
        id: int
            Наследуемый атребут

        date_of_seed: dict = {"day": ...,"mounth": ..., "year": ...}

            Наследуемый атребут

        Methods
        -------

        def __str__(self)

            перегружен, вследствие дополнения входных данных

        def __repr__(self)

            перегружен, вследствие дополнения входных данных

        def age_of_tree(self, date_of_seed, system_date):

            Наследуемый метод

        def shed_needles(self):

            метод был перегружен вследствие изменения действия для данного класса
            выводит текст - Ель сбрасывает иглы весной.

        """

        def __init__(self, id: str, date_of_seed: dict, type_of_fir: str):
            self._type_of_fir = type_of_fir
            super().__init__(id=id, date_of_seed=date_of_seed)
            super().age_of_tree(date_of_seed, system_data)
            if type_of_fir in type_list1:
                ...
            else:
                raise NameError("Данный тип дерева не найден")

        def __str__(self):
            return f"{super().__str__()}, Тип ели - {self.type_of_fir}"

        def __repr__(self):
            return f"{super().__repr__()}, type_of_fir={self.type_of_fir!r}"

        @property
        def type_of_fir(self):
            return self._type_of_fir

        @type_of_fir.setter
        def type_of_fir(self, type_of_fir):
            self._type_of_fir = type_of_fir

        def shed_needles(self):
            print("Ель сбрасывает иглы весной.")

system_data = {"year": 2025, "mounth": 2, "day": 10}
type_list1 = ("ель обыкновенная", "ель шероховатая")
fir_tree = FirTree(1, {"year": 1, "mounth": 0, "day": 1}, "ель шероховатая")
print(fir_tree.__str__())
print(fir_tree.__repr__())
fir_tree.shed_needles()
