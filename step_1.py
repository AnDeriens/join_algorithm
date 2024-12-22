from collections import namedtuple
import time
from datetime import date, timedelta



Order = namedtuple("Order", ["date", "quantity"])
Price = namedtuple("Price", ["from_date", "to_date", "price"])


def print_list(l: list) -> None:
    for item in l:
        print(item)


def init(n: int) -> tuple[list[Order], list[Price]]:
    today = date.today()
    orders = [Order(today + timedelta(days=i), 1) for i in range(n)]
    prices = [Price(today + timedelta(days=i), today + timedelta(days=1 + i), 1 + i) for i in range(n)]
    return orders, prices

def main() -> None:
    N = 3
    orders, prices = init(100000)

    # print("inputs")
    # print_list(orders)
    # print_list(prices)

    start_time = time.time()
    results = []
    for order in orders:
        for price in prices:
            if price.from_date <= order.date < price.to_date:
                results.append((order, price))

    # print("results")
    # print_list(results)

    print("elapsed time:", time.time() - start_time)


if __name__ == "__main__":
    main()