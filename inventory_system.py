"""
Inventory System
Fixes applied based on pylint, bandit, and flake8 reports:
- Added module and function docstrings
- Fixed mutable default argument (logs=None)
- Removed unused import (logging now used)
- Added input validation
- Replaced bare except with specific exceptions
- Added encoding and 'with open' for file handling
- Removed eval() call (Bandit B307)
- Used f-strings for cleaner output/logging
"""

import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def addItem(item="default", qty=0, logs=None):
    """Add item with quantity to the stock_data dictionary."""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str) or not item:
        logging.error("Invalid item name: %s", item)
        return
    if not isinstance(qty, int):
        logging.error("Invalid quantity type for %s: %s", item, type(qty).__name__)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def removeItem(item, qty):
    """Remove quantity of an item from stock_data."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        logging.info("Removed %d of %s", qty, item)
    except KeyError:
        logging.warning("Item '%s' not found in stock_data.", item)
    except TypeError:
        logging.error("Invalid quantity type when removing %s", item)


def getQty(item):
    """Return quantity of an item if it exists, else 0."""
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):
    """Load stock_data from a JSON file safely."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Loaded data from %s", file)
    except FileNotFoundError:
        logging.warning("File %s not found. Starting with empty stock_data.", file)
        stock_data = {}
    except json.JSONDecodeError:
        logging.error("Failed to decode JSON data from %s", file)


def saveData(file="inventory.json"):
    """Save stock_data to a JSON file safely."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Saved data to %s", file)
    except Exception as e:
        logging.error("Error saving data: %s", e)


def printData():
    """Print all items and quantities."""
    print("Items Report")
    for i, qty in stock_data.items():
        print(f"{i} -> {qty}")


def checkLowItems(threshold=5):
    """Return list of items with quantity below threshold."""
    return [i for i, q in stock_data.items() if q < threshold]


def main():
    """Main function demonstrating inventory operations."""
    addItem("apple", 10)
    addItem("banana", -2)
    addItem("grapes", 5)
    removeItem("apple", 3)
    removeItem("orange", 1)

    print(f"Apple stock: {getQty('apple')}")
    print(f"Low items: {checkLowItems()}")

    saveData()
    loadData()
    printData()


if __name__ == "__main__":
    main()
