# Shoe Inventory CLI (OOP)

## Overview
- Simple, object‑oriented Python CLI to manage a shoe inventory.
- Core entity is a Shoe class with fields: country, code, product, cost, quantity.
- Loads initial data from inventory.txt and provides menu-driven operations.

## What It Does
- Load inventory from inventory.txt into memory.
- View all shoes with formatted details.
- Capture a new shoe via prompts.
- Restock the shoe with the lowest quantity.
- Search a shoe by its code.
- Calculate total value per item (cost × quantity).
- Show the shoe with the highest quantity (for sale).

## Files
- Main program: # inventory.py
- Additional test stub: import unittest.py (references modules not included here).

## Requirements
- Python 3.8+.
- inventory.txt in the same directory, CSV formatted:
  - Header row, then rows: country,code,product,cost,quantity
  - Example:
    ```
    country,code,product,cost,quantity
    South Africa,SKU123,Nike Air,999.99,20
    USA,SKU124,Adidas Runner,799.50,15
    ```

## Running
- From this folder, run the program:
  - Windows PowerShell:
    ```
    python ".\# inventory.py"
    ```
  - CMD:
    ```
    python "# inventory.py"
    ```
- Follow the on-screen menu to perform operations.

## Notes
- The test file import unittest.py demonstrates a unittest structure targeting a TaskService in src/, which is not part of this shoe inventory program and may not run here.

- https://github.com/hyperiondev-bootcamps/JO25080018810/tree/main/Level%201%20-%20Python%20for%20Software%20Engineering/M03T07%20%E2%80%93%20OOP%20%E2%80%93%20Synthesis


