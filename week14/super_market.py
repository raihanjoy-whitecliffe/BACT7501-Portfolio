class StockInfo:
    def __init__(self, id, product_name, price, quantity):
        self.id = id
        self.name = product_name
        self.price = price
        self.quantity = quantity

class StockManagement:
    def __init__(self):
        #list to store added products
        self.products = []
        #list to store the items sold
        self.sales = []
        #inital id for the products
        self.id=1
    #method for registering items in the system
    def product_register(self):
        print("-------Product Registration-------")
        name= input("Enter product name: ")
        for p in self.products:
            if p.name == name:
                print("Product already exists")
                return
        price= float(input("Enter product price: "))
        qty= int(input("Enter product quantity: "))
        stock_info=StockInfo(self.id,name, price, qty)
        self.products.append(stock_info)
        self.id+=1
    #method for updating the stock
    def update_stock(self):
        print("------Stock Update------")
        product_id= int(input("Enter product id: "))
        for p in self.products:
            #updating the correct product
            if p.product_id == product_id:
                new_qty= int(input("Enter new quantity: "))
                self.quantity = new_qty
                print("Updated Successfully")
                return
        print("Product not found")
    #method for selling products and updating the stock level
    def product_sale(self):
        print("------Selling Product------")
        product_id= int(input("Enter product id: "))
        for p in self.products:
            if p.id == product_id:
                qty= int(input("Enter quantity: "))
                p.quantity -= qty
                total= qty*p.price
                sold={"ID":product_id,"Quantity":qty,"Total":total}
                self.sales.append(sold)
                return
    #method for searching the products by their id
    def search_product(self):
        print("------Searching Products------")
        product_id= int(input("Enter product id: "))
        for p in self.products:
            #validating the product search
            if p.id == product_id:
                print("Product found")
                print("ID:",p.id)
                print("Name:",p.name)
                print("Price:",p.price)
                print("Quantity:",p.quantity)
                return
        print("Product not found")
    #
    def display_summary(self):
        print("------Summary of Products------")
        print("Total Number of products: ",len(self.products))
        total=0
        total_sold=0
        for sold in self.sales:
            total+=sold["Total"]
            total_sold+=sold["Quantity"]
        print("Total Items Sold: ",total_sold)
        print("Total Sales Value: ", total)
        for p in self.products:
            print(f'ID: {p.id} | Quantity: {p.quantity}')
    def show_all(self):
        print("------All Products------")
        for p in self.products:
            print(f'ID: {p.id} | Quantity: {p.quantity}')
test=StockManagement()
while True:
    print("----------Menu-----------")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Update Stock")
    print("4. Sell Product")
    print("5. Search Product")
    print("6. View Sales Summary")
    print("7. Exit")
    entry= int(input("Enter your choice: "))
    if entry == 1:
        test.product_register()
    elif entry == 2:
        test.show_all()
    elif entry == 3:
        test.update_stock()
    elif entry == 4:
        test.product_sale()
    elif entry == 5:
        test.search_product()
    elif entry == 6:
        test.display_summary()
    elif entry == 7:
        break