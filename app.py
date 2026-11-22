"""Inventory report: reads inventory.py and prints the stock values."""
from datetime import datetime

from inventory import items
from utils.helpers import highest_stock_item, lowest_stock_item

# Width of the report table, kept in one place so it is easy to change
LINE_WIDTH = 42


def item_value(item):
    """Return the stock value of one item (quantity x price)."""
    return item["quantity"] * item["price"]


def total_stock_value(items):
    """Return the total stock value of all items."""
    return sum(item_value(item) for item in items)


def print_header():
    """Print the report title and the date it was generated."""
    print("=" * LINE_WIDTH)
    print("            INVENTORY REPORT")
    print("=" * LINE_WIDTH)
    print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M"))


def print_item_rows(items):
    """Print one table row for each item."""
    print(f"{'Item':<12}{'Qty':>6}{'Price':>10}{'Value':>14}")
    print("-" * LINE_WIDTH)
    for item in items:
        print(
            f"{item['item_name']:<12}{item['quantity']:>6}"
            f"{item['price']:>10,}{item_value(item):>14,}"
        )
    print("-" * LINE_WIDTH)


def print_summary(items):
    """Print the total value and the highest and lowest stock items."""
    print(f"{'Total stock value:':<28}{total_stock_value(items):>14,}")
    print(f"{'Highest stock:':<28}{highest_stock_item(items)['item_name']:>14}")
    print(f"{'Lowest stock:':<28}{lowest_stock_item(items)['item_name']:>14}")


def main():
    """Run the inventory report."""
    if not items:
        print("No items in inventory.")
        return
    print_header()
    print_item_rows(items)
    print_summary(items)


if __name__ == "__main__":
    main()
