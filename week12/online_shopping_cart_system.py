class ShoppingCart:
    total_price = 0

    def __init__(self, customer_name, product_name, product_price, product_quantity, discount, disc_price):
        self.customer_name = customer_name
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity
        self.discount = discount
        self.disc_price = disc_price

    def calculate_total(self):
        # Calculates and saves total_price directly to the object using self
        self.total_price = self.product_price * self.product_quantity
        return self.total_price

    def apply_discount(self):
        # Uses self.total_price calculated from the previous step
        if self.total_price >= 500:
            self.discount = self.total_price * 0.1
            self.disc_price = self.total_price - (self.total_price * 0.10)
        else:
            self.discount = 0
            self.disc_price = self.total_price

    def display_cart(self):
        print(f'Customer Name: {self.customer_name}')
        print(f'Product Name: {self.product_name}')
        print(f'Product Price: {self.product_price}')
        print(f'Product Quantity: {self.product_quantity}')
        print(f'Total Price: {self.total_price}')
        print(f'Discount: {self.discount}')
        print(f'Price after Discount: {self.disc_price}')

shopping1 = ShoppingCart("Raihan", "Mexicano Thai Sweet Chilli", 5.99, 2, 0, 0)
shopping1.calculate_total()
shopping1.apply_discount()
shopping1.display_cart()

shopping2 = ShoppingCart("Raihan", "Mexicano Natural", 5.99, 3, 0, 0)
shopping2.calculate_total()
shopping2.apply_discount()
shopping2.display_cart()