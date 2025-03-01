class Animal:
    """ Базовый класс для всех животных. """

    def __init__(self, name: str, age: int):
        """
        Инициализация животного.

        :param name: Имя животного.
        :param age: Возраст животного в годах.
        """
        self._name = name  # Защита атрибута, чтобы предотвратить его изменение извне
        self._age = age

    @property
    def name(self) -> str:
        """ Возвращает имя животного. """
        return self._name

    @property
    def age(self) -> int:
        """ Возвращает возраст животного. """
        return self._age

    def speak(self) -> str:
        """ Возвращает звук, который издает животное. """
        return "Я животное."

    def __str__(self) -> str:
        """ Возвращает строковое представление животного. """
        return f"{self.__class__.__name__}(Имя: {self.name}, Возраст: {self.age})"

    def __repr__(self) -> str:
        """ Возвращает формальное строковое представление животного. """
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"


class Dog(Animal):
    """ Класс для собак, наследуется от класса Animal. """

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация собаки.

        :param name: Имя собаки.
        :param age: Возраст собаки в годах.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)
        self._breed = breed  # Защита атрибута породы

    @property
    def breed(self) -> str:
        """ Возвращает породу собаки. """
        return self._breed

    def speak(self) -> str:
        """ Переопределяет метод speak для собак. """
        return "Гав!"

    def __str__(self) -> str:
        """ Возвращает строковое представление собаки. """
        return f"Собака(Имя: {self.name}, Возраст: {self.age}, Порода: {self.breed})"


class Cat(Animal):
    """ Класс для кошек, наследуется от класса Animal. """

    def __init__(self, name: str, age: int, color: str):
        """
        Инициализация кошки.

        :param name: Имя кошки.
        :param age: Возраст кошки в годах.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)
        self._color = color  # Защита атрибута цвета

    @property
    def color(self) -> str:
        """ Возвращает цвет кошки. """
        return self._color

    def speak(self) -> str:
        """ Переопределяет метод speak для кошек. """
        return "Мяу!"

    def __str__(self) -> str:
        """ Возвращает строковое представление кошки. """
        return f"Кошка(Имя: {self.name}, Возраст: {self.age}, Цвет: {self.color})"


# Примеры использования:
dog = Dog("Шарик", 3, "Лабрадор")
cat = Cat("Мурка", 2, "Черный")

print(dog)
print(cat)

print(dog.speak())  # Гав!
print(cat.speak())  # Мяу!
