"""Database access and business logic (SQLite backend)."""
import sqlite3

from models import Item


class InventoryController:
    """Reads and writes inventory items in a SQLite database."""

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self._create_table()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _create_table(self) -> None:
        """Create the items table if it does not exist yet."""
        with self._connect() as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS items ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "item_name TEXT NOT NULL UNIQUE, "
                "quantity INTEGER NOT NULL, "
                "price INTEGER NOT NULL)"
            )

    def add_item(self, item: Item) -> int:
        """Insert an item (ignored if it already exists). Return rows added."""
        with self._connect() as conn:
            cur = conn.execute(
                "INSERT OR IGNORE INTO items (item_name, quantity, price) "
                "VALUES (?, ?, ?)",
                (item.item_name, item.quantity, item.price),
            )
            return cur.rowcount

    def migrate(self, records: list[dict]) -> int:
        """Copy old in-memory records into the database. Return rows added."""
        return sum(self.add_item(Item(**record)) for record in records)

    def get_all(self) -> list[Item]:
        """Return every item stored in the database."""
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT item_name, quantity, price FROM items ORDER BY id"
            ).fetchall()
        return [Item(*row) for row in rows]

    def total_stock_value(self) -> int:
        """Return the total stock value of all items."""
        return sum(item.value for item in self.get_all())
