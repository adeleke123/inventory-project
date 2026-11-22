"""Helper functions for inventory stock levels."""


def highest_stock_item(items):
    """Return the item with the largest quantity in stock."""
    return max(items, key=lambda i: i["quantity"])


def lowest_stock_item(items):
    """Return the item with the smallest quantity in stock."""
    return min(items, key=lambda i: i["quantity"])
