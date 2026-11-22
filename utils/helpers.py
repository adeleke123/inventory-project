def highest_stock_item(items):
    return max(items, key=lambda i: i["quantity"])


def lowest_stock_item(items):
    return min(items, key=lambda i: i["quantity"])
