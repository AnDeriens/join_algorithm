import time
from datetime import date, timedelta
from common import Order, Price


def init(n: int) -> tuple[list[Order], list[Price]]:
    today = date(1970, 1, 1)
    orders = [Order(today + timedelta(days=i), 1) for i in range(n)]
    prices = [
        Price(today + timedelta(days=i), today + timedelta(days=1 + i), 1 + i)
        for i in range(n)
    ]
    return orders, prices


def solve(orders: list[Order], prices: list[Price]) -> list[tuple[Order, Price]]:
    # ここを書き換える
    results = []
    # orders と pricesはそれぞれ日付順にソートされている前提
    start_index = 0
    for order in orders:
        for i in range(start_index, len(prices)):
            if len(prices) - 1 == i:
                results.append((order, prices[i]))
                break

            if prices[i].from_date <= order.date < prices[i + 1].from_date:
                results.append((order, prices[i]))
                start_index = i
                break
    return results


def main() -> None:
    orders, prices = init(10000000)

    start_time = time.time()
    solve(orders, prices)

    print("elapsed time:", time.time() - start_time)


if __name__ == "__main__":
    main()
