"""Data models for the inventory application."""
from dataclasses import dataclass


@dataclass
class Item:
    """A single inventory item."""

    item_name: str
    quantity: int
    price: int

    @property
    def value(self) -> int:
        """Return the stock value (quantity x price)."""
        return self.quantity * self.price
