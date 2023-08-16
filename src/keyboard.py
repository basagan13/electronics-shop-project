from src.item import Item


class MixinLog:
    def __init__(self, language: str = 'EN') -> None:
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language.upper() == 'EN':
            self.__language = 'RU'
        elif self.__language.upper() == 'RU':
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLog):
    pass
