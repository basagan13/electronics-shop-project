"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def apple():
    return Item('apple', 30.0, 5)


def test_item(apple):
    assert apple.calculate_total_price() == 150.0

    Item.pay_rate = 0.8
    apple.apply_discount()
    assert apple.calculate_total_price() == 120.0
