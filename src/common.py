from collections import namedtuple

Order = namedtuple("Order", ["date", "quantity"])
Price = namedtuple("Price", ["from_date", "to_date", "price"])


def print_list(l: list) -> None:
    for item in l:
        print(item)
