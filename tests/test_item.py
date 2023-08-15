"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


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


def test_item_3():
    item = Item('Smartphone', 200, 10)
    assert repr(item) == "Item('Smartphone', 200, 10)"
    assert str(item) == 'Smartphone'


def test_item_4():
    item = Item('Fridge', 30000, 10)
    phone = Phone('LG', 5000, 5, 2)
    assert item + phone == 15
