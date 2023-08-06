"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def good():
    return Item('good', 30.0, 5)


def test_item(good):
    assert good.calculate_total_price() == 150.0

    Item.pay_rate = 0.8
    good.apply_discount()
    assert good.calculate_total_price() == 120.0


def test_item_2():
    new = Item('', 100, 5)
    new.name = 'TV'
    assert new.name == 'TV'
    assert new.price == 100

    new.name = 'СуперТелевизор'
    assert new.name == 'СуперТелев'

    assert Item.string_to_number('3.25') == 3
    assert Item.string_to_number('0.35') == 0
    assert Item.string_to_number(False) == 0

