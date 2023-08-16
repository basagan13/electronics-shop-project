import pytest
from src.keyboard import Keyboard


def test_keyboard_5():
    keyboard = Keyboard('HP', 5000, 30)
    assert str(keyboard) == 'HP'
    assert keyboard.calculate_total_price() == 150_000

    assert keyboard.language == 'EN'

    keyboard.change_lang()
    assert keyboard.language == 'RU'

    keyboard.change_lang().change_lang().change_lang()
    assert keyboard.language == 'EN'

    with pytest.raises(AttributeError):
        keyboard.language = 'IT'
