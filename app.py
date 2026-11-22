from datetime import datetime

from inventory import items
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    total = 0
    for item in items:
        total += item["quantity"] * item["price"]
    return total


print("=" * 42)
print("            INVENTORY REPORT")
print("=" * 42)
print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M"))
print(f"{'Item':<12}{'Qty':>6}{'Price':>10}{'Value':>14}")
print("-" * 42)
for item in items:
    value = item["quantity"] * item["price"]
    print(f"{item['item_name']:<12}{item['quantity']:>6}{item['price']:>10,}{value:>14,}")
print("-" * 42)
print(f"{'Total stock value:':<28}{total_stock_value(items):>14,}")
print(f"{'Highest stock:':<28}{highest_stock_item(items)['item_name']:>14}")
print(f"{'Lowest stock:':<28}{lowest_stock_item(items)['item_name']:>14}")
