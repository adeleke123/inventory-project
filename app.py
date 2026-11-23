"""Inventory application: SQLite-backed report."""
import os

from controllers import InventoryController
from inventory import items as legacy_items
from models import Item
from utils import print_report

DB_PATH = os.environ.get("DB_PATH", "inventory.db")


def main() -> None:
    """Migrate the old data, write one new item, and print the report."""
    controller = InventoryController(DB_PATH)
    added = controller.migrate(legacy_items)
    print(f"Migrated {added} new record(s) into SQLite ({DB_PATH})")
    controller.add_item(Item("Salt", 40, 300))
    items = controller.get_all()
    print_report(items, controller.total_stock_value())


if __name__ == "__main__":
    main()
