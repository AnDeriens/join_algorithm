import time
from datetime import date, timedelta
from .common import Order, Price, print_list


def init(n: int) -> tuple[list[Order], list[Price]]:
    today = date.today()
    orders = [Order(today + timedelta(days=i), 1) for i in range(n)]
    prices = [
        Price(today + timedelta(days=i), today + timedelta(days=1 + i), 1 + i)
        for i in range(n)
    ]
    return orders, prices


def solve(orders: list[Order], prices: list[Price]) -> list[tuple[Order, Price]]:
    results = []
    for order in orders:
        for price in prices:
            if price.from_date <= order.date < price.to_date:
                results.append((order, price))
    return results


def main() -> None:
    orders, prices = init(10)

    # print("inputs")
    # print_list(orders)
    # print_list(prices)

    start_time = time.time()
    results = solve(orders, prices)

    # print("results")
    # print_list(results)

    print("elapsed time:", time.time() - start_time)


if __name__ == "__main__":
    main()
