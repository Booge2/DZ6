class Fraction:
    """
    Опис класу "Дріб".
    """
    instances_count = 0

    def __init__(self, numerator, denominator):
        """
        :param numerator:
        :param denominator:
        """
        self.numerator = numerator
        self.denominator = denominator
        Fraction.instances_count += 1

    def __str__(self):
        """

        :return: ділення дробу
        """
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """

        :param other:
        :return: додавання дробу
        """
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """

        :param other:
        :return: віднімання дробу
        """
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """

        :param other:
        :return: множення дробу
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """

        :param other:
        :return: ділення дробу
        """
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    @staticmethod
    def get_instances_count():
        """
        Статичний метод, який повертає кількість створених об'єктів класу "Дріб".

        Повертає:
            Кількість створених об'єктів класу "Дріб".
        """
        return Fraction.instances_count


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print(f"Дріб 1: {fraction1}")
print(f"Дріб 2: {fraction2}")

sum_fraction = fraction1 + fraction2
difference_fraction = fraction1 - fraction2
product_fraction = fraction1 * fraction2
quotient_fraction = fraction1 / fraction2

print(f"Сума: {sum_fraction}")
print(f"Різниця: {difference_fraction}")
print(f"Добуток: {product_fraction}")
print(f"Частка: {quotient_fraction}")
print(f"Кількість створених об'єктів: {Fraction.get_instances_count()}")


# Завдання 2
class TemperatureConverter:
    """
    Опис класу для конвертування температури.
    """

    conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Статичний метод для конвертування
        температури з Цельсія у Фаренгейт.

        Аргументи:
            celsius: Температура в Цельсіях.

        Повертає:
            Температура в Фаренгейтах.
        """
        TemperatureConverter.conversion_count += 1
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """
        Статичний метод для конвертування
        температури з Фаренгейта у Цельсій.

        Аргументи:
            fahrenheit: Температура в Фаренгейтах.

        Повертає:
            Температура в Цельсіях.
        """
        TemperatureConverter.conversion_count += 1
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def get_conversion_count():
        """
        Статичний метод для отримання
        кількості виконаних конвертувань температури.

        Повертає:
            Кількість виконаних конвертувань температури.
        """
        return TemperatureConverter.conversion_count


celsius = 20
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit}°F")

fahrenheit = 68
celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F = {celsius}°C")

print(f"Кількість конвертувань: {TemperatureConverter.get_conversion_count()}")


# Завдання 3
class UnitConverter:
    """
    Опис класу для конвертування одиниць вимірювання.
    """

    @staticmethod
    def meter_to_foot(meter):
        """
        Статичний метод для конвертування метрів в фути.

        Аргументи:
            meter: Довжина в метрах.

        Повертає:
            Довжина в футах.
        """
        return meter * 3.28084

    @staticmethod
    def foot_to_meter(foot):
        """
        Статичний метод для конвертування футів в метри.

        Аргументи:
            foot: Довжина в футах.

        Повертає:
            Довжина в метрах.
        """
        return foot / 3.28084


meter = 10
foot = UnitConverter.meter_to_foot(meter)
print(f"{meter} м = {foot} футів")

foot = 32.8
meter = UnitConverter.foot_to_meter(foot)
print(f"{foot} футів = {meter} м")


# Завдання 4
class InformationSystem:
    """
    Опис класу InformationSystem.
    """

    data = {}

    @staticmethod
    def _get_user_data(user_name):
        """
        Статичний метод для отримання даних про користувача.

        Аргументи:
            user_name: Ім'я користувача.

        Повертає:
            Список контактів користувача.
        """
        return InformationSystem.data.get(user_name, [])

    @classmethod
    def add_user(cls, user_name):
        """
        Класовий метод для додавання нового користувача.

        Аргументи:
            user_name: Ім'я користувача.
        """
        if user_name not in cls.data:
            cls.data[user_name] = []

    @classmethod
    def add_contact(cls, user_name, contact_name):
        """
        Класовий метод для додавання контакту для користувача.

        Аргументи:
            user_name: Ім'я користувача.
            contact_name: Ім'я контакту.
        """
        user_data = cls._get_user_data(user_name)
        if user_data:
            user_data.append(contact_name)
        else:
            user_data = [contact_name]
        cls.data[user_name] = user_data


InformationSystem.add_user("Ivan")
InformationSystem.add_user("Maria")

InformationSystem.add_contact("Ivan", "Petro")
print(InformationSystem.data)

InformationSystem.add_contact("Ivan", "Olga")
print(InformationSystem.data)

InformationSystem.add_contact("Maria", "Ivan")
print(InformationSystem.data)
