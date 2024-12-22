from ..src.step_1 import solve as solve_1
from ..src.step_2 import solve as solve_2
from ..src.common import Order, Price
from datetime import date
import pytest


class TestSolve:
    @pytest.mark.parametrize("solve", [solve_1, solve_2])
    def test_空リスト(self, solve: callable):
        solve([], []) == []

    @pytest.mark.parametrize("solve", [solve_1, solve_2])
    def test_1件(self, solve: callable):
        orders = [Order(date=date(2021, 1, 1), quantity=1)]
        prices = [Price(from_date=date(2021, 1, 1), to_date=date(2021, 1, 2), price=1)]
        assert solve(orders, prices) == [(orders[0], prices[0])]

    @pytest.mark.parametrize("solve", [solve_1, solve_2])
    def test_3件(self, solve: callable):
        orders = [
            Order(date=date(2021, 1, 1), quantity=1),
            Order(date=date(2021, 1, 2), quantity=1),
            Order(date=date(2021, 1, 3), quantity=1),
        ]
        prices = [
            Price(from_date=date(2021, 1, 1), to_date=date(2021, 1, 2), price=1),
            Price(from_date=date(2021, 1, 2), to_date=date(2021, 1, 3), price=2),
            Price(from_date=date(2021, 1, 3), to_date=date(2021, 1, 4), price=3),
        ]
        assert solve(orders, prices) == [
            (orders[0], prices[0]),
            (orders[1], prices[1]),
            (orders[2], prices[2]),
        ]
