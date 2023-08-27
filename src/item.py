import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.message = args[0]
        else:
            self.message = f'Файл поврежден'

    def __str__(self):
        return self.message


class Item(InstantiateCSVError):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Не складываются')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            new_name = new_name[:10]
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, csv_file=os.path.join('..', 'src', 'items.csv')):
        if not os.path.exists(csv_file) or csv_file is None:
            raise FileNotFoundError('Отсутствует файл')
        with open(csv_file, 'r', encoding='windows-1251') as csvfile:
            Item.all.clear()
            reader = csv.DictReader(csvfile)
            if reader.fieldnames != 3:
                raise InstantiateCSVError
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls.all.append(cls(name, price, quantity))

    @staticmethod
    def string_to_number(str_num):
        return int(float(str_num))
