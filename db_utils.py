from datetime import datetime
from typing import List
import random

class Product:
    def __init__(self, id, name, exp_date, log_date, is_fav, note=""):
        self.id = id
        self.name = name
        self.exp_date = exp_date
        self.log_date = log_date
        self.is_fav: bool = is_fav
        self.note = note

    def to_string(self):
        return f"{self.id}_{self.name}_{self.exp_date}_{self.log_date}_{self.is_fav}_{self.note}"

    def get_remaining_days(self) -> int:
        today = datetime.now()
        exp_date = datetime.strptime(self.exp_date, "%m-%d-%Y")
        try:
            diff = (exp_date - today).days
            if diff == 0:
                return 1
            else:
                return diff
        except ValueError:
            return -((today - exp_date).days)


class ProductDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.products: List[Product] = self.load()
        self.sort_products_by_expiry()

    def load(self):
        products = []
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split("_")
                    if len(parts) == 6:
                        item_id = int(parts[0])
                        name = parts[1]
                        exp_date = parts[2]
                        log_date = parts[3]
                        is_fav = parts[4]
                        note = parts[5]
                        product = Product(item_id, name, exp_date, log_date, is_fav, note)
                        products.append(product)
        except FileNotFoundError:
            print("Database file not found.")
        return products

    def reload(self) -> None:
        self.products = self.load()
        self.sort_products_by_expiry()

    def save_products(self, products):
        with open(self.filename, "w") as file:
            for product in products:
                file.write(product.to_string() + "\n")

    def _get_next_id(self):
        return len(self.products) + 1

    def add_product(self, name, exp_date, is_fav: str, note=""):
        product_id = self._get_next_id()
        log_date = datetime.now().strftime("%m-%d-%Y")
        product = Product(product_id, name, exp_date, log_date, (is_fav == 'true'), note)

        with open(self.filename, "a") as file:
            file.write(product.to_string() + "\n")

        print("Product saved successfully!")

    def view_products(self):
        if not self.products:
            print("No products found.")
            return

        # Sort by expiration date
        self.products.sort(key=lambda p: datetime.strptime(p.exp_date, "%m-%d-%Y"))

        # Reassign IDs and update file
        for i, product in enumerate(self.products, start=1):
            product.id = i
        self.save_products(self.products)

        print("\nStored Products (Sorted by Expiration Date):")
        for product in self.products:
            remaining_days = product.get_remaining_days()
            if remaining_days is None:
                status = "Invalid date format"
            elif remaining_days < 0:
                status = "EXPIRED"
            else:
                status = f"{remaining_days} day(s) left"

            print(f"ID: {product.id} | Name: {product.name} | Expiry: {product.exp_date} "
                  f"| Log Date: {product.log_date} | Remaining: {status} | Note: {product.note}")

    def search_product_by_id(self, search_id):
        for product in self.products:
            if product.id == search_id:
                return product
        return None

    def delete_product_by_id(self, delete_id):
        updated_products = [p for p in self.products if p.id != delete_id]

        if len(self.products) == len(updated_products):
            print("Product not found.")
            return

        # Reassign IDs and update file
        for i, product in enumerate(updated_products, start=1):
            product.id = i
        self.save_products(updated_products)

        print(f"Product with ID {delete_id} has been deleted and IDs have been updated.")

    def sort_products_by_expiry(self):
        self.quickSort(self.products, 0, len(self.products) - 1)

    # Partition function
    def partition(self, arr: List[Product], low: int, high: int):
    
        # Choose the pivot
        pivot = self.products[high]

        # Index of smaller element and indicates 
        # the right position of pivot found so far
        i = low - 1

        # Traverse arr[low..high] and move all smaller
        # elements to the left side. Elements from low to 
        # i are smaller after every iteration
        for j in range(low, high):
            if arr[j].get_remaining_days() < pivot.get_remaining_days():
                i += 1
                self.swap(arr, i, j)

        # Move pivot after smaller elements and
        # return its position
        self.swap(arr, i + 1, high)
        return i + 1

    # Swap function
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    # The QuickSort function implementation
    def quickSort(self, arr, low, high):
        if low < high:

            # pi is the partition return index of pivot
            pi = self.partition(arr, low, high)

            # Recursion calls for smaller elements
            # and greater or equals elements
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)