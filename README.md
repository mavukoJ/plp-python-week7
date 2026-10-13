# Week 7 Assignment: Shopping List Manager

In this assignment, I practiced using Python lists to store and manage items. I learned how to add and remove items, check whether an item exists, and use loops to create a simple report.

## Files in this repository

- `list_warmup.py` — Demonstrates how to access, add, and remove fruits from a list and count the remaining items.
- `shopping_list.py` — Allows a user to add, remove, and display shopping items using a simple menu.
- `list_report.py` — Prints a numbered shopping list, counts item names longer than four characters, and finds the longest name using a loop.
- `README.md` — Explains the assignment and describes the files.
- `screenshots/` — Contains screenshots showing the programs running.

## Why is it safer to check `in` before calling `.remove()`?

It is safer to check whether an item is in the list before removing it because `.remove()` raises a `ValueError` if the item is missing. Using `if item in shopping_list` helps prevent this error and allows the program to continue running without crashing.