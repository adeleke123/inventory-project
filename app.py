from datetime import datetime

from inventory import items
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(items):
    total = 0
    for item in items:
        total += item["quantity"] * item["price"]
    return total


print("=== Inventory Report ===")
print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M"))
for item in items:
    print(item["item_name"], "-", item["quantity"], "units @", item["price"])

print("Total stock value:", total_stock_value(items))
print("Highest stock:", highest_stock_item(items)["item_name"])
print("Lowest stock:", lowest_stock_item(items)["item_name"])
