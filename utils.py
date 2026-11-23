"""Helper functions: stock lookups and report formatting."""
from datetime import datetime

from models import Item

LINE_WIDTH = 42


def highest_stock_item(items: list[Item]) -> Item:
    """Return the item with the largest quantity in stock."""
    return max(items, key=lambda i: i.quantity)


def lowest_stock_item(items: list[Item]) -> Item:
    """Return the item with the smallest quantity in stock."""
    return min(items, key=lambda i: i.quantity)


def print_report(items: list[Item], total: int) -> None:
    """Print the inventory report as a formatted table."""
    print("=" * LINE_WIDTH)
    print("            INVENTORY REPORT")
    print("=" * LINE_WIDTH)
    print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M"))
    print(f"{'Item':<12}{'Qty':>6}{'Price':>10}{'Value':>14}")
    print("-" * LINE_WIDTH)
    for item in items:
        print(
            f"{item.item_name:<12}{item.quantity:>6}"
            f"{item.price:>10,}{item.value:>14,}"
        )
    print("-" * LINE_WIDTH)
    print(f"{'Total stock value:':<28}{total:>14,}")
    print(f"{'Highest stock:':<28}{highest_stock_item(items).item_name:>14}")
    print(f"{'Lowest stock:':<28}{lowest_stock_item(items).item_name:>14}")
