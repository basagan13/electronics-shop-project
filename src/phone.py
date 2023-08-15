from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        if num <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = num

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Не складываются')
        return self.quantity + other.quantity

    def __radd__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Не складываются')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', "\
               f"{self.price}, {self.quantity}, {self.number_of_sim})"

