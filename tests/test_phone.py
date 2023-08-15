import pytest
from src.phone import Phone
from src.item import Item


def test_phone_4():

    test1 = Phone('Nokia', 2000, 10, 1)
    assert test1.number_of_sim == 1
    assert test1.calculate_total_price() == 20000
    assert test1.__str__() == "Nokia"
    assert test1.__repr__() == "Phone('Nokia', 2000, 10, 1)"
    with pytest.raises(ValueError):
        test1.number_of_sim = 0
        test3 = Phone('Model', 0, 0, 0)

    test2 = Phone('Sony', 2500, 30, 2)
    assert test1 + test2 == 40

    item = Item('Product', 30000, 5)
    assert test1 + item == 15
