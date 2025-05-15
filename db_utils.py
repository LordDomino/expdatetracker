from datetime import datetime

class Product:
    def __init__(self, id, name, expiration_date, log_date):
        self.id = id
        self.name = name
        self.expiration_date = expiration_date
        self.log_date = log_date

    def to_string(self):
        return f"{self.id}_{self.name}_{self.expiration_date}_{self.log_date}"

    def get_remaining_days(self) -> int:
        try:
            exp_date = datetime.strptime(self.expiration_date, "%m-%d-%Y")
            today = datetime.now()
            return (exp_date - today).days
        except ValueError:
            return None

class ProductDatabase:
    def __init__(self, filename):
        self.filename = filename
        self.products = self.load_products()

    def load_products(self):
        products = []
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split("_")
                    if len(parts) == 4:
                        product_id = int(parts[0])
                        name = parts[1]
                        expiration_date = parts[2]
                        log_date = parts[3]
                        product = Product(product_id, name, expiration_date, log_date)
                        products.append(product)
        except FileNotFoundError:
            print("Database file not found.")
        return products

    def save_products(self, products):
        with open(self.filename, "w") as file:
            for product in products:
                file.write(product.to_string() + "\n")

    def _get_next_id(self):
        return len(self.products) + 1

    def add_product(self, name, expiration_date):
        product_id = self._get_next_id()
        log_date = datetime.now().strftime("%m-%d-%Y")
        product = Product(product_id, name, expiration_date, log_date)

        with open(self.filename, "a") as file:
            file.write(product.to_string() + "\n")

        print("Product saved successfully!")

    def view_products(self):
        if not self.products:
            print("No products found.")
            return

        # Sort by expiration date
        self.products.sort(key=lambda p: datetime.strptime(p.expiration_date, "%m-%d-%Y"))

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

            print(f"ID: {product.id} | Name: {product.name} | Expiry: {product.expiration_date} "
                  f"| Log Date: {product.log_date} | Remaining: {status}")

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